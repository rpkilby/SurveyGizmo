
from surveygizmo.api import base


class EmailMessage(base.Resource):
    resource_fmt_str = 'survey/%(survey_id)s/surveycampaign/%(campaign_id)s/emailmessage/%(message_id)s'
    resource_id_keys = ['survey_id', 'campaign_id', 'message_id']

    def list(self, survey_id, campaign_id, **kwargs):
        kwargs.update({
            'survey_id': survey_id,
            'campaign_id': campaign_id,
        })
        return super(EmailMessage, self).list(**kwargs)

    def get(self, survey_id, campaign_id, message_id, **kwargs):
        kwargs.update({
            'survey_id': survey_id,
            'campaign_id': campaign_id,
            'message_id': message_id,
        })
        return super(EmailMessage, self).get(**kwargs)

    def create(self, survey_id, campaign_id, **kwargs):
        kwargs.update({
            'survey_id': survey_id,
            'campaign_id': campaign_id,
        })
        return super(EmailMessage, self).create(**kwargs)

    def update(self, survey_id, campaign_id, message_id, **kwargs):
        kwargs.update({
            'survey_id': survey_id,
            'campaign_id': campaign_id,
            'message_id': message_id,
        })
        return super(EmailMessage, self).update(**kwargs)

    def copy(self, **kwargs):
        raise NotImplementedError()

    def delete(self, survey_id, campaign_id, message_id, **kwargs):
        kwargs.update({
            'survey_id': survey_id,
            'campaign_id': campaign_id,
            'message_id': message_id,
        })
        return super(EmailMessage, self).delete(**kwargs)
