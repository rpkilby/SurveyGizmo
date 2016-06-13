
from unittest import TestCase
from surveygizmo import SurveyGizmo
from surveygizmo import api

client = SurveyGizmo(api_token='token', api_token_secret='secret', prepare_url=True)
client.api.base_url = ''


class APIMetaTests(TestCase):
    def test_resource_properties(self):
        # ensure that we can inspect the API to look at the available resources
        self.assertIn('surveycampaign', dir(client.api))

        # ensure that properties are returning correct types
        self.assertIsInstance(client.api.account, api.account.Account)
        self.assertIsInstance(client.api.accountteams, api.accountteams.AccountTeams)
        self.assertIsInstance(client.api.accountuser, api.accountuser.AccountUser)
        self.assertIsInstance(client.api.contact, api.contact.Contact)
        self.assertIsInstance(client.api.contactlist, api.contactlist.ContactList)
        self.assertIsInstance(client.api.emailmessage, api.emailmessage.EmailMessage)
        self.assertIsInstance(client.api.survey, api.survey.Survey)
        self.assertIsInstance(client.api.surveycampaign, api.surveycampaign.SurveyCampaign)
        self.assertIsInstance(client.api.surveyoption, api.surveyoption.SurveyOption)
        self.assertIsInstance(client.api.surveypage, api.surveypage.SurveyPage)
        self.assertIsInstance(client.api.surveyquestion, api.surveyquestion.SurveyQuestion)
        self.assertIsInstance(client.api.surveyreport, api.surveyreport.SurveyReport)
        self.assertIsInstance(client.api.surveyresponse, api.surveyresponse.SurveyResponse)
        self.assertIsInstance(client.api.surveystatistic, api.surveystatistic.SurveyStatistic)

    def test_new_resource_on_access(self):
        # new invocations should return new Resources. This is necessary
        # so that filtering is not global.
        self.assertIsNot(client.api.survey, client.api.survey)


class APITests(TestCase):
    def test_prepare_url_config(self):
        self.assertTrue(client.config.prepare_url)

        _, params = client.api.survey.list()
        self.assertNotIn('_prepare_url', params)

    def test_prepare_url_override(self):
        client = SurveyGizmo(api_token='token', api_token_secret='secret', prepare_url=False)
        client.api.base_url = ''

        _, params = client.api.survey.list(_prepare_url=True)
        self.assertNotIn('_prepare_url', params)
