from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth import get_user_model
from pc_show_off.cpu.models import Cpu
from pc_show_off.gpu.models import Gpu
from pc_show_off.mobo.models import Mobo
from pc_show_off.ram.models import Ram
from pc_show_off.psu.models import Psu
from pc_show_off.storage.models import Storage
from pc_show_off.case.models import Case


class PcApiTest(APITestCase):
    def setUp(self):
        """Set up test users & test data"""
        self.admin_user = get_user_model().objects.create_user(
            email='admin@user.com', password='testpass', is_staff=True)
        self.regular_user = get_user_model().objects.create_user(
            email='user@user.com', password='testpass', is_staff=False)

        self.cpu = Cpu.objects.create(
            model_name = "Ryzen 7 7800X3D",
            is_verified = True,
            manufacturer = "AMD",
            cpu_architecture = "Raphael",
            cpu_socket = "AM5",
            total_cores = 8,
            p_core_base_clock = 4.2,
            p_core_boost_clock = 5.0,
            cpu_level_3_cache = 96,
            cpu_release_date = "2023-04-06",
            contributor = self.admin_user
        )

        self.gpu = Gpu.objects.create(
            model_name = "ZT-D40720E-10M",
            is_verified = True,
            manufacturer = "NVIDIA",
            gpu_manufacturer = "ZOTAC",
            short_model_name = "4070 Super",
            series = "Twin Edge",
            chip_architecture = "AD104",
            v_ram = 12,
            stream_processors = 7168,
            memory_bus = 192,
            gpu_interface = "PCIe 4.0",
            recommended_psu = 650,
            gpu_release_date = "2024-01-08",
            contributor = self.admin_user
        )

        self.mobo = Mobo.objects.create(
            model_name = "MAG X670E TOMAHAWK WIFI",
            is_verified = True,
            manufacturer = "MSI",
            platform = "AMD",
            cpu_socket = "AM5",
            chipset = "X670",
            series = "MAG",
            atx_factor = "ATX",
            memory_type = "DDR5",
            memory_slots = "4",
            maximum_ram = 256,
            gpu_interface = "PCIe 5.0",
            contributor = self.admin_user
        )

        self.ram = Ram.objects.create(
            model_name = "KF560C36BBE2K2-32",
            is_verified = True,
            manufacturer = "Kingston",
            series = "Fury Beast",
            memory_type = "DDR5",
            total_ram = 32,
            max_frequency = 6000,
            default_frequency = 4800,
            cas_latency = 36,
            number_of_sticks = "2",
            colour = "Black",
            rgb = "None",
            warranty = "Limited Lifetime Warranty",
            contributor = self.admin_user
        )

        self.storage = Storage.objects.create(
            model_name = "SNV3S/2000G",
            is_verified = True,
            manufacturer = "Kingston",
            series = "NV3",
            form_factor = "M.2 (2280)",
            interface = "NVMe",
            pcie_interface = "PCIe 4.0",
            total_storage = 2000,
            read_speed = 6000,
            write_speed = 5000,
            length = 80,
            contributor = self.admin_user
        )

        self.psu = Psu.objects.create(
            model_name = "MAG A850GN PCIE5",
            is_verified = True,
            manufacturer = "MSI",
            wattage = 850,
            form_factor = "ATX",
            fan_size = 120,
            plus_rating = "Gold",
            height = 86,
            width = 150,
            depth = 140,
            warranty = 7,
            contributor = self.admin_user
        )

        self.case = Case.objects.create(
            model_name = "CC-9011200-WW",
            is_verified = True,
            manufacturer = "Corsair",
            series = "4000D Airflow",
            tower_size = "Mid Tower",
            form_factor = "ATX",
            width = 230,
            height = 466,
            depth = 453,
            psu_max_len = 220,
            gpu_max_len = 360,
            front_fans = "3",
            top_fans = "2",
            bottom_fans = "0",
            rear_fans = "1",
            colour = "Black",
            contributor = self.admin_user
        )

        self.pc_data =  {
            "id": 1,
            "pc_name": "Terminator",
            "description": "",
            "approx_cost": "999.99",
            "owner": 1,
            "cpu_part": self.cpu.id,
            "gpu_part": self.gpu.id,
            "mobo_part": self.mobo.id,
            "ram_part": self.ram.id,
            "psu_part": self.psu.id,
            "storage_part": self.storage.id,
            "case_part":self.case.id
        }

    def test_create_and_retrieve_pc(self):
        """Good weather scenario"""
        self.client.force_authenticate(user=self.admin_user)
        create_response = self.client.post('/api/v1/pcs/', self.pc_data, format='json')
        self.assertEqual(create_response.status_code, status.HTTP_201_CREATED)

        pc_id = create_response.data['id']

        # Retrieve PC via API
        retrieve_response = self.client.get(f'/api/v1/pcs/{pc_id}/')
        print('\nPC Data:\n{}\n'.format(retrieve_response.data))
        self.assertEqual(retrieve_response.status_code, status.HTTP_200_OK)
        self.assertEqual(retrieve_response.data['pc_name'], "Terminator")
        self.assertEqual(retrieve_response.data['approx_cost'], "999.99")
        self.assertEqual(retrieve_response.data['cpu_part'], self.cpu.id)
        self.assertEqual(retrieve_response.data['mobo_part'], self.mobo.id)

    def test_regular_user_cannot_create_pc(self):
        """Bad weather scenario"""
        self.client.force_authenticate(user=self.regular_user)
        response = self.client.post('/api/v1/pcs/', self.pc_data, format='json')
        self.assertEqual(response.status_code, 403)
