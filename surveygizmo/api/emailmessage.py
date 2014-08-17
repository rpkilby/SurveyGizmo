
def list(survey_id, campaign_id, *args, **kwargs):
    """ Get list of all email messages for a survey campaign.

        Optional params:
        - page:             page number
        - resultsperpage:   number of results per page
    """
    tail = "survey/%s/surveycampaign/%s/emailmessage" % (survey_id, campaign_id)
    params = {

    }
    params.update(kwargs)
    return tail, params


def get(survey_id, campaign_id, message_id, *args, **kwargs):
    """ Get email message by id.

        Required params:
        - survey_id:    survey ID
        - campaign_id:  campaign ID
        - message_id:   message ID
    """
    tail = "survey/%s/surveycampaign/%s/emailmessage/%s" % (survey_id, campaign_id, message_id)
    params = {

    }
    params.update(kwargs)
    return tail, params


def create(survey_id, campaign_id, *args, **kwargs):
    """ Create new emailmessage object.

        Required params:
        - survey_id:    survey ID
        - campaign_id:  campaign ID

        Optional params:
        - data:         refer to official documentation
    """
    tail = "survey/%s/surveycampaign/%s/emailmessage" % (survey_id, campaign_id)
    params = {
        '_method': 'PUT',
    }
    params.update(kwargs)
    return tail, params


def delete(survey_id, campaign_id, message_id, *args, **kwargs):
    """ Delete emailmessage object.

        Required params:
        - survey_id:    survey ID
        - campaign_id:  campaign ID
        - message_id:   message ID
    """
    tail = "survey/%s/surveycampaign/%s/emailmessage/%s" % (survey_id, campaign_id, message_id)
    params = {
        '_method': 'DELETE',
    }
    params.update(kwargs)
    return tail, params


def change(survey_id, campaign_id, message_id, *args, **kwargs):
    """ Change existing emailmessage object.

        Required params:
        - survey_id:    survey ID
        - campaign_id:  campaign ID
        - message_id:   message ID

        Optional params:
        - data:         refer to official documentation
    """
    tail = "survey/%s/surveycampaign/%s/emailmessage/%s" % (survey_id, campaign_id, message_id)
    params = {
        '_method': 'POST',
    }
    params.update(kwargs)
    return tail, params
