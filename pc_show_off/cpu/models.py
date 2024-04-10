from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from pc_show_off.common.models import ComputerComponent


# Create your models here.
class Cpu(ComputerComponent):

    MAX_MANUFACTURER_LEN = 5
    
    MAX_CPU_ARCHITECTURE_LEN = 25
    MAX_CPU_SOCKET_LEN = 15

    MAX_P_CORE_BASE_CLOCK = 10
    MIN_P_CORE_BASE_CLOCK = 0.1
    MAX_P_CORE_BOOST_CLOCK = 10
    MIN_P_CORE_BOOST_CLOCK = 0.1

    class ManufacturerChoices(models.TextChoices):
        INTEL = 'Intel', 'Intel'
        AMD = 'AMD', 'AMD'
    
    manufacturer = models.CharField(
        max_length=MAX_MANUFACTURER_LEN,
        choices = ManufacturerChoices.choices,
    )

    cpu_architecture = models.CharField(
        blank=True,
        null=True,
        max_length=MAX_CPU_ARCHITECTURE_LEN,
    )

    cpu_socket = models.CharField(
        blank=True,
        null=True,
        max_length=MAX_CPU_SOCKET_LEN,
    )

    total_cores = models.PositiveSmallIntegerField(
        blank=True,
        null=True,
    )

    p_core_base_clock = models.FloatField(
        blank=True,
        null=True,
        validators=[
            MaxValueValidator(MAX_P_CORE_BASE_CLOCK),
            MinValueValidator(MIN_P_CORE_BASE_CLOCK),
        ],
    ) 

    p_core_boost_clock = models.FloatField(
        blank=True,
        null=True,
        validators=[
            MaxValueValidator(MAX_P_CORE_BOOST_CLOCK),
            MinValueValidator(MIN_P_CORE_BOOST_CLOCK),
        ],
    )

    cpu_level_3_cache = models.PositiveSmallIntegerField(
        blank=True,
        null=True,
    )

    cpu_release_date = models.DateField(
        blank=True,
        null=True,
    )

    def __str__(self) -> str:
        return f'{self.manufacturer} {self.model_name}'
