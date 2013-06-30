
# Accounts
    

# Account Teams


# Account Users


# Contact List


# Surveys
def list_surveys(*args, **kwargs):
    return "survey/", {}


def get_survey(survey_id, *args, **kwargs):
    tail = "survey/%s" % survey_id
    params = {

    }
    params.update(kwargs)
    return tail, params


def create_survey(*args, **kwargs):
    tail = "survey/"
    params = {
        '_method': 'PUT',
    }
    params.update(kwargs)
    return tail, params


def delete_survey(survey_id, *args, **kwargs):
    tail = "survey/%s" % survey_id
    params = {
        '_method': 'DELETE',
    }
    params.update(kwargs)
    return tail, params


def change_survey(survey_id, *args, **kwargs):
    tail = "survey/%s" % survey_id
    params = {
        '_method': 'POST',
    }
    params.update(kwargs)
    return tail, params


def copy_survey(survey_id, title, *args, **kwargs):
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

