
import time
import requests
from api import base


class ImproperlyConfigured(Exception):
    """
    SurveyGizmo is somehow improperly configured.
    """
    pass


def default_52xhandler(response, resource, url, params):
    """
    Default 52x handler that loops every second until a non 52x response is received.
    :param response: The response of the last executed api request.
    :param resource: The resource of the last executed api request.
    :param url: The url of the last executed api request sans encoded query parameters.
    :param params: The query params of the last executed api request in dictionary format.
    """
    time.sleep(1)
    return resource.execute(url, params)


class Config(object):
    def __init__(self, **kwargs):
        self.api_version = kwargs.get('api_version', 'head')
        self.auth_method = kwargs.get('auth_method', None)
        self.username = kwargs.get('username', None)
        self.password = kwargs.get('password', None)
        self.md5_hash = kwargs.get('md5_hash', None)
        self.consumer_key = kwargs.get('consumer_key', None)
        self.consumer_secret = kwargs.get('consumer_secret', None)
        self.access_token = kwargs.get('access_token', None)
        self.access_token_secret = kwargs.get('access_token_secret', None)

        self.response_type = kwargs.get('response_type', None)
        self.requests_kwargs = kwargs.get('requests_kwargs', {})
        self.prepare_url = kwargs.get('prepare_url', False)
        self.preserve_filters = kwargs.get('preserve_filters', False)
        self.handler52x = kwargs.get('handler52x', None)

    def validate(self):
        """ Perform validation check on properties.
        """
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


class API(object):
    base_url = "https://restapi.surveygizmo.com/"

    def __init__(self, config):
        self.config = config

        self._resources = {}
        self._session = None

        self._import_api()

    def _import_api(self):
        """
        Instantiates API resources and adds them to the API instance. e.g., The
        `surveygizmo.api.survey.Survey` resource is callable as `sg.api.survey`.
        """
        resources = __import__('api', globals(), locals(), ['*'])

        for resource_name in resources.__all__:
            resource = getattr(resources, resource_name)

            if issubclass(resource, base.Resource):
                self._resources[resource_name.lower()] = resource(self)

    def __getattr__(self, name):
        # necessary to retrieve resources loaded from api
        if self._resources.get(name, None) is not None:
            return self._resources[name]
        raise AttributeError(name)

    def call(self, path, params):
        self.config.validate()
        url = self._prepare_url(path)
        params = self._prepare_params(params)

        if self.config.prepare_url:
            return url, params
        return self.execute(url, params)

    def _prepare_url(self, path):

        # API version and response format
        if self.config.response_type:
            path = "%s.%s" % (path, self.config.response_type)
        path = "%s/%s" % (self.config.api_version, path)

        # full url
        return "%s%s" % (self.base_url, path)

    def _prepare_params(self, params):
        params.update({
            'api_token': self.config.api_token,
            'api_token_secret': self.config.api_token_secret,
        })

        return params

    def execute(self, url, params):
        """ Executes a call to the API.
            :param url: The full url for the api call.
            :param params: Query parameters encoded in the request.
        """
        response = requests.get(url, params=params, **self.config.requests_kwargs)

        if 520 <= response.status_code < 530:
            if self.config.handler52x:
                return self.config.handler52x(response, self, url, params)

        response.raise_for_status()

        if not self.config.response_type:
            return response.json()
        else:
            return response.text


class SurveyGizmo(object):
    """
    SurveyGizmo API client.
    """
    def __init__(self, **kwargs):
        self.config = Config(**kwargs)
        self.api = API(self.config)
