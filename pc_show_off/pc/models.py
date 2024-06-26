from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator, MinValueValidator

from pc_show_off.case.models import Case
from pc_show_off.cpu.models import Cpu
from pc_show_off.gpu.models import Gpu
from pc_show_off.mobo.models import Mobo
from pc_show_off.psu.models import Psu
from pc_show_off.ram.models import Ram
from pc_show_off.storage.models import Storage


# Create your models here.
UserModel = get_user_model()

class Pc(models.Model):
    
    MAX_PC_NAME_LEN = 40
    MAX_DESCRIPTION_LEN = 500

    pc_name = models.CharField(unique=True, max_length=MAX_PC_NAME_LEN)
    owner = models.ForeignKey(UserModel, on_delete=models.DO_NOTHING, related_name='computers')

    cpu_part = models.ForeignKey(Cpu, on_delete=models.DO_NOTHING, related_name='computers')
    gpu_part = models.ForeignKey(Gpu, on_delete=models.DO_NOTHING, related_name='computers')
    mobo_part = models.ForeignKey(Mobo, on_delete=models.DO_NOTHING, related_name='computers')
    ram_part = models.ForeignKey(Ram, on_delete=models.DO_NOTHING, related_name='computers')
    psu_part = models.ForeignKey(Psu, on_delete=models.DO_NOTHING, related_name='computers')
    storage_part = models.ForeignKey(Storage, on_delete=models.DO_NOTHING, related_name='computers')
    case_part = models.ForeignKey(Case, on_delete=models.DO_NOTHING, related_name='computers')

    description = models.TextField(max_length=MAX_DESCRIPTION_LEN, null=True, blank=True)
    approx_cost = models.DecimalField(blank=True, null=True, max_digits=7, decimal_places=2,)

    def __str__(self) -> str:
        return self.pc_name


class PcRating(models.Model):

    MAX_RATING_VAL = 5
    ONE = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5

    RATING_CHOICES = (
        (ONE,'1'),
        (TWO,'2'),
        (THREE,'3'),
        (FOUR,'4'),
        (FIVE,'5'),
    )

    rating_value = models.PositiveSmallIntegerField(
        blank=True,
        null=True,
        validators=[
            MaxValueValidator(MAX_RATING_VAL)
        ],
        choices=RATING_CHOICES,
    )

    pc = models.ForeignKey(Pc, on_delete=models.CASCADE, related_name='ratings')

    reviewer = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name='ratings')


class PcComment(models.Model):

    MAX_BODY_LEN = 250

    author = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name='comments')
    
    pc = models.ForeignKey(Pc, on_delete=models.CASCADE, related_name='comments')

    date_of_creation = models.DateTimeField(auto_now_add=True)

    body = models.TextField(max_length=MAX_BODY_LEN)
