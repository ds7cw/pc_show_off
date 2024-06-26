from django.db import models

from django.utils.translation import gettext_lazy as _
from django.contrib.auth import models as auth_models, get_user_model

from django.utils import timezone

from pc_show_off.accounts.managers import AppUserManager


# Create your models here.

class AppUser(auth_models.AbstractBaseUser, auth_models.PermissionsMixin):

    email = models.EmailField(
        _("email address"),
        unique=True,
        error_messages={
            "unique": _("A user with that email already exists."),
        },
    )

    date_joined = models.DateTimeField(_("date joined"), default=timezone.now)

    is_staff = models.BooleanField(
        default=False,
    )

    is_active = models.BooleanField(
        default=True,
    )

    USERNAME_FIELD = "email"

    objects = AppUserManager()


UserModel = get_user_model()

class Profile(models.Model):
    MAX_FIRST_NAME_LENGTH = 30
    MAX_LAST_NAME_LENGTH = 30

    first_name = models.CharField(
        max_length=MAX_FIRST_NAME_LENGTH,
        blank=True,
        null=True,
    )

    last_name = models.CharField(
        max_length=MAX_LAST_NAME_LENGTH,
        blank=True,
        null=True,
    )

    date_of_birth = models.DateField(
        blank=True,
        null=True,
    )

    profile_picture = models.URLField(
        blank=True,
        null=True,
    )

    contributions = models.PositiveIntegerField(
        blank=True,
        null=True,
        default=0,
    )

    user = models.OneToOneField(
        UserModel,
        primary_key=True,
        on_delete=models.CASCADE,
        related_name='profiles',
    )

    @property
    def full_name(self):
        if self.first_name and self.last_name:
            return f'{self.first_name} {self.last_name}'

        return self.first_name or self.last_name