
from unittest import TestCase
from surveygizmo import SurveyGizmo

client = SurveyGizmo(api_token='token', api_token_secret='secret', prepare_url=True)
client.api.base_url = ''


class ResourceTests(TestCase):
    def test_authentication(self):
        path, params = client.api.survey.get(1)
        self.assertEqual(params['api_token'], 'token')
        self.assertEqual(params['api_token_secret'], 'secret')

    def test_methods(self):
        path, params = client.api.survey.list()
        self.assertNotIn('_method', params)

        path, params = client.api.survey.get(1)
        self.assertNotIn('_method', params)

        path, params = client.api.survey.create()
        self.assertEqual(params['_method'], 'PUT')

        path, params = client.api.survey.update(1)
        self.assertEqual(params['_method'], 'POST')

        path, params = client.api.survey.copy(1)
        self.assertEqual(params['_method'], 'POST')

        path, params = client.api.survey.delete(1)
        self.assertEqual(params['_method'], 'DELETE')


class AccountTests(TestCase):
    resource = client.api.account

    def test_list(self):
        with self.assertRaises(NotImplementedError):
            self.resource.list()

    def test_get(self):
        path, params = self.resource.get()
        self.assertEqual(path, 'head/account/')

    def test_create(self):
        with self.assertRaises(NotImplementedError):
            self.resource.create()

    def test_update(self):
        with self.assertRaises(NotImplementedError):
            self.resource.update()

    def test_copy(self):
        with self.assertRaises(NotImplementedError):
            self.resource.copy()

    def test_delete(self):
        with self.assertRaises(NotImplementedError):
            self.resource.delete()


class AccountTeamsTests(TestCase):
    resource = client.api.accountteams

    def test_list(self):
        path, params = self.resource.list()
        self.assertEqual(path, 'head/accountteams/')

    def test_get(self):
        path, params = self.resource.get(1)
        self.assertEqual(path, 'head/accountteams/1')

    def test_create(self):
        path, params = self.resource.create()
        self.assertEqual(path, 'head/accountteams/')

    def test_update(self):
        path, params = self.resource.update(1)
        self.assertEqual(path, 'head/accountteams/1')

    def test_copy(self):
        with self.assertRaises(NotImplementedError):
            self.resource.copy()

    def test_delete(self):
        path, params = self.resource.delete(1)
        self.assertEqual(path, 'head/accountteams/1')


class AccountUserTests(TestCase):
    resource = client.api.accountuser

    def test_list(self):
        path, params = self.resource.list()
        self.assertEqual(path, 'head/accountuser/')

    def test_get(self):
        path, params = self.resource.get(1)
        self.assertEqual(path, 'head/accountuser/1')

    def test_create(self):
        path, params = self.resource.create()
        self.assertEqual(path, 'head/accountuser/')

    def test_update(self):
        path, params = self.resource.update(1)
        self.assertEqual(path, 'head/accountuser/1')

    def test_copy(self):
        with self.assertRaises(NotImplementedError):
            self.resource.copy()

    def test_delete(self):
        path, params = self.resource.delete(1)
        self.assertEqual(path, 'head/accountuser/1')


class ContactTests(TestCase):
    resource = client.api.contact

    def test_list(self):
        path, params = self.resource.list(1, 1)
        self.assertEqual(path, 'head/survey/1/surveycampaign/1/contact/')

    def test_get(self):
        path, params = self.resource.get(1, 1, 1)
        self.assertEqual(path, 'head/survey/1/surveycampaign/1/contact/1')

    def test_create(self):
        path, params = self.resource.create(1, 1)
        self.assertEqual(path, 'head/survey/1/surveycampaign/1/contact/')

    def test_update(self):
        path, params = self.resource.update(1, 1, 1)
        self.assertEqual(path, 'head/survey/1/surveycampaign/1/contact/1')

    def test_copy(self):
        with self.assertRaises(NotImplementedError):
            self.resource.copy()

    def test_delete(self):
        path, params = self.resource.delete(1, 1, 1)
        self.assertEqual(path, 'head/survey/1/surveycampaign/1/contact/1')


class ContactListTests(TestCase):
    resource = client.api.contactlist

    def test_list(self):
        path, params = self.resource.list()
        self.assertEqual(path, 'head/contactlist/')

    def test_get(self):
        path, params = self.resource.get(1)
        self.assertEqual(path, 'head/contactlist/1')

    def test_create(self):
        path, params = self.resource.create()
        self.assertEqual(path, 'head/contactlist/')

    def test_update(self):
        path, params = self.resource.update(1)
        self.assertEqual(path, 'head/contactlist/1')

    def test_copy(self):
        with self.assertRaises(NotImplementedError):
            self.resource.copy()

    def test_delete(self):
        with self.assertRaises(NotImplementedError):
            self.resource.delete()


class EmailMessageTests(TestCase):
    resource = client.api.emailmessage

    def test_list(self):
        path, params = self.resource.list(1, 1)
        self.assertEqual(path, 'head/survey/1/surveycampaign/1/emailmessage/')

    def test_get(self):
        path, params = self.resource.get(1, 1, 1)
        self.assertEqual(path, 'head/survey/1/surveycampaign/1/emailmessage/1')

    def test_create(self):
        path, params = self.resource.create(1, 1)
        self.assertEqual(path, 'head/survey/1/surveycampaign/1/emailmessage/')

    def test_update(self):
        path, params = self.resource.update(1, 1, 1)
        self.assertEqual(path, 'head/survey/1/surveycampaign/1/emailmessage/1')

    def test_copy(self):
        with self.assertRaises(NotImplementedError):
            self.resource.copy()

    def test_delete(self):
        path, params = self.resource.delete(1, 1, 1)
        self.assertEqual(path, 'head/survey/1/surveycampaign/1/emailmessage/1')


class SurveyTests(TestCase):
    resource = client.api.survey

    def test_list(self):
        path, params = self.resource.list()
        self.assertEqual(path, 'head/survey/')

    def test_get(self):
        path, params = self.resource.get(1)
        self.assertEqual(path, 'head/survey/1')

    def test_create(self):
        path, params = self.resource.create()
        self.assertEqual(path, 'head/survey/')

    def test_update(self):
        path, params = self.resource.update(1)
        self.assertEqual(path, 'head/survey/1')

    def test_copy(self):
        path, params = self.resource.copy(1)
        self.assertEqual(path, 'head/survey/1')

    def test_delete(self):
        path, params = self.resource.delete(1)
        self.assertEqual(path, 'head/survey/1')


class SurveyCampaignTests(TestCase):
    resource = client.api.surveycampaign

    def test_list(self):
        path, params = self.resource.list(1)
        self.assertEqual(path, 'head/survey/1/surveycampaign/')

    def test_get(self):
        path, params = self.resource.get(1, 1)
        self.assertEqual(path, 'head/survey/1/surveycampaign/1')

    def test_create(self):
        path, params = self.resource.create(1)
        self.assertEqual(path, 'head/survey/1/surveycampaign/')

    def test_update(self):
        path, params = self.resource.update(1, 1)
        self.assertEqual(path, 'head/survey/1/surveycampaign/1')

    def test_copy(self):
        path, params = self.resource.copy(1, 1)
        self.assertEqual(path, 'head/survey/1/surveycampaign/1')

    def test_delete(self):
        path, params = self.resource.delete(1, 1)
        self.assertEqual(path, 'head/survey/1/surveycampaign/1')


class SurveyOptionTests(TestCase):
    resource = client.api.surveyoption

    def test_list(self):
        path, params = self.resource.list(1, 1)
        self.assertEqual(path, 'head/survey/1/surveyquestion/1/surveyoption/')

    def test_get(self):
        path, params = self.resource.get(1, 1, 1)
        self.assertEqual(path, 'head/survey/1/surveyquestion/1/surveyoption/1')

    def test_create(self):
        path, params = self.resource.create(1, 1)
        self.assertEqual(path, 'head/survey/1/surveyquestion/1/surveyoption/')

    def test_update(self):
        path, params = self.resource.update(1, 1, 1)
        self.assertEqual(path, 'head/survey/1/surveyquestion/1/surveyoption/1')

    def test_copy(self):
        with self.assertRaises(NotImplementedError):
            self.resource.copy()

    def test_delete(self):
        path, params = self.resource.delete(1, 1, 1)
        self.assertEqual(path, 'head/survey/1/surveyquestion/1/surveyoption/1')


class SurveyPageTests(TestCase):
    resource = client.api.surveypage

    def test_list(self):
        path, params = self.resource.list(1)
        self.assertEqual(path, 'head/survey/1/surveypage/')

    def test_get(self):
        path, params = self.resource.get(1, 1)
        self.assertEqual(path, 'head/survey/1/surveypage/1')

    def test_create(self):
        path, params = self.resource.create(1)
        self.assertEqual(path, 'head/survey/1/surveypage/')

    def test_update(self):
        path, params = self.resource.update(1, 1)
        self.assertEqual(path, 'head/survey/1/surveypage/1')

    def test_copy(self):
        with self.assertRaises(NotImplementedError):
            self.resource.copy()

    def test_delete(self):
        path, params = self.resource.delete(1, 1)
        self.assertEqual(path, 'head/survey/1/surveypage/1')


class SurveyQuestionTests(TestCase):
    resource = client.api.surveyquestion

    def test_list(self):
        path, params = self.resource.list(1)
        self.assertEqual(path, 'head/survey/1/surveyquestion/')

    def test_get(self):
        path, params = self.resource.get(1, 1)
        self.assertEqual(path, 'head/survey/1/surveyquestion/1')

    def test_create(self):
        path, params = self.resource.create(1, 1)
        self.assertEqual(path, 'head/survey/1/surveypage/1/surveyquestion/')

    def test_update(self):
        path, params = self.resource.update(1, 1)
        self.assertEqual(path, 'head/survey/1/surveyquestion/1')

    def test_copy(self):
        with self.assertRaises(NotImplementedError):
            self.resource.copy()

    def test_delete(self):
        path, params = self.resource.delete(1, 1)
        self.assertEqual(path, 'head/survey/1/surveyquestion/1')


class SurveyReportTests(TestCase):
    resource = client.api.surveyreport

    def test_list(self):
        path, params = self.resource.list(1)
        self.assertEqual(path, 'head/survey/1/surveyreport/')

    def test_get(self):
        path, params = self.resource.get(1, 1)
        self.assertEqual(path, 'head/survey/1/surveyreport/1')

    def test_create(self):
        with self.assertRaises(NotImplementedError):
            self.resource.create()

    def test_update(self):
        path, params = self.resource.update(1, 1)
        self.assertEqual(path, 'head/survey/1/surveyreport/1')

    def test_copy(self):
        path, params = self.resource.copy(1, 1)
        self.assertEqual(path, 'head/survey/1/surveyreport/1')

    def test_delete(self):
        path, params = self.resource.delete(1, 1)
        self.assertEqual(path, 'head/survey/1/surveyreport/1')


class SurveyResponseTests(TestCase):
    resource = client.api.surveyresponse

    def test_list(self):
        path, params = self.resource.list(1)
        self.assertEqual(path, 'head/survey/1/surveyresponse/')

    def test_get(self):
        path, params = self.resource.get(1, 1)
        self.assertEqual(path, 'head/survey/1/surveyresponse/1')

    def test_create(self):
        path, params = self.resource.create(1)
        self.assertEqual(path, 'head/survey/1/surveyresponse/')

    def test_update(self):
        path, params = self.resource.update(1, 1)
        self.assertEqual(path, 'head/survey/1/surveyresponse/1')

    def test_copy(self):
        with self.assertRaises(NotImplementedError):
            self.resource.copy()

    def test_delete(self):
        path, params = self.resource.delete(1, 1)
        self.assertEqual(path, 'head/survey/1/surveyresponse/1')


class SurveyStatisticTests(TestCase):
    resource = client.api.surveystatistic

    def test_list(self):
        path, params = self.resource.list(1)
        self.assertEqual(path, 'head/survey/1/surveystatistic/')

    def test_get(self):
        with self.assertRaises(NotImplementedError):
            self.resource.get()

    def test_create(self):
        with self.assertRaises(NotImplementedError):
            self.resource.create()

    def test_update(self):
        with self.assertRaises(NotImplementedError):
            self.resource.update()

    def test_copy(self):
        with self.assertRaises(NotImplementedError):
            self.resource.copy()

    def test_delete(self):
        with self.assertRaises(NotImplementedError):
            self.resource.delete()
