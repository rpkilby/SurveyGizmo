
from surveygizmo.api import base


class SurveyReport(base.Resource):
    resource_fmt_str = 'survey/%(survey_id)s/surveyreport/%(report_id)s'
    resource_id_keys = ['survey_id', 'report_id']

    def list(self, survey_id, **kwargs):
        """ Get list of all reports for a survey.

            Required params:
            - survey_id:    survey ID

            Optional params:
            - types:            summary, profile, turf
            - page:             page number
            - resultsperpage:   number of results per page
        """
        kwargs.update({
            'survey_id': survey_id,
        })
        return super(SurveyReport, self).list(**kwargs)

    def get(self, survey_id, report_id, **kwargs):
        """ Get SurveyReport by id.

            Required params:
            - survey_id:    survey ID
            - report_id:    report ID
        """
        kwargs.update({
            'survey_id': survey_id,
            'report_id': report_id,
        })
        return super(SurveyReport, self).get(**kwargs)

    def create(self, **kwargs):
        raise NotImplementedError()

    def update(self, survey_id, report_id, **kwargs):
        """ Update existing SurveyReport object.

            Required params:
            - survey_id:    survey ID
            - report_id:    report ID

            Optional params:

            - _run*                 true
            - filter_date[after]*   5/1/2014
            - filter_date[before]*  6/1/2014

            * v4 API only
        """
        kwargs.update({
            'survey_id': survey_id,
            'report_id': report_id,
        })
        return super(SurveyReport, self).update(**kwargs)

    def copy(self, survey_id, report_id, **kwargs):
        """ Update existing SurveyReport object.

            Required params:
            - survey_id:    survey ID
            - report_id:    report ID

            Optional params:

            - _run*                 true
            - filter_date[after]*   5/1/2014
            - filter_date[before]*  6/1/2014

            * v4 API only
        """
        kwargs.update({
            'survey_id': survey_id,
            'report_id': report_id,
        })
        return super(SurveyReport, self).copy(**kwargs)

    def delete(self, survey_id, report_id, **kwargs):
        """ Delete SurveyReport object.

            Required params:
            - survey_id:    survey ID
            - report_id:    report ID
        """
        kwargs.update({
            'survey_id': survey_id,
            'report_id': report_id,
        })
        return super(SurveyReport, self).delete(**kwargs)
