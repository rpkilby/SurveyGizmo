

def list(survey_id, *args, **kwargs):
    """ Get list of all statistics for a survey.

        Required params:
        - survey_id:    survey ID

        Optional params:
        - surveypage:       restricts the statistics to specific page
        - page:             page number
        - resultsperpage:   number of results per page
    """
    tail = "survey/%s/surveystatistic" % survey_id
    params = {

    }
    params.update(kwargs)
    return tail, params


def get(survey_id, statistic_id, *args, **kwargs):
    """ Get surveystatistic by id.

        Note: Experimental in SG

        Required params:
        - survey_id:    survey ID
        - statistic_id:  statistic ID
    """
    tail = "survey/%s/surveystatistic/%s" % (survey_id, statistic_id)
    params = {

    }
    params.update(kwargs)
    return tail, params
