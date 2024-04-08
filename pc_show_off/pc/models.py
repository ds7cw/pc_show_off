from django.db import models
from django.contrib.auth import get_user_model

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
