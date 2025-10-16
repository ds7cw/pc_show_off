from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth import get_user_model


class MoboApiTest(APITestCase):
    def setUp(self):
        """Set up test users & test data"""
        self.admin_user = get_user_model().objects.create_user(
            email='admin@user.com', password='testpass', is_staff=True)
        self.regular_user = get_user_model().objects.create_user(
            email='user@user.com', password='testpass', is_staff=False)

        self.mobo_data = {
            "id": 1,
            "model_name": "MAG X670E TOMAHAWK WIFI",
            "is_verified": True,
            "manufacturer": "MSI",
            "platform": "AMD",
            "cpu_socket": "AM5",
            "chipset": "X670",
            "series": "MAG",
            "atx_factor": "ATX",
            "memory_type": "DDR5",
            "memory_slots": "4",
            "maximum_ram": 256,
            "gpu_interface": "PCIe 5.0",
            "contributor": self.admin_user.id
        }

    def test_create_and_retrieve_mobo(self):
        """Good weather scenario"""
        self.client.force_authenticate(user=self.admin_user)
        create_response = self.client.post('/api/v1/mobos/', self.mobo_data, format='json')
        self.assertEqual(create_response.status_code, status.HTTP_201_CREATED)

        mobo_id = create_response.data['id']

        # Retrieve Motherboard via API
        retrieve_response = self.client.get(f'/api/v1/mobos/{mobo_id}/')
        print('\nMotherboard Data:\n{}\n'.format(retrieve_response.data))
        self.assertEqual(retrieve_response.status_code, status.HTTP_200_OK)
        self.assertEqual(retrieve_response.data['manufacturer'], "MSI")
        self.assertEqual(retrieve_response.data['model_name'], "MAG X670E TOMAHAWK WIFI")

    def test_regular_user_cannot_create_mobo(self):
        """Bad weather scenario"""
        self.client.force_authenticate(user=self.regular_user)
        response = self.client.post('/api/v1/mobos/', self.mobo_data, format='json')
        self.assertEqual(response.status_code, 403)
