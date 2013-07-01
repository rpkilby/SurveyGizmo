
def list_all(*args, **kwargs):
    return "survey/", {}


def get(survey_id, *args, **kwargs):
    tail = "survey/%s" % survey_id
    params = {

    }
    params.update(kwargs)
    return tail, params


def create(*args, **kwargs):
    tail = "survey/"
    params = {
        '_method': 'PUT',
    }
    params.update(kwargs)
    return tail, params


def delete(survey_id, *args, **kwargs):
    tail = "survey/%s" % survey_id
    params = {
        '_method': 'DELETE',
    }
    params.update(kwargs)
    return tail, params


def change(survey_id, *args, **kwargs):
    tail = "survey/%s" % survey_id
    params = {
        '_method': 'POST',
    }
    params.update(kwargs)
    return tail, params


def copy(survey_id, title, *args, **kwargs):
    tail = "survey/%s" % survey_id
    params = {
        '_method': 'POST',
        'title': str(title),
        'copy': 'true',
    }
    params.update(kwargs)
    return tail, params


def disable_vote_protection(survey_id, *args, **kwargs):
    tail = "survey/%s" % survey_id
    params = {
        '_method': 'POST',
        'blockby': 'NONE',
    }
    params.update(kwargs)
    return tail, params


def enable_ip_vote_protection(survey_id, *args, **kwargs):
    tail = "survey/%s" % survey_id
    params = {
        '_method': 'POST',
        'blockby': 'IP',
    }
    params.update(kwargs)
    return tail, params


def enable_cookie_vote_protection(survey_id, *args, **kwargs):
    tail = "survey/%s" % survey_id
    params = {
        '_method': 'POST',
        'blockby': 'COOKIE',
    }
    params.update(kwargs)
    return tail, params
