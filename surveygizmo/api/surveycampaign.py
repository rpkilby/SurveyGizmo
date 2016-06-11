
from surveygizmo.api import base


class SurveyCampaign(base.Resource):
    resource_fmt_str = 'survey/%(survey_id)s/surveycampaign/%(campaign_id)s'
    resource_id_keys = ['survey_id', 'campaign_id']

    def list(self, survey_id, **kwargs):
        kwargs.update({'survey_id': survey_id, })
        return super(SurveyCampaign, self).list(**kwargs)

    def get(self, survey_id, campaign_id, **kwargs):
        kwargs.update({
            'survey_id': survey_id,
            'campaign_id': campaign_id,
        })
        return super(SurveyCampaign, self).get(**kwargs)

    def create(self, survey_id, name, type, **kwargs):
        kwargs.update({
            'survey_id': survey_id,
            'name': name,
            'type': type,
        })
        return super(SurveyCampaign, self).create(**kwargs)

    def update(self, survey_id, campaign_id, **kwargs):
        kwargs.update({
            'survey_id': survey_id,
            'campaign_id': campaign_id,
        })
        return super(SurveyCampaign, self).update(**kwargs)

    def copy(self, survey_id, campaign_id, **kwargs):
        kwargs.update({
            'survey_id': survey_id,
            'campaign_id': campaign_id,
        })
        return super(SurveyCampaign, self).copy(**kwargs)

    def delete(self, survey_id, campaign_id, **kwargs):
        kwargs.update({
            'survey_id': survey_id,
            'campaign_id': campaign_id,
        })
        return super(SurveyCampaign, self).delete(**kwargs)
