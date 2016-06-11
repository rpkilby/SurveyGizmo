
from surveygizmo.api import base


class SurveyStatistic(base.Resource):
    resource_fmt_str = 'survey/%(survey_id)s/surveystatistic/%(statistic_id)s'
    resource_id_keys = ['survey_id', 'statistic_id']

    def list(self, survey_id, **kwargs):
        kwargs.update({'survey_id': survey_id, })
        return super(SurveyStatistic, self).list(**kwargs)

    def get(self, **kwargs):
        raise NotImplementedError()

    def create(self, **kwargs):
        raise NotImplementedError()

    def update(self, **kwargs):
        raise NotImplementedError()

    def copy(self, **kwargs):
        raise NotImplementedError()

    def delete(self, **kwargs):
        raise NotImplementedError()
