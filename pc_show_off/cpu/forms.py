from django import forms
from .models import Cpu


class CreateCpuModelForm(forms.ModelForm):

    class Meta:

        model = Cpu
        fields = [
            'manufacturer',
            'model_name',
            'cpu_architecture',
            'cpu_socket',
            'total_cores',
            'p_core_base_clock',
            'p_core_boost_clock',
            'cpu_level_3_cache',
            'cpu_release_date',
        ]
        labels = {
            'cpu_level_3_cache': 'L3 Cache (MB)',
            'p_core_base_clock': 'P Cores Base Clock (GHz)',
            'p_core_boost_clock': 'P Cores Boost Clock (GHz)',
        }

        widgets = {
            'model_name': forms.TextInput(
                attrs={
                    'placeholder': 'Core i7-13700K | Ryzen 7 7800X3D',
                },
            ),
            'cpu_architecture': forms.TextInput(
                attrs={
                    'placeholder': 'Raptor Lake-S | Raphael',
                },
            ),
            'cpu_socket': forms.TextInput(
                attrs={
                    'placeholder': '1700 | AM5',
                },
            ),
            'total_cores': forms.NumberInput(
                attrs={
                    'placeholder': '16 | 8',
                },
            ),
            'cpu_level_3_cache': forms.NumberInput(
                attrs={
                    'placeholder': '30 | 96',
                },
            ),
            'p_core_base_clock': forms.NumberInput(
                attrs={
                    'placeholder': '3.4 | 4.2',
                    'step': 0.1,
                },
            ),
            'p_core_boost_clock': forms.NumberInput(
                attrs={
                    'placeholder': '5.4 | 5',
                    'step': 0.1,
                },
            ),
            'cpu_release_date': forms.DateInput(
                attrs={
                    'type':'date',
                }
            ),
        }