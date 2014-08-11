

def list(survey_id, *args, **kwargs):
    """ Get list of all pages for a survey.

        Optional params:
        - page:             page number
        - resultsperpage:   number of results per page
    """
    tail = "survey/%s/surveypage" % survey_id
    params = {

    }
    params.update(kwargs)
    return tail, params


def get(survey_id, page_id, *args, **kwargs):
    """ Get surveypage by id.

        Required params:
        - survey_id:    survey ID
        - page_id:      page ID
    """
    tail = "survey/%s/surveypage/%s" % (survey_id, page_id)
    params = {

    }
    params.update(kwargs)
    return tail, params


def create(survey_id, *args, **kwargs):
    """ Create new surveypage object.

        Required params:
        - survey_id:    survey ID

        Optional params:
        - after:        which page to add after
        - title:        page title
        - description:  page description
        - properties
    """
    tail = "survey/%s/surveypage" % survey_id
    params = {
        '_method': 'PUT',
    }
    params.update(kwargs)
    return tail, params


def delete(survey_id, page_id, *args, **kwargs):
    """ Delete surveypage object.

        Required params:
        - survey_id:    survey ID
        - page_id:      page ID
    """
    tail = "survey/%s/surveypage/%s" % (survey_id, page_id)
    params = {
        '_method': 'DELETE',
    }
    params.update(kwargs)
    return tail, params


def update(survey_id, page_id, *args, **kwargs):
    """ Update existing surveypage object.

        Required params:
        - survey_id:    survey ID
        - page_id:      page ID

        Optional params:
        - title:        page title
        - description:  page description
        - properties
    """
    tail = "survey/%s/surveypage/%s" % (survey_id, page_id)
    params = {
        '_method': 'POST',
    }
    params.update(kwargs)
    return tail, params
