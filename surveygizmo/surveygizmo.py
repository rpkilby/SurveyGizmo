
import oauth_helper
import requests
import hashlib
import imp


class ImproperlyConfigured(Exception):
    """ SurveyGizmo is somehow improperly configured."""
    pass


class InvalidFilter(Exception):
    """ Filter format is invalid."""
    pass


class _Config(object):
    def __init__(self, _sg, **kwargs):
        self._sg = _sg
        self._api_version = kwargs.get('api_version', 'head')
        self.auth_method = kwargs.get('auth_method', None)
        self.username = kwargs.get('username', None)
        self.password = kwargs.get('password', None)
        self.md5_hash = kwargs.get('md5_hash', None)
        self.consumer_key = kwargs.get('consumer_key', None)
        self.consumer_secret = kwargs.get('consumer_secret', None)
        self.access_token = kwargs.get('access_token', None)
        self.access_token_secret = kwargs.get('access_token_secret', None)
        self.response_type = kwargs.get('response_type', None)

    def validate(self):
        """ Perform validation check on properties.
        """
        if not self.api_version in ['v3', 'head']:
            raise ImproperlyConfigured("API version provided is invalid.")

        if not self.auth_method in ['user:pass', 'user:md5', 'oauth']:
            raise ImproperlyConfigured("No authentication method provided.")
        else:
            if self.auth_method == "user:pass":
                if not self.username or not self.password:
                    raise ImproperlyConfigured("Username and password for 'user:pass' authentication.")
            elif self.auth_method == "user:md5":
                if not self.username:
                    raise ImproperlyConfigured("Username required for 'user:md5' authentication.")
                elif not self.password and not self.md5_hash:
                    raise ImproperlyConfigured("Password or md5 hash of password required for 'user:md5' authentication.")
            elif self.auth_method == "oauth":
                if not self.consumer_key or not self.consumer_secret or \
                   not self.access_token or not self.access_token_secret:
                    raise ImproperlyConfigured("OAuth consumer key and secret, and OAuth access token and secret required for 'oauth' authentication.")

        if not self.response_type in ["json", "pson", "xml", "debug", None]:
            raise ImproperlyConfigured()

    @property
    def api_version(self):
        return self._api_version

    @api_version.setter
    def api_version(self, value):
        self._api_version = value
        self._sg.api._check_version()


class _Field(object):
    associations = {
        'surveyresponse': [
            '[question(%d)]',
            '[question(%d), option(%d)]'
            'datesubmitted',
            'istestdata',
            'status',
            'contact_id',
        ],
        'survey': [
            'createdon',
            'modifiedon',
            'title',
            'subtype',
            'team',
            'status',
        ],
        'surveycampaign': [
            '_type',
            'name',
            'ssl',
            'datecreated',
            'datemodified',
            'status',
        ],
    }


class _API(object):
    base_url = "https://restapi.surveygizmo.com/"
    head = 'v3'

    def __init__(self, _sg):
        self._sg = _sg
        self._api_version = None
        self._modules = None
        self._filters = []
        self._session = None

    def _check_version(self):
        """ update api modules, wrap callables.
        """
        if self._api_version != self._sg.config.api_version:
            self._api_version = self._sg.config.api_version
            self._modules = {}

            api_version = self.head if self._api_version == 'head' else self._api_version

            module_list = getattr(__import__('api', globals(), locals(), [api_version]), api_version).__all__
            _, package_path, _ = imp.find_module('surveygizmo')
            search_path = '%s/api/%s' % (package_path, api_version)

            for module_name in module_list:
                find_result = imp.find_module(module_name, [search_path])
                module = imp.load_module("_api_loaded_%s" % module_name, *find_result)

                for name, func in module.__dict__.items():
                    if callable(func) and not name.startswith('__'):
                        setattr(module, name, self._wrap(func))

                self._modules[module_name] = module

    def __getattr__(self, name):
        """ retrieve modules loaded from api
        """
        if self._modules.get(name, None) is not None:
            return self._modules[name]
        raise AttributeError(name)

    def _wrap(self, func):
        """ wrap api callable's such that their return values
            are immediately executed
        """
        def wrapper(*args, **kwargs):
            keep = kwargs.pop('keep', False)
            tail, params = func(*args, **kwargs)

            response_type = self._sg.config.response_type
            if response_type:
                tail = "%s.%s" % (tail, response_type)
            tail = "%s/%s" % (self._api_version, tail)

            return self.execute(tail, params, keep)
        return wrapper

    def add_filter(self, field, operator, value):  # , object_type=None):
        """ Add a query filter to be applied to the next API call.
            :param field: Field name to filter by
            :type field: str
            :param operator: Operator value
            :type operator: str
            :param value: Value of filter
            :type value: str
            :param object_type: Optional. Checks field for object association
            :type object_type: str

            Known Filters:
                Question                    [question(2)]                   surveyresponse
                Question Option             [question(2), option(10001)]    surveyresponse
                Date Submitted              datesubmitted                   surveyresponse
                Is Test Data                istestdata                      surveyresponse
                Status                      status                          surveyresponse
                Contact ID                  contact_id                      surveyresponse
                Creation Time               createdon                       survey
                Last Modified Time          modifiedon                      survey
                Survey Title                title                           survey
                Type of Project             subtype                         survey
                Team Survey Belongs To      team                            survey
                Status                      status                          survey
                Type of Link                type                            surveycampaign
                Name of Link                name                            surveycampaign
                Secure / Unsecure Link      ssl                             surveycampaign
                Link Created Date           datecreated                     surveycampaign
                Link Last Modified Date     datemodified                    surveycampaign
                Status                      status                          surveycampaign


            Known Operators:
                ==
                !=
                >=
                <=
                >
                <
                =           (==)
                <>          (!=)
                IS NULL     Value is True or False
                IS NOT NULL Value is True or False
                in          Value is comma separated list
        """
        i = len(self._filters)
        self._filters.append({
            'filter[field][%d]' % i: str(field),
            'filter[operator][%d]' % i: str(operator),
            'filter[value][%d]' % i: str(value),
        })

    def execute(self, tail, params, keep=False):
        """ Executes a call to the API.
            :param tail: The tail portion of the URL. This should not include
            the domain name.
            :param params: Query parameters passed to API.
            :param keep: Keep filters for next API call. Defaults to False.
        """
        self._sg.config.validate()

        for _filter in self._filters:
            params.update(_filter)
        if not keep:
            self._filters = []

        config = self._sg.config
        if config.auth_method == 'user:pass':
            params.update({
                config.auth_method: "%s:%s" % (config.username, config.password),
            })
            url = "%s%s" % (self.base_url, tail)
            response = requests.get(url, params=params)

        elif config.auth_method == 'user:md5':
            if not config.md5_hash:
                config.md5_hash = hashlib.md5(config.password).hexdigest()
            params.update({
                config.auth_method: "%s:%s" % (config.username, config.md5_hash),
            })
            url = "%s%s" % (self.base_url, tail)
            response = requests.get(url, params=params)

        else:  # 'oauth'
            if not self._session:
                self._session = oauth_helper.SGAuthService(
                    config.consumer_key, config.consumer_secret,
                    config.access_token, config.access_token_secret
                ).get_session()

            response = self._session.get(tail, params)

        response.raise_for_status()

        if not config.response_type:
            return response.json()
        else:
            return response.text


class SurveyGizmo(object):
    """
    """
    def __init__(self, **kwargs):
        self.config = _Config(self, **kwargs)
        self.api = _API(self)
        self.api._check_version()
