
from __future__ import absolute_import

import time
import requests
from .api import base
from .compat import with_metaclass


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
        self.base_url = kwargs.get('base_url', 'https://restapi.surveygizmo.com/')
        self.api_version = kwargs.get('api_version', 'head')
        self.api_token = kwargs.get('api_token', None)
        self.api_token_secret = kwargs.get('api_token_secret', None)

        self.response_type = kwargs.get('response_type', None)
        self.requests_kwargs = kwargs.get('requests_kwargs', {})
        self.prepare_url = kwargs.get('prepare_url', False)
        self.handler52x = kwargs.get('handler52x', None)

    def validate(self):
        """
        Perform validation check on properties.
        """
        if not self.api_token or not self.api_token_secret:
            raise ImproperlyConfigured("'api_token' and 'api_token_secret' are required for authentication.")

        if self.response_type not in ["json", "pson", "xml", "debug", None]:
            raise ImproperlyConfigured("'%s' is an invalid response_type" % self.response_type)


class APIMeta(type):
    def __init__(cls, name, bases, attrs):
        super(APIMeta, cls).__init__(name, bases, attrs)

        resources = __import__('api', globals(), locals(), [], 1)

        for resource_name in resources.__all__:
            resource = getattr(resources, resource_name)
            if issubclass(resource, base.Resource):

                setattr(cls, resource_name.lower(), cls.prop(resource))

    def prop(self, resource):
        """
        Generate properties for accessing resources.
        """
        @property
        def wrapped(self):
            return resource(self)

        return wrapped


class API(with_metaclass(APIMeta, object)):
    def __init__(self, config):
        self.config = config

    def call(self, path, params):
        self.config.validate()
        url = self._prepare_url(path)
        params = self._prepare_params(params)

        if params.pop('_prepare_url', self.config.prepare_url):
            return url, params
        return self.execute(url, params)

    def _prepare_url(self, path):

        # API version and response format
        if self.config.response_type:
            path = "%s.%s" % (path, self.config.response_type)
        path = "%s/%s" % (self.config.api_version, path)

        # full url
        return "%s%s" % (self.config.base_url, path)

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
