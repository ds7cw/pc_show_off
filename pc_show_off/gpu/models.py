from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from pc_show_off.common.models import ComputerComponent


# Create your models here.
class Gpu(ComputerComponent):
    
    MAX_CHIP_MANUFACTURER_LEN = 8
    MAX_GPU_MANUFACTURER_LEN = 10
    MAX_SHORT_NAME_LEN = 25
    MAX_SERIES_LEN = 35
    MAX_CHIP_ARCH_LEN = 20

    MAX_V_RAM_VAL = 48
    MAX_STREAM_PROCESSORS_VAL = 50_000
    MAX_MEMORY_BUS_VAL = 8192
    MIN_RECOMMENDED_PSU_VAL = 300
    MAX_RECOMMENDED_PSU_VAL = 2050

    MAX_GPU_INTERFACE_LEN = 8

    class ManufacturerChoices(models.TextChoices):
        AMD = 'AMD', 'AMD'
        INTEL = 'Intel', 'Intel'
        NVIDIA = 'NVIDIA', 'NVIDIA'
        
    class GpuManufacturerChoices(models.TextChoices):
        Acer = 'Acer', 'Acer'
        AMD = 'AMD', 'AMD'
        ASRock = 'ASRock', 'ASRock'
        Biostar = 'Biostar', 'Biostar'
        EVGA = 'EVGA', 'EVGA'
        Gainward = 'Gainward', 'Gainward'
        Gigabyte = 'Gigabyte', 'Gigabyte'
        Inno3D = 'Inno3D', 'Inno3D'
        INTEL = 'Intel', 'Intel'
        KFA2 = 'KFA2', 'KFA2' 
        MSI = 'MSI', 'MSI'
        NVIDIA = 'NVIDIA', 'NVIDIA'
        Palit = 'Palit', 'Palit'
        PNY = 'PNY', 'PNY'
        PowerColor = 'PowerColor', 'PowerColor'
        Saphire = 'Saphire', 'Saphire'
        XFX = 'XFX', 'XFX'
        ZOTAC = 'ZOTAC', 'ZOTAC'

    class GpuInterfaceChoices(models.TextChoices):
        TWO = 'PCIe 2.0', 'PCIe 2.0'
        THREE = 'PCIe 3.0', 'PCIe 3.0'
        FOUR = 'PCIe 4.0', 'PCIe 4.0'
        FIVE = 'PCIe 5.0', 'PCIe 5.0'

    manufacturer = models.CharField(
        max_length=MAX_CHIP_MANUFACTURER_LEN,
        choices = ManufacturerChoices.choices,
    )

    gpu_manufacturer = models.CharField(
        max_length=MAX_GPU_MANUFACTURER_LEN,
        choices = GpuManufacturerChoices.choices,
    )

    short_model_name = models.CharField(
        blank=True,
        null=True,
        max_length=MAX_SHORT_NAME_LEN,
    )
    
    series = models.CharField(
        blank=True,
        null=True,
        max_length=MAX_SERIES_LEN,
    )

    chip_architecture = models.CharField(
        blank=True,
        null=True,
        max_length=MAX_SERIES_LEN,
    )

    v_ram = models.PositiveSmallIntegerField(
        blank=True,
        null=True,
        validators=[
            MaxValueValidator(MAX_V_RAM_VAL)
        ],
    )

    stream_processors = models.PositiveIntegerField(
        blank=True,
        null=True,
        validators=[
            MaxValueValidator(MAX_STREAM_PROCESSORS_VAL)
        ],
    )

    memory_bus = models.PositiveSmallIntegerField(
        blank=True,
        null=True,
        validators=[
            MaxValueValidator(MAX_MEMORY_BUS_VAL),
        ],
    )

    gpu_interface = models.CharField(
        blank=True,
        null=True,
        max_length=MAX_GPU_INTERFACE_LEN,
        choices=GpuInterfaceChoices.choices,
    )


    recommended_psu = models.PositiveSmallIntegerField(
        blank=True,
        null=True,
        validators=[
            MinValueValidator(MIN_RECOMMENDED_PSU_VAL),
            MaxValueValidator(MAX_RECOMMENDED_PSU_VAL),
        ],
    )

    gpu_release_date = models.DateField(
        blank=True,
        null=True,
    )

    def __str__(self) -> str:
        return self.short_model_name
