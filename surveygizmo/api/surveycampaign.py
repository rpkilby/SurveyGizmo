
from surveygizmo.api import base


class SurveyCampaign(base.Resource):
    resource_fmt_str = 'survey/%(survey_id)s/surveycampaign/%(campaign_id)s'
    resource_id_keys = ['survey_id', 'campaign_id']

    def list(self, survey_id, **kwargs):
        """ Get list of all campaigns for a survey.

            Required params:
            - survey_id:    survey ID

            Optional params:
            - page:             page number
            - resultsperpage:   number of results per page
        """
        kwargs.update({
            'survey_id': survey_id,
        })
        return super(SurveyCampaign, self).list(**kwargs)

    def get(self, survey_id, campaign_id, **kwargs):
        """ Get surveycampaign by id.

            Required params:
            - survey_id:    survey ID
            - campaign_id:  campaign ID
        """
        kwargs.update({
            'survey_id': survey_id,
            'campaign_id': campaign_id,
        })
        return super(SurveyCampaign, self).get(**kwargs)

    def create(self, survey_id, campaign_type, campaign_name, **kwargs):
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
        kwargs.update({
            'survey_id': 'survey_id',
            "type": campaign_type,
            "name": campaign_name,
        })
        return super(SurveyCampaign, self).create(**kwargs)

    def update(self, survey_id, campaign_id, **kwargs):
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
        kwargs.update({
            'survey_id': survey_id,
            'campaign_id': campaign_id,
        })
        return super(SurveyCampaign, self).update(**kwargs)

    def copy(self, survey_id, campaign_id, **kwargs):
        """ Copy new surveycampaign object from existing surveycampaign.

            Required params:
            - survey_id:    survey ID
            - campaign_id:  campaign ID

            Optional params:
            - id:           link ID of the campaign
            - name:         name of the campaign
        """
        kwargs.update({
            'survey_id': survey_id,
            'campaign_id': campaign_id,
        })
        return super(SurveyCampaign, self).copy(**kwargs)

    def delete(self, survey_id, campaign_id, **kwargs):
        """ Delete surveycampaign object.

            Required params:
            - survey_id:    survey ID
            - campaign_id:  campaign ID
        """
        kwargs.update({
            'survey_id': survey_id,
            'campaign_id': campaign_id,
        })
        return super(SurveyCampaign, self).delete(**kwargs)
