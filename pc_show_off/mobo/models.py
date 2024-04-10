from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from pc_show_off.common.models import ComputerComponent


# Create your models here.
class Mobo(ComputerComponent):

    MAX_MANUFACTURER_LEN = 10
    MAX_PLATFORM_LEN = 5 
    
    MAX_CPU_SOCKET_LEN = 15
    MAX_CHIPSET_LEN = 50
    MAX_SERIES_LEN = 25
    MAX_ATX_FACTOR_LEN = 14

    MAX_MEM_TYPE_LEN = 4
    MAX_MEM_SLOTS_LEN = 1
    MAX_MEM_CAPACITY_VAL = 2048

    MAX_GPU_INTERFACE_LEN = 8

    class ManufacturerChoices(models.TextChoices):
        Asus = 'Asus', 'Asus'
        ASRock = 'ASRock', 'ASRock'
        Biostar = 'Biostar', 'Biostar'
        EVGA = 'EVGA', 'EVGA'
        Gigabyte = 'Gigabyte', 'Gigabyte'
        MSI = 'MSI', 'MSI'
        NZXT = 'NZXT', 'NZXT'
    
    class PlatformChoices(models.TextChoices):
        INTEL = 'Intel', 'Intel'
        AMD = 'AMD', 'AMD'
    
    class AtxFactorChoices(models.TextChoices):
        XL = 'XL-ATX', 'XL-ATX'
        E = 'E-ATX', 'E-ATX'
        ATX = 'ATX', 'ATX'
        MICRO = 'Micro-ATX', 'Micro-ATX'
        MINI = 'Mini-ITX', 'Mini-ITX'
        THIN = 'Thin Mini-ITX', 'Thin Mini-ITX'

    class MemoryTypeChoices(models.TextChoices):
        DDR4 = 'DDR4', 'DDR4'
        DDR5 = 'DDR5', 'DDR5'
    
    class MemorySlotsChoices(models.TextChoices):
        ONE = '1', '1'
        TWO = '2', '2'
        FOUR = '4', '4'
        EIGHT = '8', '8'
    
    class GpuInterfaceChoices(models.TextChoices):
        TWO = 'PCIe 2.0', 'PCIe 2.0'
        THREE = 'PCIe 3.0', 'PCIe 3.0'
        FOUR = 'PCIe 4.0', 'PCIe 4.0'
        FIVE = 'PCIe 5.0', 'PCIe 5.0'

    manufacturer = models.CharField(
        max_length=MAX_MANUFACTURER_LEN,
        choices = ManufacturerChoices.choices,
    )

    platform = models.CharField(
        max_length=MAX_PLATFORM_LEN,
        choices = PlatformChoices.choices,
    )

    cpu_socket = models.CharField(
        blank=True,
        null=True,
        max_length=MAX_CPU_SOCKET_LEN,
    )

    chipset = models.CharField(
        blank=True,
        null=True,
        max_length=MAX_CHIPSET_LEN,
    )

    series = models.CharField(
        blank=True,
        null=True,
        max_length=MAX_SERIES_LEN,
    )
    
    atx_factor = models.CharField(
        blank=True,
        null=True,
        max_length=MAX_ATX_FACTOR_LEN,
        choices=AtxFactorChoices.choices,
    )

    memory_type = models.CharField(
        blank=True,
        null=True,
        max_length=MAX_MEM_TYPE_LEN,
        choices=MemoryTypeChoices.choices,
    )

    memory_slots = models.CharField(
        blank=True,
        null=True,
        max_length=MAX_MEM_SLOTS_LEN,
        choices=MemorySlotsChoices.choices,
    )

    maximum_ram = models.PositiveSmallIntegerField(
        blank=True,
        null=True,
        validators=[
            MaxValueValidator(MAX_MEM_CAPACITY_VAL),
        ],
    )

    gpu_interface = models.CharField(
        blank=True,
        null=True,
        max_length=MAX_GPU_INTERFACE_LEN,
        choices=GpuInterfaceChoices.choices,
    )

    def __str__(self) -> str:
        return f'{self.manufacturer} {self.series} {self.chipset} {self.platform} {self.cpu_socket} {self.memory_type}'
