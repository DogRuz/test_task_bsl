from django.test import TestCase
from django.core.management import call_command


# Create your tests here.

class ViewsTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        """
        Load data in test db
        """
        call_command('loaddata', 'db.json', verbosity=0)

    def test_get_info_person_none_id(self):
        """
        Testing without parameters
        """
        response = self.client.get('/api/status/', format='json')
        self.assertEqual(response.status_code, 400)

    def test_get_info_person_none_id_db(self):
        """
        Testing with no id
        """
        response = self.client.get('/api/status?id=15f4a3d4-0211-479a-a5c6-c85e56bd4d89', format='json')
        self.assertEqual(response.status_code, 404)

    def test_get_info_person_good_id_db(self):
        """
        Testing with id which is
        """
        response = self.client.get('/api/status?id=15f4a3d4-0211-479a-a5c6-c85e56bd4d88', format='json')
        self.assertEqual(response.status_code, 200)

    def test_subtraction_balance_none_sum(self):
        """
        Testing without parameters
        """
        response = self.client.post('/api/substract/', format='json')
        self.assertEqual(response.status_code, 400)

    def test_subtraction_balance_big_sum(self):
        """
        Testing with big sum
        """
        response = self.client.post('/api/substract',
                                    {'id': '15f4a3d4-0211-479a-a5c6-c85e56bd4d88', 'get_sum': '12978'},
                                    format='json')
        self.assertEqual(response.status_code, 402)

    def test_subtraction_balance_sum_db(self):
        """
        Testing with norm sum
        """
        response = self.client.post('/api/substract',
                                    {'id': '15f4a3d4-0211-479a-a5c6-c85e56bd4d88', 'get_sum': '1'},
                                    format='json')
        self.assertEqual(response.status_code, 200)

    def test_add_balance_sum_db(self):
        """
        Testing add with norm sum
        """
        response = self.client.post('/api/add',
                                    {'id': '15f4a3d4-0211-479a-a5c6-c85e56bd4d88', 'get_sum': '100000'},
                                    format='json')
        self.assertEqual(response.status_code, 200)
