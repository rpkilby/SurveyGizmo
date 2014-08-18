
from surveygizmo.api import base


class SurveyQuestion(base.Resource):
    resource_fmt_str = 'survey/%(survey_id)s/surveyquestion/%(question_id)s'
    resource_id_keys = ['survey_id', 'question_id']

    def list(self, survey_id, **kwargs):
        kwargs.update({'survey_id': survey_id, })
        return super(SurveyQuestion, self).list(**kwargs)

    def get(self, survey_id, question_id, **kwargs):
        kwargs.update({
            'survey_id': survey_id,
            'question_id': question_id,
        })
        return super(SurveyQuestion, self).get(**kwargs)

    def create(self, survey_id, **kwargs):
        kwargs.update({'survey_id': survey_id, })
        return super(SurveyQuestion, self).create(**kwargs)

    def update(self, survey_id, question_id, **kwargs):
        kwargs.update({
            'survey_id': survey_id,
            'question_id': question_id,
        })
        return super(SurveyQuestion, self).update(**kwargs)

    def copy(self, **kwargs):
        raise NotImplementedError()

    def delete(self, survey_id, question_id, **kwargs):
        kwargs.update({
            'survey_id': survey_id,
            'question_id': question_id,
        })
        return super(SurveyQuestion, self).delete(**kwargs)
