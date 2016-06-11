
class Resource(object):
    resource_fmt_str = ''
    resource_id_keys = []

    def __init__(self, api):
        self._filters = []
        self.api = api

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
                <>          Is equal to (!=)
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
        self.clear_filters()
        return self.api.call(*self.prepare(kwargs))

    def get(self, **kwargs):
        return self.api.call(*self.prepare(kwargs))

    def create(self, **kwargs):
        kwargs.update({
            '_method': 'PUT',
        })
        return self.api.call(*self.prepare(kwargs))

    def update(self, **kwargs):
        kwargs.update({
            '_method': 'POST',
        })
        return self.api.call(*self.prepare(kwargs))

    def delete(self, **kwargs):
        kwargs.update({
            '_method': 'DELETE',
        })
        return self.api.call(*self.prepare(kwargs))

    def copy(self, **kwargs):
        kwargs.update({
            '_method': 'POST',
            'copy': 'true',
        })
        return self.api.call(*self.prepare(kwargs))

    def prepare(self, kwargs):
        # format the path part of the url
        ids = {}
        for id_key in self.resource_id_keys:
            ids[id_key] = kwargs.pop(id_key, '')

        path = self.resource_fmt_str % ids

        return path, kwargs
