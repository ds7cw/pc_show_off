from django import forms
from .models import Gpu


class BaseGpuModelForm(forms.ModelForm):

    class Meta:
        model = Gpu
        fields = [
            'manufacturer',
            'gpu_manufacturer',
            'model_name',
            'gpu_manufacturer',
            'short_model_name',
            'series',
            'chip_architecture',
            'v_ram',
            'stream_processors',
            'memory_bus',
            'gpu_interface',
            'recommended_psu',
            'gpu_release_date',
        ]
        labels = {
            'manufacturer': 'Chip Manufacturer',
            'model_name': 'Model Name',
            'gpu_manufacturer': 'GPU Manufacturer',
            'short_model_name': 'GPU Model',
            'series': 'GPU Manufacturer Series',
            'chip_architecture': 'Chip Architecture',
            'v_ram': 'Virtual Memory (GB)',
            'stream_processors': 'Stream Processors (Shaders)',
            'memory_bus': 'Memory Bus (bit)',
            'gpu_interface': 'GPU Interface',
            'recommended_psu': 'Recommended PSU (W)',
            'gpu_release_date': 'GPU Release Date',
        }

        widgets = {
            'model_name': forms.TextInput(
                attrs={
                    'placeholder': 'ZT-D40720E-10M | RX7800XT SL 16GO',
                },
            ),
            'short_model_name': forms.TextInput(
                attrs={
                    'placeholder': '4070 Super | RX 7800 XT',
                },
            ),
            'series': forms.TextInput(
                attrs={
                    'placeholder': 'Twin Edge | Steel Legend',
                },
            ),
            'chip_architecture': forms.TextInput(
                attrs={
                    'placeholder': 'AD104 | Navi 32',
                },
            ),
            'gpu_release_date': forms.DateInput(
                attrs={
                    'type':'date',
                }
            ),
        }


class CreateGpuModelForm(BaseGpuModelForm):

    class Meta(BaseGpuModelForm.Meta):
        pass


class DeleteGpuModelForm(BaseGpuModelForm):
    
    class Meta(BaseGpuModelForm.Meta):
        pass

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['disabled'] = 'disabled'
