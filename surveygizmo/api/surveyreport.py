
from surveygizmo.api import base


class SurveyReport(base.Resource):
    resource_fmt_str = 'survey/%(survey_id)s/surveyreport/%(report_id)s'
    resource_id_keys = ['survey_id', 'report_id']

    def list(self, survey_id, **kwargs):
        kwargs.update({'survey_id': survey_id, })
        return super(SurveyReport, self).list(**kwargs)

    def get(self, survey_id, report_id, **kwargs):
        kwargs.update({
            'survey_id': survey_id,
            'report_id': report_id,
        })
        return super(SurveyReport, self).get(**kwargs)

    def create(self, **kwargs):
        raise NotImplementedError()

    def update(self, survey_id, report_id, **kwargs):
        kwargs.update({
            'survey_id': survey_id,
            'report_id': report_id,

            # copy is required, even if false?
            'copy': 'false',
        })
        return super(SurveyReport, self).update(**kwargs)

    def copy(self, survey_id, report_id, **kwargs):
        kwargs.update({
            'survey_id': survey_id,
            'report_id': report_id,
        })
        return super(SurveyReport, self).copy(**kwargs)

    def delete(self, survey_id, report_id, **kwargs):
        kwargs.update({
            'survey_id': survey_id,
            'report_id': report_id,
        })
        return super(SurveyReport, self).delete(**kwargs)
