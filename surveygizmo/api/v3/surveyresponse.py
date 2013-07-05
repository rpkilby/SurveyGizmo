

def list(survey_id, *args, **kwargs):
    """ Get list of all responses for a survey.

        Optional params:
        - page:             page number
        - resultsperpage:   number of results per page
    """
    tail = "survey/%s/surveyresponse" % survey_id
    params = {

    }.update(kwargs)
    return tail, params


def get(survey_id, response_id, *args, **kwargs):
    """ Get surveyresponse by id.

        Required params:
        - survey_id:    survey ID
        - response_id:  response ID
    """
    tail = "survey/%s/surveyresponse/%s" % (survey_id, response_id)
    params = {

    }.update(kwargs)
    return tail, params


def create(survey_id, *args, **kwargs):
    """ Create new surveyresponse object.

        Required params:
        - survey_id:    survey ID

        Optional params:
        - data:         refer to official documentation
    """
    tail = "survey/%s/surveyresponse" % survey_id
    params = {
        '_method': 'PUT',
    }.update(kwargs)
    return tail, params


def delete(survey_id, response_id, *args, **kwargs):
    """ Delete surveyresponse object.

        Required params:
        - survey_id: survey ID
        - response_id:  response ID
    """
    tail = "survey/%s/surveyresponse/%s" % (survey_id, response_id)
    params = {
        '_method': 'DELETE',
    }.update(kwargs)
    return tail, params


def change(survey_id, response_id, *args, **kwargs):
    """ Change existing surveyresponse object.

        Required params:
        - survey_id:    survey ID
        - response_id:  response ID

        Optional params:
        - data:         refer to official documentation
    """
    tail = "survey/%s/surveyresponse/%s" % (survey_id, response_id)
    params = {
        '_method': 'POST',
    }.update(kwargs)
    return tail, params
