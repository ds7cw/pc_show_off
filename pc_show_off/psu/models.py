from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from pc_show_off.common.models import ComputerComponent


# Create your models here.
class Psu(ComputerComponent):

    MAX_MANUFACTURER_LEN = 20

    MAX_WATTAGE_VAL = 2050
    MAX_FORM_FACTOR_LEN = 8
    MAX_PLUS_RATING_LEN = 16

    MAX_FAN_SIZE_VAL = 360
    MAX_DIMS_VAL = 300
    MAX_WARRANTY_VAL = 10

    class ManufacturerChoices(models.TextChoices):
        FirstPlayer = '1stPlayer', '1stPlayer'
        ADATA = 'ADATA', 'ADATA'
        AeroCool = 'AeroCool', 'AeroCool'
        Antec = 'Antec', 'Antec'
        Asus = 'Asus', 'Asus'
        BeQuiet = 'be quiet!', 'be quiet!'
        BitFenix = 'BitFenix', 'BitFenix'
        Chieftec = 'Chieftec', 'Chieftec'
        CoolerMaster = 'Cooler Master', 'Cooler Master'
        Corsair = 'Corsair', 'Corsair'
        DeepCool = 'DeepCool', 'DeepCool'
        DeltaElectronics = 'Delta Electronics', 'Delta Electronics'
        Endorfy = 'Endorfy', 'Endorfy'
        EVGA = 'EVGA', 'EVGA'
        FractalDesign = 'Fractal Design', 'Fractal Design'
        FSP = 'FSP', 'FSP'
        Gamdias = 'Gamdias', 'Gamdias'
        Gigabyte = 'Gigabyte', 'Gigabyte'
        InterTech = 'InterTech', 'InterTech'
        KEEP = 'KEEP OUT', 'KEEP OUT'
        Kolink = 'Kolink', 'Kolink'
        Lian = 'Lian Li', 'Lian Li'
        Lindy = 'Lindy', 'Lindy'
        Makki = 'Makki', 'Makki'
        MSI = 'MSI', 'MSI'
        NZXT = 'NZXT', 'NZXT'
        Omega = 'Omega', 'Omega'
        PowerColor = 'PowerColor', 'PowerColor'
        RaptoxX = 'RaptoxX', 'RaptoxX'
        SBOX = 'SBOX', 'SBOX'
        Seasonic = 'Seasonic', 'Seasonic'
        Segotep = 'Segotep', 'Segotep'
        Sharkoon = 'Sharkoon', 'Sharkoon'
        Spire = 'Spire', 'Spire'
        Super = 'Super Flower', 'Super Flower'
        Thermaltake = 'Thermaltake', 'Thermaltake'
        TrendSonic = 'TrendSonic', 'TrendSonic'
        Xigmatek = 'Xigmatek', 'Xigmatek'
        Zalman = 'Zalman', 'Zalman'
    
    class FormFactorChoices(models.TextChoices):
        ATX = 'ATX', 'ATX'
        EPS = 'EPS', 'EPS'
        FLEX = 'Flex ATX', 'Flex ATX'
        SFX = 'SFX', 'SFX'
        TFX = 'TFX', 'TFX'
    
    class PlusRatingChoices(models.TextChoices):
        Titanium = 'Titanium', 'Titanium'
        Platinum = 'Platinum', 'Platinum'
        Gold = 'Gold', 'Gold'
        Silver = 'Siler', 'Silver'
        Bronze = 'Bronze', 'Bronze'
        Standard = 'Standard (White)', 'Standard (White)'

    manufacturer = models.CharField(
        max_length=MAX_MANUFACTURER_LEN,
        choices = ManufacturerChoices.choices,
    )

    wattage = models.PositiveSmallIntegerField(
        blank=True,
        null=True,
        validators=[
            MaxValueValidator(MAX_WATTAGE_VAL),
        ],
    )

    form_factor = models.CharField(
        blank=True,
        null=True,
        max_length=MAX_FORM_FACTOR_LEN,
        choices=FormFactorChoices.choices,
    )

    fan_size = models.PositiveSmallIntegerField(
        blank=True,
        null=True,
        validators=[
            MaxValueValidator(MAX_FAN_SIZE_VAL),
        ],
    )

    plus_rating = models.CharField(
        blank=True,
        null=True,
        max_length=MAX_PLUS_RATING_LEN,
        choices=PlusRatingChoices.choices,
    )

    height = models.PositiveSmallIntegerField(
        blank=True,
        null=True,
        validators=[
            MaxValueValidator(MAX_DIMS_VAL),
        ],
    )

    width = models.PositiveSmallIntegerField(
        blank=True,
        null=True,
        validators=[
            MaxValueValidator(MAX_DIMS_VAL),
        ],
    )

    depth = models.PositiveSmallIntegerField(
        blank=True,
        null=True,
        validators=[
            MaxValueValidator(MAX_DIMS_VAL),
        ],
    )

    warranty = models.PositiveSmallIntegerField(
        blank=True,
        null=True,
        validators=[
            MaxValueValidator(MAX_WARRANTY_VAL),
        ],
    )

    def __str__(self) -> str:
        return f'{self.manufacturer} {self.model_name} {self.wattage}W {self.plus_rating}'
