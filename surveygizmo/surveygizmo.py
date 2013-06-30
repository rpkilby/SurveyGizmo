
import oauth_helper
import requests
import hashlib

"https://restapi.surveygizmo.com/v1/survey/{$survey}/surveyresponse?user:pass={$user}:{$pass}{$status}{$datesubmmitted}"


class ImproperlyConfigured(Exception):
    """ SurveyGizmo is somehow improperly configured."""
    pass


class _Config(object):
    def __init__(self, **kwargs):
        self.api_version = kwargs.get('api_version')
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
            raise ImproperlyConfigured()

        if not self.auth_method in ['user:pass', 'user:md5', 'oauth']:
            raise ImproperlyConfigured()
        else:
            if self.auth_method == "user:pass":
                if not self.username or not self.password:
                    raise ImproperlyConfigured()
            elif self.auth_method == "user:md5":
                if not self.username:
                    raise ImproperlyConfigured()
                elif not self.password and not self.md5_hash:
                    raise ImproperlyConfigured()
            elif self.auth_method == "oauth":
                if not self.oauth_consumer_key or not self.oauth_consumer_secret or \
                   not self.oauth_token or not self.oauth_token_secret:
                    raise ImproperlyConfigured()

        if not self.response_type in ["json", "pson", "xml", "debug", None]:
            raise ImproperlyConfigured()


class _API(object):
    def __init__(self, _sg):
        self._sg = _sg
        self._api_version = None
        self._api = None
        self._filters = {}
        self._session = None
        self.base_url = "https://restapi.surveygizmo.com/"

    def __getattr__(self, name):
        """ Validate configuration, get api, get method.
        """
        self._sg.config.validate()

        if self._api_version != self._sg.config.api_version:
            self._api_version = self._sg.config.api_version
            self._api = importlib.import_module(".%s" % self._sg.config.api_version, 'surveygizmo.api')

        if hasattr(self.other, name):
            func = getattr(self._api, name)
            # return lambda *args, **kwargs: self._wrap(func, args, kwargs)
            return self._wrap(func)
        raise AttributeError(name)

    # def _wrap(self, func, args, kwargs):
    #     result = func(self._sg, *args, **kwargs)
    #     return self.execute(*result)

    def _wrap(self, func):
        def wrapper(*args, **kwargs):
            # print "Arguments were: %s, %s" % (args, kwargs)
            # self._tail, self._params = func(*args, **kwargs)
            tail, params = func(*args, **kwargs)

            return_type = self._sg.config.return_type
            if return_type:
                tail = "%s.%s" % (tail, return_type)
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
        params.update(self._filters)
        if not keep:
            self._filters = {}

        config = self._sg.config
        if config.auth_method == 'user:pass':
            params.update({
                config.auth_method: "%s:%s" % (config.username, config.password),
            })
            url = "%s%s" % (self.base_url, tail)
            response = requests.get(url, params)

        elif config.auth_method == 'user:md5':
            if not config.md5_hash:
                config.md5_hash = hashlib.md5(config.password).hexdigest()
            params.update({
                config.auth_method: "%s:%s" % (config.username, config.md5_hash),
            })
            url = "%s%s" % (self.base_url, tail)
            response = requests.get(url, params)

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
    def __init__(self, api_version="head", **kwargs):
        self.config = _Config(api_version, **kwargs)
        self.api = _API(self)
