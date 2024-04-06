from django import forms
from .models import Ram


class BaseRamModelForm(forms.ModelForm):

    class Meta:
        model = Ram
        fields = [
            'manufacturer',
            'series',
            'model_name',
            'memory_type',
            'total_ram',
            'max_frequency',
            'default_frequency',
            'cas_latency',
            'number_of_sticks',
            'colour',
            'rgb',
            'warranty',
        ]
        labels = {
            'model_name': 'Model Name',
            'memory_type': 'Memory Type',
            'total_ram': 'Total RAM Capacity (GB)',
            'max_frequency': 'Tested Speed (MHz)',
            'default_frequency': 'Default Speed (MHz)',
            'cas_latency': 'CAS Latency',
            'number_of_sticks': 'Number of RAM Sticks',
            'rgb': 'RGB Lighting',
        }

        widgets = {
            'series': forms.TextInput(
                attrs={
                    'placeholder': 'Fury Beast',
                },
            ),
            'model_name': forms.TextInput(
                attrs={
                    'placeholder': 'KF432C16BBK2/16',
                },
            ),
        }


class CreateRamModelForm(BaseRamModelForm):

    class Meta(BaseRamModelForm.Meta):
        pass


class DeleteRamModelForm(BaseRamModelForm):
    
    class Meta(BaseRamModelForm.Meta):
        pass

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['disabled'] = 'disabled'
