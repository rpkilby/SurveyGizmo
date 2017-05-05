
from unittest import TestCase
from surveygizmo import SurveyGizmo

client = SurveyGizmo(api_token='token', api_token_secret='secret', prepare_url=True)
client.api.base_url = ''


class ResourceTests(TestCase):
    def test_authentication(self):
        _, params = client.api.survey.get(1)
        self.assertEqual(params['api_token'], 'token')
        self.assertEqual(params['api_token_secret'], 'secret')

    def test_methods(self):
        _, params = client.api.survey.list()
        self.assertNotIn('_method', params)

        _, params = client.api.survey.get(1)
        self.assertNotIn('_method', params)

        _, params = client.api.survey.create('My Survey', 'poll')
        self.assertEqual(params['_method'], 'PUT')

        _, params = client.api.survey.update(1)
        self.assertEqual(params['_method'], 'POST')

        _, params = client.api.survey.copy(1)
        self.assertEqual(params['_method'], 'POST')

        _, params = client.api.survey.delete(1)
        self.assertEqual(params['_method'], 'DELETE')


class FilteringTests(TestCase):
    def test_copy_on_filter(self):
        resource1 = client.api.survey
        resource2 = resource1.filter('field', 'op', 'value')

        self.assertIsNot(resource1, resource2)

    def test_filter_chaining(self):
        resource1 = client.api.survey
        resource2 = resource1.filter('field', 'op', 'value')
        resource3 = resource2.filter('field', 'op', 'value')

        self.assertEqual(len(resource1._filters), 0)
        self.assertEqual(len(resource2._filters), 1)
        self.assertEqual(len(resource3._filters), 2)

    def test_list_filters(self):
        _, params = client.api.survey.filter('field', 'op', 'value').list()

        self.assertEqual(params['filter[field][0]'], 'field')
        self.assertEqual(params['filter[operator][0]'], 'op')
        self.assertEqual(params['filter[value][0]'], 'value')

    def test_duplicate_calls(self):
        resource = client.api.survey.filter('field', 'op', 'value')

        _, params = resource.list()

        self.assertEqual(params['filter[field][0]'], 'field')
        self.assertEqual(params['filter[operator][0]'], 'op')
        self.assertEqual(params['filter[value][0]'], 'value')

        _, params = resource.list()

        self.assertEqual(params['filter[field][0]'], 'field')
        self.assertEqual(params['filter[operator][0]'], 'op')
        self.assertEqual(params['filter[value][0]'], 'value')

    def test_no_persistence(self):
        _, params = client.api.survey.filter('field', 'op', 'value').list()

        self.assertEqual(params['filter[field][0]'], 'field')
        self.assertEqual(params['filter[operator][0]'], 'op')
        self.assertEqual(params['filter[value][0]'], 'value')

        _, params = client.api.survey.list()
        self.assertNotIn('filter[field][0]', params)
        self.assertNotIn('filter[operator][0]', params)
        self.assertNotIn('filter[value][0]', params)

    def test_pagination(self):
        _, params = client.api.surveyresponse.resultsperpage('3').list(1)
        self.assertEqual(params['resultsperpage'], '3')

        _, params = client.api.surveyresponse.page('5').list(1)
        self.assertEqual(params['page'], '5')
