
from surveygizmo.api import base


class SurveyResponse(base.Resource):
    resource_fmt_str = 'survey/%(survey_id)s/surveyresponse/%(response_id)s'
    resource_id_keys = ['survey_id', 'response_id']

    def list(self, survey_id, **kwargs):
        kwargs.update({'survey_id': survey_id, })
        return super(SurveyResponse, self).list(**kwargs)

    def get(self, survey_id, response_id, **kwargs):
        kwargs.update({
            'survey_id': survey_id,
            'response_id': response_id,
        })
        return super(SurveyResponse, self).get(**kwargs)

    def create(self, survey_id, **kwargs):
        kwargs.update({'survey_id': survey_id, })
        return super(SurveyResponse, self).create(**kwargs)

    def update(self, survey_id, response_id, **kwargs):
        kwargs.update({
            'survey_id': survey_id,
            'response_id': response_id,
        })
        return super(SurveyResponse, self).update(**kwargs)

    def copy(self, **kwargs):
        raise NotImplementedError()

    def delete(self, survey_id, response_id, **kwargs):
        kwargs.update({
            'survey_id': survey_id,
            'response_id': response_id,
        })
        return super(SurveyResponse, self).delete(**kwargs)
