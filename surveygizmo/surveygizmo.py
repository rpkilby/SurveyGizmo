

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
        if not self.api_version in ['v1', 'v2', 'v3', 'head']:
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
                if not self.oauth_consumer_key or not self.oauth_consumer_secret:
                    raise ImproperlyConfigured()

        if not self.response_type in ["json", "pson", "xml", "debug", None]:
            raise ImproperlyConfigured()


class _API(object):
    def __init__(self, _sg):
        self._sg = _sg
        self._api_version = None
        self._api = None

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
            result = func(*args, **kwargs)
            return self.execute(*result)
        return wrapper

    def filter(self, params):
        """
        """
        pass

    def execute(self, tail, params):
        """
        """
        pass


class SurveyGizmo(object):
    def __init__(self, api_version="head", **kwargs):
        self.config = _Config(api_version, **kwargs)
        self.api = _API(self)
