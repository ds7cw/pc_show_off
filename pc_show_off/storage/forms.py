from django import forms
from .models import Storage


class BaseStorageModelForm(forms.ModelForm):

    class Meta:
        model = Storage
        fields = [
            'manufacturer',
            'series',
            'model_name',
            'form_factor',
            'interface',
            'pcie_interface',
            'total_storage',
            'read_speed',
            'write_speed',
            'length',
        ]
        labels = {
            'model_name': 'Model Name',
            'form_factor': 'Form Factor',
            'pcie_interface': 'PCIe Interface',
            'total_storage': 'Capacity (GB)',
            'read_speed': 'Sequential Read (MB/s)',
            'write_speed': 'Sequential Write (MB/s)',
            'length': 'Component Length (mm)',
        }

        widgets = {
            'series': forms.TextInput(
                attrs={
                    'placeholder': '990 PRO',
                },
            ),
            'model_name': forms.TextInput(
                attrs={
                    'placeholder': 'MZ-V9P1T0BW',
                },
            ),
        }


class CreateStorageModelForm(BaseStorageModelForm):

    class Meta(BaseStorageModelForm.Meta):
        pass


class DeleteStorageModelForm(BaseStorageModelForm):
    
    class Meta(BaseStorageModelForm.Meta):
        pass

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['disabled'] = 'disabled'
