from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from pc_show_off.common.models import ComputerComponent


# Create your models here.
class Case(ComputerComponent):
    
    MAX_MANUFACTURER_LEN = 15
    MAX_SERIES_LEN = 35
    MAX_TOWER_SIZE_LEN = 12
    MAX_FORM_FACTOR_LEN = 15

    
    MAX_WIDTH_VAL = 1000
    MAX_HEIGHT_VAL = 1000
    MAX_DEPTH_VAL = 1000

    MAX_PSU_LEN_VAL = 500
    MAX_GPU_LEN_VAL = 500
    
    MAX_FANS_LEN = 2
    MAX_COLOUR_LEN = 8
    

    class ManufacturerChoices(models.TextChoices):
        FirstPlayer = '1stPlayer', '1stPlayer'
        AeroCool = 'AeroCool', 'AeroCool'
        Antec = 'Antec', 'Antec'
        Asus = 'Asus', 'Asus'
        bequiet = 'be quiet!', 'be quiet!'
        BitFenix = 'BitFenix', 'BitFenix'
        Chieftec = 'Chieftec', 'Chieftec'
        CoolerMaster = 'CoolerMaster', 'CoolerMaster'
        Corsair = 'Corsair', 'Corsair'
        CougarGaming = 'Cougar Gaming', 'Cougar Gaming'
        DeepCool = 'DeepCool', 'DeepCool'
        Endorfy = 'Endorfy', 'Endorfy'
        FractalDesign = 'Fractal Design', 'Fractal Design'
        FSP = 'FSP', 'FSP'
        Fury = 'Fury', 'Fury'
        Gamdias = 'Gamdias', 'Gamdias'
        Genesis = 'Genesis', 'Genesis'
        GenesysGroup = 'Genesys Group', 'Genesys Group'
        Gigabyte = 'Gigabyte', 'Gigabyte'
        HYTE = 'HYTE', 'HYTE'
        InWin = 'In Win', 'In Win'
        InterTech = 'Inter-Tech', 'Inter-Tech'
        Jonsbo = 'Jonsbo', 'Jonsbo'
        Kolink = 'Kolink', 'Kolink'
        LCPower = 'LC Power', 'LC Power'
        LianLi = 'Lian Li', 'Lian Li'
        Makki = 'Makki', 'Makki'
        Modecom = 'Modecom', 'Modecom'
        Montech = 'Montech', 'Montech'
        MSI = 'MSI', 'MSI'
        NZXT = 'NZXT', 'NZXT'
        Omega = 'Omega', 'Omega'
        Phanteks = 'Phanteks', 'Phanteks'
        Powercase = 'Powercase', 'Powercase'
        Razer = 'Razer', 'Razer'
        Redragon = 'Redragon', 'Redragon'
        Seasonic = 'Seasonic', 'Seasonic'
        Segotep = 'Segotep', 'Segotep'
        Sharkoon = 'Sharkoon', 'Sharkoon'
        SilverStone = 'SilverStone', 'SilverStone'
        Spire = 'Spire', 'Spire'
        Thermaltake = 'Thermaltake', 'Thermaltake'
        TrendSonic = 'TrendSonic', 'TrendSonic'
        Xigmatek = 'Xigmatek', 'Xigmatek'
        Zalman = 'Zalman', 'Zalman'

    class TowerSizeChoices(models.TextChoices):
        
        MicroTower = 'Micro Tower', 'Micro Tower'
        MiniTower = 'Mini Tower', 'Mini Tower'
        MidTower = 'Mid Tower', 'Mid Tower'
        FullTower = 'Full Tower', 'Full Tower'
        SuperTower = 'Super Tower', 'Super Tower'

    class FormFactorChoices(models.TextChoices):
        ATX = 'ATX', 'ATX'
        E = 'E-ATX', 'E-ATX'
        MICROATX = 'Micro-ATX', 'Micro-ATX'
        MICROITX = 'Micro-ITX', 'Micro-ITX'
        MINIATX = 'Mini-ATX', 'Mini-ATX'
        MINIDTX = 'Mini-DTX', 'Mini-DTX'
        MINIITX = 'Mini-ITX', 'Mini-ITX'
        DTX = 'DTX', 'DTX'
        ITX = 'ITX', 'ITX'
        XL = 'XL-ATX', 'XL-ATX'
    
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
    
    class FanChoices(models.TextChoices):
        ZERO = '0', '0'
        ONE = '1', '1'
        TWO = '2', '2'
        THREE = '3', '3'



    manufacturer = models.CharField(
        max_length=MAX_MANUFACTURER_LEN,
        choices = ManufacturerChoices.choices,
    )
    
    series = models.CharField(
        blank=True,
        null=True,
        max_length=MAX_SERIES_LEN,
    )

    tower_size = models.CharField(
        blank=True,
        null=True,
        max_length=MAX_TOWER_SIZE_LEN,
        choices=TowerSizeChoices.choices,
    )

    form_factor = models.CharField(
        blank=True,
        null=True,
        max_length=MAX_FORM_FACTOR_LEN,
        choices=FormFactorChoices.choices,
    )

    width = models.PositiveSmallIntegerField(
        blank=True,
        null=True,
        validators=[
            MaxValueValidator(MAX_WIDTH_VAL),
        ],
    )

    height = models.PositiveSmallIntegerField(
        blank=True,
        null=True,
        validators=[
            MaxValueValidator(MAX_HEIGHT_VAL),
        ],
    )
    
    depth = models.PositiveSmallIntegerField(
        blank=True,
        null=True,
        validators=[
            MaxValueValidator(MAX_DEPTH_VAL),
        ],
    )

    psu_max_len = models.PositiveSmallIntegerField(
        blank=True,
        null=True,
        validators=[
            MaxValueValidator(MAX_PSU_LEN_VAL),
        ],
    )

    gpu_max_len = models.PositiveSmallIntegerField(
        blank=True,
        null=True,
        validators=[
            MaxValueValidator(MAX_GPU_LEN_VAL),
        ],
    )

    front_fans = models.CharField(
        blank=True,
        null=True,
        max_length=MAX_FANS_LEN,
        choices=FanChoices.choices,
        default=FanChoices.ZERO,
    )

    top_fans = models.CharField(
        blank=True,
        null=True,
        max_length=MAX_FANS_LEN,
        choices=FanChoices.choices,
        default=FanChoices.ZERO,
    )

    bottom_fans = models.CharField(
        blank=True,
        null=True,
        max_length=MAX_FANS_LEN,
        choices=FanChoices.choices,
        default=FanChoices.ZERO,
    )

    rear_fans = models.CharField(
        blank=True,
        null=True,
        max_length=MAX_FANS_LEN,
        choices=FanChoices.choices,
        default=FanChoices.ONE,
    )

    colour = models.CharField(
        blank=True,
        null=True,
        max_length=MAX_COLOUR_LEN,
        choices=ColourChoices.choices,
    )