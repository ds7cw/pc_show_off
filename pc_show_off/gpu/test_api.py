from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth import get_user_model

class GpuApiTest(APITestCase):
    def setUp(self):
        # Create a user and authenticate
        self.user = get_user_model().objects.create_user(email='testuser', password='testpass')
        self.client.force_authenticate(user=self.user)

    def test_create_and_retrieve_gpu(self):
        create_data = {
            "id": 1,
            "model_name": "ZT-D40720E-10M",
            "is_verified": True,
            "manufacturer": "NVIDIA",
            "gpu_manufacturer": "ZOTAC",
            "short_model_name": "RTX 4070 Super",
            "series": "Twin Edge",
            "chip_architecture": "AD104",
            "v_ram": 12,
            "stream_processors": 7168,
            "memory_bus": 192,
            "gpu_interface": "PCIe 4.0",
            "recommended_psu": 650,
            "gpu_release_date": "2024-01-08",
            "contributor": 1
        }
        create_response = self.client.post('/api/v1/gpus/', create_data, format='json')
        self.assertEqual(create_response.status_code, status.HTTP_201_CREATED)

        gpu_id = create_response.data['id']

        # Retrieve CPU via API
        retrieve_response = self.client.get(f'/api/v1/gpus/{gpu_id}/')
        print('\nGPU Data:\n{}\n'.format(retrieve_response.data))
        self.assertEqual(retrieve_response.status_code, status.HTTP_200_OK)
        self.assertEqual(retrieve_response.data['manufacturer'], "NVIDIA")
        self.assertEqual(retrieve_response.data['short_model_name'], "RTX 4070 Super")
