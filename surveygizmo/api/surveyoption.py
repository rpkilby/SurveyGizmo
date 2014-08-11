

def list(survey_id, question_id, *args, **kwargs):
    """ Get list of all options for a surveyquestion.

        Required params:
        - survey_id:    survey ID
        - question_id:  question ID

        Optional params:
        - page:             page number
        - resultsperpage:   number of results per page
    """
    tail = "survey/%s/surveyquestion/%s/surveyoption" % (survey_id, question_id)
    params = {

    }
    params.update(kwargs)
    return tail, params


def get(survey_id, question_id, option_id, *args, **kwargs):
    """ Get surveyoption by id.

        Required params:
        - survey_id:    survey ID
        - question_id:  question ID
        - option_id:    option ID
    """
    tail = "survey/%s/surveyquestion/%s/surveyoption/%s" % (survey_id, question_id, option_id)
    params = {

    }
    params.update(kwargs)
    return tail, params


def create(survey_id, question_id, *args, **kwargs):
    """ Create new surveyoption object.

        Required params:
        - survey_id:    survey ID
        - question_id:  question ID

        Optional params:
        - title:        option title
        - value:        option value
    """
    tail = "survey/%s/surveyquestion/%s/surveyoption" % (survey_id, question_id)
    params = {
        '_method': 'PUT',
    }
    params.update(kwargs)
    return tail, params


def delete(survey_id, question_id, option_id, *args, **kwargs):
    """ Delete surveyoption object.

        Required params:
        - survey_id:    survey ID
        - question_id:  question ID
        - option_id:    option ID
    """
    tail = "survey/%s/surveyquestion/%s/surveyoption/%s" % (survey_id, question_id, option_id)
    params = {
        '_method': 'DELETE',
    }
    params.update(kwargs)
    return tail, params


def update(survey_id, question_id, option_id, *args, **kwargs):
    """ Update existing surveyoption object.

        Required params:
        - survey_id:    survey ID
        - question_id:  question ID
        - option_id:    option ID

        Optional params:
        - title:        option title
        - value:        option value
    """
    tail = "survey/%s/surveyquestion/%s/surveyoption/%s" % (survey_id, question_id, option_id)
    params = {
        '_method': 'POST',
    }
    params.update(kwargs)
    return tail, params
