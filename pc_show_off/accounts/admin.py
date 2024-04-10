from django.contrib import admin
from django.contrib.auth import get_user_model

from .models import AppUser, Profile
from .forms import AppUserChangeForm, AppUserCreationForm

# Register your models here.
UserModel = get_user_model()

@admin.register(AppUser)
class AppUserAdmin(admin.ModelAdmin):

    model = UserModel
    add_form = AppUserCreationForm
    form = AppUserChangeForm

    list_display = ('pk', 'email', 'is_staff', 'is_superuser',)
    search_fields = ('email',)
    ordering = ('pk',)

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ()}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login',)}),
    )

    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("email", "password1", "password2"),
            },
        ),
    )

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    
    list_display = (
        'user',
        'first_name',
        'last_name',
        'date_of_birth',
        'profile_picture',
        'contributions',
    )
    search_fields = (
        'first_name',
        'last_name',
    )
