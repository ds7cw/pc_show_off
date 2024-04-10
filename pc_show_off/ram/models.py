from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from pc_show_off.common.models import ComputerComponent


# Create your models here.
class Ram(ComputerComponent):
    
    MAX_MANUFACTURER_LEN = 15
    MAX_SERIES_LEN = 35
    MAX_MEM_TYPE_LEN = 5

    MAX_TOTAL_RAM_VAL = 256
    MAX_FREQUENCY_VAL = 8800
    MAX_DEFAULT_FREQUENCY_VAL = 6600
    MAX_LATENCY_VAL = 100

    MAX_NUMBER_OF_STICKS_LEN = 2
    MAX_RGB_LEN = 4
    MAX_COLOUR_LEN = 8
    MAX_WARRANTY_LEN = 25

    class ManufacturerChoices(models.TextChoices):
        ADATA = 'ADATA', 'ADATA'
        Apacer = 'Apacer', 'Apacer'
        Biostar = 'Biostar', 'Biostar'
        Corsair = 'Corsair', 'Corsair'
        Crucial = 'Crucial', 'Crucial'
        Dynac = 'Dynac', 'Dynac'
        GSKILL = 'G.Skill', 'G.Skill'
        Gigabyte = 'Gigabyte', 'Gigabyte'
        HP = 'HP', 'HP'
        Kingston = 'Kingston', 'Kingston'
        Lexar = 'Lexar', 'Lexar'
        Patriot = 'Patriot', 'Patriot'
        Samsung = 'Samsung', 'Samsung'
        SiliconPower = 'Silicon Power', 'Silicon Power'
        SKHynix = 'SK Hynix', 'SK Hynix'
        TeamGroup = 'TeamGroup', 'TeamGroup'
        Thermaltake = 'Thermaltake', 'Thermaltake'
        Transcend = 'Transcend', 'Transcend'

    class MemoryTypeChoices(models.TextChoices):
        DDR4 = 'DDR4', 'DDR4'
        DDR5 = 'DDR5', 'DDR5'
    
    class NumberOfSticksChoices(models.TextChoices):
        ONE = '1', '1'
        TWO = '2', '2'
        FOUR = '4', '4'
        EIGHT = '8', '8'
    
    class ColourChoices(models.TextChoices):
        BLACK = 'Black', 'Black'
        WHITE = 'White', 'White'
        RED = 'Red', 'Red'
        BLUE = 'Blue', 'Blue'
        GREEN = 'Green', 'Green'
        GOLD = 'Gold', 'Gold'
        Silver = 'Silver', 'Silver'
        GREY = 'Grey', 'Grey'
        PINK = 'Pink', 'Pink'

    class RgbChoices(models.TextChoices):
        NONE = 'None', 'None'
        RGB = 'RGB', 'RGB'
        ARGB = 'ARGB', 'ARGB'
    
    manufacturer = models.CharField(
        max_length=MAX_MANUFACTURER_LEN,
        choices = ManufacturerChoices.choices,
    )
    
    series = models.CharField(
        blank=True,
        null=True,
        max_length=MAX_SERIES_LEN,
    )

    memory_type = models.CharField(
        blank=True,
        null=True,
        max_length=MAX_MEM_TYPE_LEN,
        choices=MemoryTypeChoices.choices,
    )

    total_ram = models.PositiveSmallIntegerField(
        blank=True,
        null=True,
        validators=[
            MaxValueValidator(MAX_TOTAL_RAM_VAL),
        ],
    )

    max_frequency = models.PositiveSmallIntegerField(
        blank=True,
        null=True,
        validators=[
            MaxValueValidator(MAX_FREQUENCY_VAL),
        ],
    )

    default_frequency = models.PositiveSmallIntegerField(
        blank=True,
        null=True,
        validators=[
            MaxValueValidator(MAX_DEFAULT_FREQUENCY_VAL),
        ],
    )

    cas_latency = models.PositiveSmallIntegerField(
        blank=True,
        null=True,
        validators=[
            MaxValueValidator(MAX_LATENCY_VAL),
        ],
    )

    number_of_sticks = models.CharField(
        blank=True,
        null=True,
        max_length=MAX_NUMBER_OF_STICKS_LEN,
        choices=NumberOfSticksChoices.choices,
    )

    colour = models.CharField(
        blank=True,
        null=True,
        max_length=MAX_COLOUR_LEN,
        choices=ColourChoices.choices,
    )

    rgb = models.CharField(
        blank=True,
        null=True,
        max_length=MAX_RGB_LEN,
        choices=RgbChoices.choices,
        default=RgbChoices.NONE,
    )

    warranty = models.CharField(
        blank=True,
        null=True,
        max_length=MAX_WARRANTY_LEN,
    )

    def __str__(self):
        return f'{self.manufacturer} {self.series} {self.total_ram} {self.memory_type} {self.max_frequency}MHz CL{self.cas_latency}'
