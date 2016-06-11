
from unittest import TestCase
from surveygizmo import SurveyGizmo

client = SurveyGizmo(api_token='token', api_token_secret='secret', prepare_url=True)
client.api.base_url = ''


class AccountTests(TestCase):
    def test_list(self):
        with self.assertRaises(NotImplementedError):
            client.api.account.list()

    def test_get(self):
        path, params = client.api.account.get()

        self.assertEqual(path, 'head/account/')

    def test_create(self):
        with self.assertRaises(NotImplementedError):
            client.api.account.create()

    def test_update(self):
        with self.assertRaises(NotImplementedError):
            client.api.account.update()

    def test_copy(self):
        with self.assertRaises(NotImplementedError):
            client.api.account.copy()

    def test_delete(self):
        with self.assertRaises(NotImplementedError):
            client.api.account.delete()
