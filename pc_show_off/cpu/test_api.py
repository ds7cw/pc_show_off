from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth import get_user_model

class CpuApiTest(APITestCase):
    def setUp(self):
        """Set up test users & test data"""
        self.admin_user = get_user_model().objects.create_user(
            email='admin@user.com', password='testpass', is_staff=True)
        self.regular_user = get_user_model().objects.create_user(
            email='regular@user.com', password='testpass', is_staff=False)

        self.cpu_data = {
            "id": 2,
            "model_name": "Core i7-13700K",
            "is_verified": False,
            "manufacturer": "Intel",
            "cpu_architecture": "Raptor Lake-S",
            "cpu_socket": "1700",
            "total_cores": 16,
            "p_core_base_clock": 3.4,
            "p_core_boost_clock": 5.4,
            "cpu_level_3_cache": 30,
            "cpu_release_date": "2022-09-27",
            "contributor": 1
        }
        
    def test_create_and_retrieve_cpu(self):
        """Good weather scenario"""
        self.client.force_authenticate(user=self.admin_user)
        create_response = self.client.post('/api/v1/cpus/', self.cpu_data, format='json')
        self.assertEqual(create_response.status_code, status.HTTP_201_CREATED)

        cpu_id = create_response.data['id']

        # Retrieve CPU via API
        retrieve_response = self.client.get(f'/api/v1/cpus/{cpu_id}/')
        print('\nCPU Data:\n{}\n'.format(retrieve_response.data))
        self.assertEqual(retrieve_response.status_code, status.HTTP_200_OK)
        self.assertEqual(retrieve_response.data['manufacturer'], "Intel")
        self.assertEqual(retrieve_response.data['model_name'], "Core i7-13700K")

    def test_regular_user_cannot_create_cpu(self):
        """Bad weather scenario"""
        self.client.force_authenticate(user=self.regular_user)
        response = self.client.post('/api/v1/cpus/', self.cpu_data, format='json')
        self.assertEqual(response.status_code, 403)
