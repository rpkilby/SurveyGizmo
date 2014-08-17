
def list(survey_id, campaign_id, *args, **kwargs):
    """ Get list of all contacts for a survey campaign.

        Optional params:
        - page:             page number
        - resultsperpage:   number of results per page
    """
    tail = "survey/%s/surveycampaign/%s/contact" % (survey_id, campaign_id)
    params = {

    }
    params.update(kwargs)
    return tail, params


def get(survey_id, campaign_id, contact_id, *args, **kwargs):
    """ Get contact by id.

        Required params:
        - survey_id:    survey ID
        - campaign_id:  campaign ID
        - contact_id:   contact ID
    """
    tail = "survey/%s/surveycampaign/%s/contact/%s" % (survey_id, campaign_id, contact_id)
    params = {

    }
    params.update(kwargs)
    return tail, params


def create(survey_id, campaign_id, *args, **kwargs):
    """ Create new contact object.

        Required params:
        - survey_id:    survey ID
        - campaign_id:  campaign ID

        Optional params:
        - data:         refer to official documentation
    """
    tail = "survey/%s/surveycampaign/%s/contact" % (survey_id, campaign_id)
    params = {
        '_method': 'PUT',
    }
    params.update(kwargs)
    return tail, params


def delete(survey_id, campaign_id, contact_id, *args, **kwargs):
    """ Delete contact object.

        Required params:
        - survey_id:    survey ID
        - campaign_id:  campaign ID
        - contact_id:   contact ID
    """
    tail = "survey/%s/surveycampaign/%s/contact/%s" % (survey_id, campaign_id, contact_id)
    params = {
        '_method': 'DELETE',
    }
    params.update(kwargs)
    return tail, params


def change(survey_id, campaign_id, contact_id, *args, **kwargs):
    """ Change existing contact object.

        Required params:
        - survey_id:    survey ID
        - campaign_id:  campaign ID
        - contact_id:   contact ID

        Optional params:
        - data:         refer to official documentation
    """
    tail = "survey/%s/surveycampaign/%s/contact/%s" % (survey_id, campaign_id, contact_id)
    params = {
        '_method': 'POST',
    }
    params.update(kwargs)
    return tail, params
