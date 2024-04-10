from django.contrib.auth import forms as auth_forms, get_user_model
from django import forms

from .models import Profile


UserModel = get_user_model()


class AppUserCreationForm(auth_forms.UserCreationForm):
    user = None

    class Meta(auth_forms.UserCreationForm.Meta):
        model = UserModel
        fields = ('email',)


class AppUserChangeForm(auth_forms.UserChangeForm):
    
    class Meta(auth_forms.UserChangeForm.Meta):
        model = UserModel


class ProfileChangeModelForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['contributions'].widget.attrs['disabled'] = 'disabled'
        self.fields['contributions'].widget.attrs['readonly'] = 'readonly'

    class Meta:

        model = Profile
        fields = [
            'first_name',
            'last_name',
            'date_of_birth',
            'profile_picture',
            'contributions',
        ]
        widgets = {
            'date_of_birth': forms.DateInput(
                attrs={
                    'type':'date',
                }
            ),
        }