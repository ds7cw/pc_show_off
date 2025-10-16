from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth import get_user_model


class RamApiTest(APITestCase):
    def setUp(self):
        """Set up test users & test data"""
        self.admin_user = get_user_model().objects.create_user(
            email='admin@user.com', password='testpass', is_staff=True)
        self.regular_user = get_user_model().objects.create_user(
            email='user@user.com', password='testpass', is_staff=False)

        self.ram_data =  {
            "id": 1,
            "model_name": "KF560C36BBE2K2-32",
            "is_verified": True,
            "manufacturer": "Kingston",
            "series": "Fury Beast",
            "memory_type": "DDR5",
            "total_ram": 32,
            "max_frequency": 6000,
            "default_frequency": 4800,
            "cas_latency": 36,
            "number_of_sticks": "2",
            "colour": "Black",
            "rgb": "None",
            "warranty": "Limited Lifetime Warranty",
            "contributor": self.admin_user.id
        }

    def test_create_and_retrieve_ram(self):
        """Good weather scenario"""
        self.client.force_authenticate(user=self.admin_user)
        create_response = self.client.post('/api/v1/rams/', self.ram_data, format='json')
        self.assertEqual(create_response.status_code, status.HTTP_201_CREATED)

        ram_id = create_response.data['id']

        # Retrieve RAM via API
        retrieve_response = self.client.get(f'/api/v1/rams/{ram_id}/')
        print('\nRAM Data:\n{}\n'.format(retrieve_response.data))
        self.assertEqual(retrieve_response.status_code, status.HTTP_200_OK)
        self.assertEqual(retrieve_response.data['manufacturer'], "Kingston")
        self.assertEqual(retrieve_response.data['warranty'], "Limited Lifetime Warranty")

    def test_regular_user_cannot_create_ram(self):
        """Bad weather scenario"""
        self.client.force_authenticate(user=self.regular_user)
        response = self.client.post('/api/v1/rams/', self.ram_data, format='json')
        self.assertEqual(response.status_code, 403)
