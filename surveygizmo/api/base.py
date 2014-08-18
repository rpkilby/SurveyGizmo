
import hashlib

import requests
from surveygizmo import oauth_helper


class Resource(object):
    base_url = ''
    copyable = False
    resource_sub_str = ''
    resource_id_keys = []

    def __init__(self, api):
        self._api = api
        self._config = api._config
        self._filters = []
        self.base_url = api.base_url

        if not self.copyable:
            del self.copy

    def filter(self, field, operator, value):
        """ Add a query filter to be applied to the next API list call for this resource.
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


            Known Operators:
                =           Is equal to (==)
                <>          Is no eqal to (!=)
                IS NULL     Value is not answered or is blank
                IS NOT NULL Value is answered or is not blank
                in          Value is in comma separated list

            Unknown Operators:
                Not officially mentioned in documentation, but may work.
                ==
                !=
                >=
                <=
                >
                <
        """
        i = len(self._filters)
        self._filters.append({
            'filter[field][%d]' % i: str(field),
            'filter[operator][%d]' % i: str(operator),
            'filter[value][%d]' % i: str(value),
        })
        return self

    def clear_filters(self):
        """ Clear API filters added through `filter`.
        """
        self._filters = []

    @property
    def filters(self):
        params = {}
        for _filter in self._filters:
            params.update(_filter)

        return params

    def list(self, **kwargs):
        kwargs.update(self.filters)
        if not self._config.preserve_filters:
            self.clear_filters()
        return self._api_call(**kwargs)

    def get(self, **kwargs):
        return self._api_call(**kwargs)

    def create(self, **kwargs):
        kwargs.update({
            '_method': 'PUT',
        })
        return self._api_call(**kwargs)

    def update(self, **kwargs):
        kwargs.update({
            '_method': 'POST',
        })
        return self._api_call(**kwargs)

    def delete(self, **kwargs):
        kwargs.update({
            '_method': 'DELETE',
        })
        return self._api_call(**kwargs)

    def copy(self, **kwargs):
        kwargs.update({
            '_method': 'POST',
            'copy': 'true',
        })
        return self._api_call(**kwargs)

    def _api_call(self, **kwargs):
        self._config.validate()
        url = self._prepare_url(kwargs)
        params = self._prepare_params(kwargs)

        if self._config.prepare_url:
            return url, params
        return self.execute(url, params)

    def _prepare_url(self, kwargs):
        # create/format the path of the url
        ids = {}
        for id_key in self.resource_id_keys:
            ids[id_key] = kwargs.pop(id_key, '')

        path = self.resource_sub_str % ids

        # API version and response format
        if self._config.response_type:
            path = "%s.%s" % (path, self._config.response_type)
        path = "%s/%s" % (self._config.api_version, path)

        # full url
        return "%s%s" % (self.base_url, path)

    def _prepare_params(self, kwargs):
        config = self._config

        if config.auth_method == 'user:pass':
            kwargs.update({
                config.auth_method: "%s:%s" % (config.username, config.password),
            })

        elif config.auth_method == 'user:md5':
            if not config.md5_hash:
                config.md5_hash = hashlib.md5(config.password).hexdigest()
            kwargs.update({
                config.auth_method: "%s:%s" % (config.username, config.md5_hash),
            })

        return kwargs

    def execute(self, url, params):
        """ Executes a call to the API.
            :param url: The full url for the api call.
            :param params: Query parameters encoded in the request.
        """
        config = self._config

        if config.auth_method == 'oauth':
            if not self._api._session:
                self._api._session = oauth_helper.SGAuthService(
                    config.consumer_key, config.consumer_secret,
                    config.access_token, config.access_token_secret,
                ).get_session()

            response = self._api._session.get(url, params=params, **config.requests_kwargs)
        else:
            response = requests.get(url, params=params, **config.requests_kwargs)

        if 520 <= response.status_code < 530:
            if config.handler52x:
                return config.handler52x(response, self, url, params)

        response.raise_for_status()

        if not config.response_type:
            return response.json()
        else:
            return response.text
