

def list(*args, **kwargs):
    """ Get list of all surveys.

        Optional params:
        - page:             page number
        - resultsperpage:   number of results per page
    """
    return "survey/", {}


def get(survey_id, *args, **kwargs):
    """ Get survey by id.

        Required params:
        - survey_id:    survey ID

        Optional params:
        - metaonly:     exclude page info
    """
    tail = "survey/%s" % survey_id
    params = {

    }
    params.update(kwargs)
    return tail, params


def create(title, survey_type, *args, **kwargs):
    """ Create new survey object.

        Required params:
        - title         survey title
        - survey_type   select from [survey, form, poll, quiz]

        Optional params:
        - status:                   select from [launched, closed, deleted]
        - theme:                    theme ID
        - team:                     team ID
        - options[internal_title]:  internal title
        - blockby:                  select from [NONE, IP, COOKIE]
    """
    tail = "survey/"
    params = {
        '_method': 'PUT',
        'title': title,
        'type': survey_type,
    }
    params.update(kwargs)
    return tail, params


def update(survey_id, *args, **kwargs):
    """ Update existing survey object.

        Required params:
        - survey_id: survey ID

        Optional params:
        - title:                    survey title
        - status:                   select from [launched, closed, deleted]
        - theme:                    theme ID
        - team:                     team ID
        - options[internal_title]:  internal title
        - blockby:                  select from [NONE, IP, COOKIE]
    """
    tail = "survey/%s" % survey_id
    params = {
        '_method': 'POST',
    }
    params.update(kwargs)
    return tail, params


def copy(survey_id, title, *args, **kwargs):
    """ Copy new survey object from existing survey.

        Required params:
        - survey_id:    survey ID
        - title:        survey title

        Optional params:
        - status:                   select from [launched, closed, deleted]
        - theme:                    theme ID
        - team:                     team ID
        - options[internal_title]:  internal title
        - blockby:                  select from [NONE, IP, COOKIE]
    """
    tail = "survey/%s" % survey_id
    params = {
        '_method': 'POST',
        'title': title,
        'copy': 'true',
    }
    params.update(kwargs)
    return tail, params


def delete(survey_id, *args, **kwargs):
    """ Delete survey object.

        Required params:
        - survey_id: survey ID
    """
    tail = "survey/%s" % survey_id
    params = {
        '_method': 'DELETE',
    }
    params.update(kwargs)
    return tail, params
