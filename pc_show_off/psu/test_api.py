from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth import get_user_model


class PsuApiTest(APITestCase):
    def setUp(self):
        """Set up test users & test data"""
        self.admin_user = get_user_model().objects.create_user(
            email='admin@user.com', password='testpass', is_staff=True)
        self.regular_user = get_user_model().objects.create_user(
            email='user@user.com', password='testpass', is_staff=False)

        self.psu_data =  {
            "id": 1,
            "model_name": "MAG A850GN PCIE5",
            "is_verified": True,
            "manufacturer": "MSI",
            "wattage": 850,
            "form_factor": "ATX",
            "fan_size": 120,
            "plus_rating": "Gold",
            "height": 86,
            "width": 150,
            "depth": 140,
            "warranty": 7,
            "contributor": 1
        }

    def test_create_and_retrieve_psu(self):
        """Good weather scenario"""
        self.client.force_authenticate(user=self.admin_user)
        create_response = self.client.post('/api/v1/psus/', self.psu_data, format='json')
        self.assertEqual(create_response.status_code, status.HTTP_201_CREATED)

        psu_id = create_response.data['id']

        # Retrieve PSU via API
        retrieve_response = self.client.get(f'/api/v1/psus/{psu_id}/')
        print('\nPSU Data:\n{}\n'.format(retrieve_response.data))
        self.assertEqual(retrieve_response.status_code, status.HTTP_200_OK)
        self.assertEqual(retrieve_response.data['manufacturer'], "MSI")
        self.assertEqual(retrieve_response.data['model_name'], "MAG A850GN PCIE5")
        self.assertEqual(retrieve_response.data['warranty'], 7)

    def test_regular_user_cannot_create_psu(self):
        """Bad weather scenario"""
        self.client.force_authenticate(user=self.regular_user)
        response = self.client.post('/api/v1/psus/', self.psu_data, format='json')
        self.assertEqual(response.status_code, 403)
