
from unittest import TestCase
from surveygizmo import SurveyGizmo

client = SurveyGizmo(
    base_url='',
    api_token='token',
    api_token_secret='secret',
    prepare_url=True,
)


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
        path, params = self.resource.create('team')
        self.assertEqual(path, 'head/accountteams/')
        self.assertEqual(params['teamname'], 'team')

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
        path, params = self.resource.create('user@example.com')
        self.assertEqual(path, 'head/accountuser/')
        self.assertEqual(params['email'], 'user@example.com')

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
        path, params = self.resource.create(1, 1, 'user@example.com')
        self.assertEqual(path, 'head/survey/1/surveycampaign/1/contact/')
        self.assertEqual(params['semailaddress'], 'user@example.com')

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
        path, params = self.resource.create('Contact List')
        self.assertEqual(path, 'head/contactlist/')
        self.assertEqual(params['listname'], 'Contact List')

    def test_update(self):
        path, params = self.resource.update(1, 'user@example.com')
        self.assertEqual(path, 'head/contactlist/1')
        self.assertEqual(params['semailaddress'], 'user@example.com')

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
        path, params = self.resource.create('My Survey', 'poll')
        self.assertEqual(path, 'head/survey/')
        self.assertEqual(params['title'], 'My Survey')
        self.assertEqual(params['type'], 'poll')

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
        path, params = self.resource.create(1, 'My Campaign', 'email')
        self.assertEqual(path, 'head/survey/1/surveycampaign/')
        self.assertEqual(params['name'], 'My Campaign')
        self.assertEqual(params['type'], 'email')

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
        path, params = self.resource.create(1, 1, 'Option', 'Value')
        self.assertEqual(path, 'head/survey/1/surveyquestion/1/surveyoption/')
        self.assertEqual(params['title'], 'Option')
        self.assertEqual(params['value'], 'Value')

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
        path, params = self.resource.create(1, 'Page 1')
        self.assertEqual(path, 'head/survey/1/surveypage/')
        self.assertEqual(params['title'], 'Page 1')

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
        self.assertEqual(params['copy'], 'false')

    def test_copy(self):
        path, params = self.resource.copy(1, 1)
        self.assertEqual(path, 'head/survey/1/surveyreport/1')
        self.assertEqual(params['copy'], 'true')

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
