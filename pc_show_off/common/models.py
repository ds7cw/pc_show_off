from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
UserModel = get_user_model()

class ComputerComponent(models.Model):

    class Meta:
        abstract = True

    class ManufacturerChoices(models.TextChoices):
        pass

    manufacturer = models.CharField(
        max_length=15,
        choices = ManufacturerChoices.choices,
    )

    model_name = models.CharField(
        max_length=50,
        unique=True,
    )

    is_verified = models.BooleanField(
        default=False,
    )

    contributor = models.ForeignKey(
        UserModel,
        on_delete=models.DO_NOTHING,
    )
