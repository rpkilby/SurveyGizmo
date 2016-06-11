
from surveygizmo.api import base


class Contact(base.Resource):
    resource_fmt_str = 'survey/%(survey_id)s/surveycampaign/%(campaign_id)s/contact/%(contact_id)s'
    resource_id_keys = ['survey_id', 'campaign_id', 'contact_id']

    def list(self, survey_id, campaign_id, **kwargs):
        kwargs.update({
            'survey_id': survey_id,
            'campaign_id': campaign_id,
        })
        return super(Contact, self).list(**kwargs)

    def get(self, survey_id, campaign_id, contact_id, **kwargs):
        kwargs.update({
            'survey_id': survey_id,
            'campaign_id': campaign_id,
            'contact_id': contact_id,
        })
        return super(Contact, self).get(**kwargs)

    def create(self, survey_id, campaign_id, semailaddress, **kwargs):
        kwargs.update({
            'survey_id': survey_id,
            'campaign_id': campaign_id,
            'semailaddress': semailaddress,
        })
        return super(Contact, self).create(**kwargs)

    def update(self, survey_id, campaign_id, contact_id, **kwargs):
        kwargs.update({
            'survey_id': survey_id,
            'campaign_id': campaign_id,
            'contact_id': contact_id,
        })
        return super(Contact, self).update(**kwargs)

    def copy(self, **kwargs):
        raise NotImplementedError()

    def delete(self, survey_id, campaign_id, contact_id, **kwargs):
        kwargs.update({
            'survey_id': survey_id,
            'campaign_id': campaign_id,
            'contact_id': contact_id,
        })
        return super(Contact, self).delete(**kwargs)
