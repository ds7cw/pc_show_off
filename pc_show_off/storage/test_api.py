from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth import get_user_model


class StorageApiTest(APITestCase):
    def setUp(self):
        """Set up test users & test data"""
        self.admin_user = get_user_model().objects.create_user(
            email='admin@user.com', password='testpass', is_staff=True)
        self.regular_user = get_user_model().objects.create_user(
            email='user@user.com', password='testpass', is_staff=False)

        self.storage_data =  {
            "id": 1,
            "model_name": "SNV3S/2000G",
            "is_verified": True,
            "manufacturer": "Kingston",
            "series": "NV3",
            "form_factor": "M.2 (2280)",
            "interface": "NVMe",
            "pcie_interface": "PCIe 4.0",
            "total_storage": 2000,
            "read_speed": 6000,
            "write_speed": 5000,
            "length": 80,
            "contributor": 1
        }

    def test_create_and_retrieve_storage(self):
        """Good weather scenario"""
        self.client.force_authenticate(user=self.admin_user)
        create_response = self.client.post('/api/v1/storage-devices/', self.storage_data, format='json')
        self.assertEqual(create_response.status_code, status.HTTP_201_CREATED)

        storage_id = create_response.data['id']

        # Retrieve Storage Device via API
        retrieve_response = self.client.get(f'/api/v1/storage-devices/{storage_id}/')
        print('\nStorage Device Data:\n{}\n'.format(retrieve_response.data))
        self.assertEqual(retrieve_response.status_code, status.HTTP_200_OK)
        self.assertEqual(retrieve_response.data['manufacturer'], "Kingston")
        self.assertEqual(retrieve_response.data['model_name'], "SNV3S/2000G")
        self.assertEqual(retrieve_response.data['pcie_interface'], "PCIe 4.0")

    def test_regular_user_cannot_create_storage(self):
        """Bad weather scenario"""
        self.client.force_authenticate(user=self.regular_user)
        response = self.client.post('/api/v1/storage-devices/', self.storage_data, format='json')
        self.assertEqual(response.status_code, 403)
