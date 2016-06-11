
from surveygizmo.api import base


class SurveyPage(base.Resource):
    resource_fmt_str = 'survey/%(survey_id)s/surveypage/%(page_id)s'
    resource_id_keys = ['survey_id', 'page_id']

    def list(self, survey_id, **kwargs):
        kwargs.update({'survey_id': survey_id, })
        return super(SurveyPage, self).list(**kwargs)

    def get(self, survey_id, page_id, **kwargs):
        kwargs.update({
            'survey_id': survey_id,
            'page_id': page_id,
        })
        return super(SurveyPage, self).get(**kwargs)

    def create(self, survey_id, title, **kwargs):
        kwargs.update({
            'survey_id': survey_id,
            'title': title,
        })
        return super(SurveyPage, self).create(**kwargs)

    def update(self, survey_id, page_id, **kwargs):
        kwargs.update({
            'survey_id': survey_id,
            'page_id': page_id,
        })
        return super(SurveyPage, self).update(**kwargs)

    def copy(self, **kwargs):
        raise NotImplementedError()

    def delete(self, survey_id, page_id, **kwargs):
        kwargs.update({
            'survey_id': survey_id,
            'page_id': page_id,
        })
        return super(SurveyPage, self).delete(**kwargs)
