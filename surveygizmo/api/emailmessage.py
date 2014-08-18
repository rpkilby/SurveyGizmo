
from surveygizmo.api import base


class EmailMessage(base.Resource):
    resource_fmt_str = 'survey/%(survey_id)s/surveycampaign/%(campaign_id)s/emailmessage/%(message_id)s'
    resource_id_keys = ['survey_id', 'campaign_id', 'message_id']

    def list(self, survey_id, campaign_id, **kwargs):
        """ Get list of all email messages for a survey campaign.

            Required params:
            - survey_id:    survey ID
            - campaign_id:  campaign ID

            Optional params:
            - page:             page number
            - resultsperpage:   number of results per page
        """
        kwargs.update({
            'survey_id': survey_id,
            'campaign_id': campaign_id,
        })
        return super(EmailMessage, self).list(**kwargs)

    def get(self, survey_id, campaign_id, message_id, **kwargs):
        """ Get email message by id.

            Required params:
            - survey_id:    survey ID
            - campaign_id:  campaign ID
            - message_id:   message ID
        """
        kwargs.update({
            'survey_id': survey_id,
            'campaign_id': campaign_id,
            'message_id': message_id,
        })
        return super(EmailMessage, self).get(**kwargs)

    def create(self, survey_id, campaign_id, **kwargs):
        """ Create new emailmessage object.

            Required params:
            - survey_id:    survey ID
            - campaign_id:  campaign ID

            Optional params:
            refer to official documentation
        """
        kwargs.update({
            'survey_id': survey_id,
            'campaign_id': campaign_id,
        })
        return super(EmailMessage, self).create(**kwargs)

    def update(self, survey_id, campaign_id, message_id, **kwargs):
        """ Update existing emailmessage object.

            Required params:
            - survey_id:    survey ID
            - campaign_id:  campaign ID
            - message_id:   message ID

            Optional params:
            refer to official documentation
        """
        kwargs.update({
            'survey_id': survey_id,
            'campaign_id': campaign_id,
            'message_id': message_id,
        })
        return super(EmailMessage, self).update(**kwargs)

    def copy(self, **kwargs):
        raise NotImplementedError()

    def delete(self, survey_id, campaign_id, message_id, **kwargs):
        """ Delete emailmessage object.

            Required params:
            - survey_id:    survey ID
            - campaign_id:  campaign ID
            - message_id:   message ID
        """
        kwargs.update({
            'survey_id': survey_id,
            'campaign_id': campaign_id,
            'message_id': message_id,
        })
        return super(EmailMessage, self).delete(**kwargs)
