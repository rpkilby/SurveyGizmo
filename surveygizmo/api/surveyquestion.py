

def list(survey_id, *args, **kwargs):
    """ Get list of all questions for a survey.

        Required params:
        - survey_id:    survey ID

        Optional params:
        - page:             page number
        - resultsperpage:   number of results per page
    """
    tail = "survey/%s/surveyquestion" % survey_id
    params = {

    }
    params.update(kwargs)
    return tail, params


def get(survey_id, question_id, *args, **kwargs):
    """ Get surveyquestion by id.

        Required params:
        - survey_id:    survey ID
        - question_id:  question ID
    """
    tail = "survey/%s/surveyquestion/%s" % (survey_id, question_id)
    params = {

    }
    params.update(kwargs)
    return tail, params


def create(survey_id, question_type, *args, **kwargs):
    """ Create new surveyquestion object.

        Required params:
        - survey_id:        survey ID
        - question_type:    select from [radio, text, email, checkbox, essay,
                                contsum, rank-dragdrop, multitext, hidden,
                                instructions, urlredirect, media, email, file,
                                single-image, multi-image]

        Optional params:
        - after:        which question to add after
        - title:        question title
        - description:  question description
        - properties
    """
    tail = "survey/%s/surveyquestion" % survey_id
    params = {
        '_method': 'PUT',
    }
    params.update(kwargs)
    return tail, params


def delete(survey_id, question_id, *args, **kwargs):
    """ Delete surveyquestion object.

        Required params:
        - survey_id: survey ID
        - question_id:  question ID
    """
    tail = "survey/%s/surveyquestion/%s" % (survey_id, question_id)
    params = {
        '_method': 'DELETE',
    }
    params.update(kwargs)
    return tail, params


def update(survey_id, question_id, *args, **kwargs):
    """ Update existing surveyquestion object.

        Required params:
        - survey_id:    survey ID
        - question_id:  question ID

        Optional params:
        - title:        question title
        - description:  question description
        - properties
    """
    tail = "survey/%s/surveyquestion/%s" % (survey_id, question_id)
    params = {
        '_method': 'POST',
    }
    params.update(kwargs)
    return tail, params
