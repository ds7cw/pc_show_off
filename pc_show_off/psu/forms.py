from django import forms
from .models import Psu


class CreatePsuModelForm(forms.ModelForm):

    class Meta:

        model = Psu
        fields = [
            'manufacturer',
            'model_name',
            'wattage',
            'form_factor',
            'fan_size',
            'plus_rating',
            'height',
            'width',
            'depth',
            'warranty',
        ]
        labels = {
            'model_name': 'Model Name',
            'wattage': 'Wattage (W)',
            'form_factor': 'Form Factor',
            'fan_size': 'Fan Size (mm)',
            'plus_rating': '80 Plus Rating',
            'height': 'Height (mm)',
            'width': 'Width (mm)',
            'depth': 'Depth (mm)',
            'warranty': 'Warranty (Yrs)',
        }

        widgets = {
            'model_name': forms.TextInput(
                attrs={
                    'placeholder': 'RM850e',
                },
            ),
        }


class DeletePsuModelForm(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['disabled'] = 'disabled'
    class Meta:

        model = Psu
        fields = [
            'manufacturer',
            'model_name',
            'wattage',
            'form_factor',
            'fan_size',
            'plus_rating',
            'height',
            'width',
            'depth',
            'warranty',
        ]
        labels = {
            'model_name': 'Model Name',
            'wattage': 'Wattage (W)',
            'form_factor': 'Form Factor',
            'fan_size': 'Fan Size (mm)',
            'plus_rating': '80 Plus Rating',
            'height': 'Height (mm)',
            'width': 'Width (mm)',
            'depth': 'Depth (mm)',
            'warranty': 'Warranty (Yrs)',
        }
