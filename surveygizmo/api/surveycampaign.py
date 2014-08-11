

def list(survey_id, *args, **kwargs):
    """ Get list of all campaigns for a survey.

        Required params:
        - survey_id:    survey ID

        Optional params:
        - page:             page number
        - resultsperpage:   number of results per page
    """
    tail = "survey/%s/surveycampaign" % survey_id
    params = {

    }
    params.update(kwargs)
    return tail, params


def get(survey_id, campaign_id, *args, **kwargs):
    """ Get surveycampaign by id.

        Required params:
        - survey_id:    survey ID
        - campaign_id:  campaign ID
    """
    tail = "survey/%s/surveycampaign/%s" % (survey_id, campaign_id)
    params = {

    }
    params.update(kwargs)
    return tail, params


def create(survey_id, campaign_type, campaign_name, *args, **kwargs):
    """ Create new surveycampaign object.

        Required params:
        - survey_id         survey ID
        - campaign_type     select from [link, email, html, js, blog, iframe, popup ...]
        - campaign_name     name of the campaign

        Optional params:
        - language:     language of the campaign [Auto, English...]
        - status:       select from [Active, Closed, Deleted]
        - slug:         url slug for the campaign
        - subtype:      distribution link subtype (private), Ex: &subtype=private
    """

    tail = "survey/%s/surveycampaign/" % (survey_id,)
    params = {
        '_method': 'PUT',
    }
    params.update(kwargs)
    params.update({
        "type": campaign_type,
        "name": campaign_name,
    })
    return tail, params


def update(survey_id, campaign_id, *args, **kwargs):
    """ Update existing surveycampaign object.

        Required params:
        - survey_id:    survey ID
        - campaign_id:  campaign ID

        Optional params:
        - name:         name of the campaign
        - language:     language of the campaign [Auto, English...]
        - status:       select from [Active, Closed, Deleted]
        - slug:         url slug for the campaign
    """
    tail = "survey/%s/surveycampaign/%s" % (survey_id, campaign_id)
    params = {
        '_method': 'POST',
    }
    params.update(kwargs)
    return tail, params


def copy(survey_id, campaign_id, *args, **kwargs):
    """ Copy new surveycampaign object from existing surveycampaign.

        Required params:
        - survey_id:    survey ID
        - campaign_id:  campaign ID

        Optional params:
        - id:           link ID of the campaign
        - name:         name of the campaign
    """
    tail = "survey/%s/surveycampaign/%s" % (survey_id, campaign_id)
    params = {
        '_method': 'POST',
        'copy': 'true',
    }
    params.update(kwargs)
    return tail, params


def delete(survey_id, campaign_id, *args, **kwargs):
    """ Delete surveycampaign object.

        Required params:
        - survey_id: survey ID
        - campaign_id:  campaign ID
    """
    tail = "survey/%s/surveycampaign/%s" % (survey_id, campaign_id)
    params = {
        '_method': 'DELETE',
    }
    params.update(kwargs)
    return tail, params
