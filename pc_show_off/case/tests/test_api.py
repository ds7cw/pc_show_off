from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth import get_user_model


class CaseApiTest(APITestCase):
    def setUp(self):
        """Set up test users & test data"""
        self.admin_user = get_user_model().objects.create_user(
            email='admin@user.com', password='testpass', is_staff=True)
        self.regular_user = get_user_model().objects.create_user(
            email='user@user.com', password='testpass', is_staff=False)

        self.pc_case_data =  {
            "id": 1,
            "model_name": "CC-9011200-WW",
            "is_verified": True,
            "manufacturer": "Corsair",
            "series": "4000D Airflow",
            "tower_size": "Mid Tower",
            "form_factor": "ATX",
            "width": 230,
            "height": 466,
            "depth": 453,
            "psu_max_len": 220,
            "gpu_max_len": 360,
            "front_fans": "3",
            "top_fans": "2",
            "bottom_fans": "0",
            "rear_fans": "1",
            "colour": "Black",
            "contributor": self.admin_user.id
        }

    def test_create_and_retrieve_pc_case(self):
        """Good weather scenario"""
        self.client.force_authenticate(user=self.admin_user)
        create_response = self.client.post('/api/v1/cases/', self.pc_case_data, format='json')
        self.assertEqual(create_response.status_code, status.HTTP_201_CREATED)

        pc_case_id = create_response.data['id']

        # Retrieve PC Case via API
        retrieve_response = self.client.get(f'/api/v1/cases/{pc_case_id}/')
        print('\nPC Case Data:\n{}\n'.format(retrieve_response.data))
        self.assertEqual(retrieve_response.status_code, status.HTTP_200_OK)
        self.assertEqual(retrieve_response.data['manufacturer'], "Corsair")
        self.assertEqual(retrieve_response.data['series'], "4000D Airflow")
        self.assertEqual(retrieve_response.data['model_name'], "CC-9011200-WW")

    def test_regular_user_cannot_create_pc_case(self):
        """Bad weather scenario"""
        self.client.force_authenticate(user=self.regular_user)
        response = self.client.post('/api/v1/cases/', self.pc_case_data, format='json')
        self.assertEqual(response.status_code, 403)
