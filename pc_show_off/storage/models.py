from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from pc_show_off.common.models import ComputerComponent


# Create your models here.
class Storage(ComputerComponent):
    
    MAX_MANUFACTURER_LEN = 15
    MAX_SERIES_LEN = 35
    MAX_FORM_FACTOR_LEN = 10
    MAX_INTERFACE_LEN = 8
    MAX_PCIE_INTERFACE_LEN = 8
    
    MAX_TOTAL_STORAGE_VAL = 8192
    MAX_READ_SPEED_VAL = 30_000
    MAX_WRITE_SPEED_VAL = 30_000
    MAX_LENGTH_VAL = 200

    class ManufacturerChoices(models.TextChoices):
        ADATA = 'ADATA', 'ADATA'
        Apacer = 'Apacer', 'Apacer'
        Corsair = 'Corsair', 'Corsair'
        Crucial = 'Crucial', 'Crucial'
        Gigabyte = 'Gigabyte', 'Gigabyte'
        HP = 'HP', 'HP'
        INTEL = 'Intel', 'Intel'
        Kingston = 'Kingston', 'Kingston'
        Lenovo = 'Lenovo', 'Lenovo'
        Lexar = 'Lexar', 'Lexar'
        Micron = 'Micron', 'Micron'
        Patriot = 'Patriot', 'Patriot'
        Samsung = 'Samsung', 'Samsung'
        SanDisk = 'SanDisk', 'SanDisk'
        Seagate = 'Seagate', 'Seagate'
        SiliconPower = 'Silicon Power', 'Silicon Power'
        SKHynix = 'SK Hynix', 'SK Hynix'
        TeamGroup = 'TeamGroup', 'TeamGroup'
        Thermaltake = 'Thermaltake', 'Thermaltake'
        Transcend = 'Transcend', 'Transcend'
        WD = 'WD', 'WD'

    class FormFactorChoices(models.TextChoices):
        M_2280 = 'M.2 (2280)', 'M.2 (2280)'
        M_2242 = 'M.2 (2242)', 'M.2 (2242)'
        M_2230 = 'M.2 (2230)', 'M.2 (2230)'
        M_2260 = 'M.2 (2260)', 'M.2 (2260)'
        SATA_25 = '2.5\"', '2.5\"'
    
    class InterfaceChoices(models.TextChoices):
        NVME = 'NVMe', 'NVMe'
        SATA3 = 'SATA 3', 'SATA 3'
    
    class PcieInterfaceChoices(models.TextChoices):
        NONE = 'N/A', 'N/A'
        THREE = 'PCIe 3.0', 'PCIe 3.0'
        FOUR = 'PCIe 4.0', 'PCIe 4.0'
        FIVE = 'PCIe 5.0', 'PCIe 5.0'

    manufacturer = models.CharField(
        max_length=MAX_MANUFACTURER_LEN,
        choices = ManufacturerChoices.choices,
    )
    
    series = models.CharField(
        blank=True,
        null=True,
        max_length=MAX_SERIES_LEN,
    )

    form_factor = models.CharField(
        blank=True,
        null=True,
        max_length=MAX_FORM_FACTOR_LEN,
        choices=FormFactorChoices.choices,
    )

    interface = models.CharField(
        blank=True,
        null=True,
        max_length=MAX_INTERFACE_LEN,
        choices=InterfaceChoices.choices,
    )

    pcie_interface = models.CharField(
        blank=True,
        null=True,
        max_length=MAX_PCIE_INTERFACE_LEN,
        choices=PcieInterfaceChoices.choices,
    )

    total_storage = models.PositiveSmallIntegerField(
        blank=True,
        null=True,
        validators=[
            MaxValueValidator(MAX_TOTAL_STORAGE_VAL),
        ],
    )

    read_speed = models.PositiveSmallIntegerField(
        blank=True,
        null=True,
        validators=[
            MaxValueValidator(MAX_READ_SPEED_VAL),
        ],
    )

    write_speed = models.PositiveSmallIntegerField(
        blank=True,
        null=True,
        validators=[
            MaxValueValidator(MAX_WRITE_SPEED_VAL),
        ],
    )

    length = models.PositiveSmallIntegerField(
        blank=True,
        null=True,
        validators=[
            MaxValueValidator(MAX_LENGTH_VAL),
        ],
    )

    def __str__(self) -> str:
        return f'{self.manufacturer} {self.series} {self.total_storage}GB {self.interface}'
