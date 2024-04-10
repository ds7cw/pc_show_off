from django import forms
from .models import Mobo


class BaseMoboModelForm(forms.ModelForm):

    class Meta:

        model = Mobo
        fields = [
            'manufacturer',
            'model_name',
            'platform',
            'cpu_socket',
            'chipset',
            'series',
            'atx_factor',
            'memory_type',
            'memory_slots',
            'maximum_ram',
            'gpu_interface',
        ]
        labels = {
            'model_name': 'Model Name',
            'cpu_socket': 'CPU Socket',
            'atx_factor': 'Form Factor',
            'memory_type': 'Memory Type',
            'memory_slots': 'Memory Slots',
            'maximum_ram': 'Maximum RAM (GB)',
            'gpu_interface': 'GPU Interface',
        }

        widgets = {
            'model_name': forms.TextInput(
                attrs={
                    'placeholder': 'B550 AORUS ELITE AX V2 (rev. 1.4)',
                },
            ),
            'cpu_socket': forms.TextInput(
                attrs={
                    'placeholder': 'AM4',
                },
            ),
            'chipset': forms.TextInput(
                attrs={
                    'placeholder': 'B550',
                },
            ),
            'series': forms.TextInput(
                attrs={
                    'placeholder': 'AORUS',
                },
            ),
            'max_ram': forms.NumberInput(
                attrs={
                    'placeholder': '128',
                },
            ),
        }


class CreateMoboModelForm(BaseMoboModelForm):

    class Meta(BaseMoboModelForm.Meta):
        pass


class DeleteMoboModelForm(BaseMoboModelForm):
    
    class Meta(BaseMoboModelForm.Meta):
        pass

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['disabled'] = 'disabled'
