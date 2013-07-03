

def list(survey_id, *args, **kwargs):
    tail = "survey/%s/surveyresponse" % survey_id
    params = {

    }.update(kwargs)
    return tail, params


def get(survey_id, response_id, *args, **kwargs):
    tail = "survey/%s/surveyresponse/%s" % (survey_id, response_id)
    params = {

    }.update(kwargs)
    return tail, params


def create(*args, **kwargs):
    tail = "survey/"
    params = {
        '_method': 'PUT',
    }.update(kwargs)
    return tail, params


def delete(survey_id, response_id, *args, **kwargs):
    tail = "survey/%s/surveyresponse/%s" % (survey_id, response_id)
    params = {
        '_method': 'DELETE',
    }.update(kwargs)
    return tail, params


def change(survey_id, response_id, *args, **kwargs):
    tail = "survey/%s/surveyresponse/%s" % (survey_id, response_id)
    params = {
        '_method': 'POST',
    }.update(kwargs)
    return tail, params
