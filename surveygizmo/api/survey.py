
from surveygizmo.api import base


class Survey(base.Resource):
    resource_sub_str = 'survey/%(survey_id)s'
    resource_id_keys = ['survey_id']
    copyable = True

    def list(self, **kwargs):
        """ Get list of all surveys.

            Optional params:
            - page:             page number
            - resultsperpage:   number of results per page
        """
        return super(Survey, self).list(**kwargs)

    def get(self, survey_id, **kwargs):
        """ Get survey by id.

            Required params:
            - survey_id:    survey ID

            Optional params:
            - metaonly:     exclude page info
        """
        kwargs.update({
            'survey_id': survey_id,
        })
        return super(Survey, self).get(**kwargs)

    def create(self, title, survey_type, **kwargs):
        """ Create new survey object.

            Required params:
            - title         survey title
            - survey_type   select from [survey, form, poll, quiz]

            Optional params:
            - status:                   select from [launched, closed, deleted]
            - theme:                    theme ID
            - team:                     team ID
            - options[internal_title]:  internal title
            - blockby:                  select from [NONE, IP, COOKIE]
        """
        kwargs.update({
            'title': title,
            'type': survey_type,
        })
        return super(Survey, self).create(**kwargs)

    def update(self, survey_id, **kwargs):
        """ Update existing survey object.

            Required params:
            - survey_id: survey ID

            Optional params:
            - title:                    survey title
            - status:                   select from [launched, closed, deleted]
            - theme:                    theme ID
            - team:                     team ID
            - options[internal_title]:  internal title
            - blockby:                  select from [NONE, IP, COOKIE]
        """
        kwargs.update({
            'survey_id': survey_id,
        })
        return super(Survey, self).update(**kwargs)

    def copy(self, survey_id, title, **kwargs):
        """ Copy new survey object from existing survey.

            Required params:
            - survey_id:    survey ID
            - title:        survey title

            Optional params:
            - status:                   select from [launched, closed, deleted]
            - theme:                    theme ID
            - team:                     team ID
            - options[internal_title]:  internal title
            - blockby:                  select from [NONE, IP, COOKIE]
        """
        kwargs.update({
            'survey_id': survey_id,
            'title': title,
        })
        return super(Survey, self).copy(**kwargs)

    def delete(self, survey_id, **kwargs):
        """ Delete survey object.

            Required params:
            - survey_id: survey ID
        """
        kwargs.update({
            'survey_id': survey_id,
        })
        return super(Survey, self).delete(**kwargs)
