
import oauth_helper
import requests
import hashlib
import imp

# "https://restapi.surveygizmo.com/v1/survey/{$survey}/surveyresponse?user:pass={$user}:{$pass}{$status}{$datesubmmitted}"


class ImproperlyConfigured(Exception):
    """ SurveyGizmo is somehow improperly configured."""
    pass


class _Config(object):
    def __init__(self, _sg, **kwargs):
        self._sg = _sg
        self._api_version = kwargs.get('api_version', 'head')
        self.auth_method = kwargs.get('auth_method', None)
        self.username = kwargs.get('username', None)
        self.password = kwargs.get('password', None)
        self.md5_hash = kwargs.get('md5_hash', None)
        self.oauth_consumer_key = kwargs.get('oauth_consumer_key', None)
        self.oauth_consumer_secret = kwargs.get('oauth_consumer_secret', None)
        self.oauth_token = kwargs.get('oauth_token', None)
        self.oauth_token_secret = kwargs.get('oauth_token_secret', None)
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
                if not self.oauth_consumer_key or not self.oauth_consumer_secret or \
                   not self.oauth_token or not self.oauth_token_secret:
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


class _API(object):
    base_url = "https://restapi.surveygizmo.com/"
    head = 'v3'

    def __init__(self, _sg):
        self._sg = _sg
        self._api_version = None
        self._modules = None
        self._filters = {}
        self._session = None

    def _check_version(self):
        """ update api modules, wrap callables.
        """
        if self._api_version != self._sg.config.api_version:
            self._api_version = self._sg.config.api_version
            self._modules = {}

            api_version = self.head if self._api_version == 'head' else self._api_version

            module_list = getattr(__import__('api', globals(), locals(), [api_version]), api_version).__all__
            search_path = 'surveygizmo/api/%s' % api_version

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
            tail, params = func(*args, **kwargs)

            response_type = self._sg.config.response_type
            if response_type:
                tail = "%s.%s" % (tail, response_type)
            tail = "%s/%s" % (self._api_version, tail)

            return self.execute(tail, params)
        return wrapper

    def add_filter(self, params):
        """ Add a query filter to be applied to the next API call.
        """
        pass

    def execute(self, tail, params, keep=False):
        """ Executes a call to the API.
            :param tail: The tail portion of the URL. This should not include
            the domain name.
            :param params: Query parameters passed to API. 
            :param keep: Keep filters for next API call. Defaults to False.
        """
        self._sg.config.validate()

        params.update(self._filters)
        if not keep:
            self._filters = {}

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
                    config.oauth_consumer_key, config.oauth_consumer_secret,
                    config.oauth_token, config.oauth_token_secret
                ).get_session()

            response = self._session.get(tail, params)

        response.raise_for_status()

        if not config.response_type:
            return response.json()
        else:
            return response.text


class SurveyGizmo(object):
    def __init__(self, **kwargs):
        self.config = _Config(self, **kwargs)
        self.api = _API(self)
        self.api._check_version()
