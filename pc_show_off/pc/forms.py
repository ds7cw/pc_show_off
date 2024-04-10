from django import forms
from .models import Pc, Cpu, Gpu, Mobo, Ram, Psu, Storage, Case, PcRating


class BasePcModelForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(BasePcModelForm, self).__init__(*args, **kwargs)
        self.fields['cpu_part'].queryset = Cpu.objects.filter(is_verified=True).order_by('manufacturer', 'model_name')
        self.fields['gpu_part'].queryset = Gpu.objects.filter(is_verified=True).order_by('manufacturer', 'short_model_name')
        self.fields['mobo_part'].queryset = Mobo.objects.filter(is_verified=True).order_by('platform', 'cpu_socket')
        self.fields['ram_part'].queryset = Ram.objects.filter(is_verified=True).order_by('total_ram', 'memory_type')
        self.fields['psu_part'].queryset = Psu.objects.filter(is_verified=True).order_by('wattage', 'manufacturer')
        self.fields['storage_part'].queryset = Storage.objects.filter(is_verified=True).order_by('total_storage', 'model_name')
        self.fields['case_part'].queryset = Case.objects.filter(is_verified=True).order_by('manufacturer', 'series')
    
    class Meta:
        model = Pc
        fields = [
            'pc_name',
            'cpu_part',
            'gpu_part',
            'mobo_part',
            'ram_part',
            'psu_part',
            'storage_part',
            'case_part',
            'description',
            'approx_cost',
        ]
        labels = {
            'pc_name': 'PC Name',
            'cpu_part': 'Processor (CPU)',
            'gpu_part': 'Graphics Card (GPU)',
            'mobo_part': 'Motherboard',
            'ram_part': 'RAM Modules',
            'psu_part': 'Power Supply (PSU)',
            'storage_part': 'Internal SSD Storage',
            'case_part': 'PC Case',
            'approx_cost': 'Approximate Cost (USD)',
        }

        widgets = {
            'pc_name': forms.TextInput(
                attrs={
                    'placeholder': 'HAL 9000',
                },
            ),
            'Description': forms.TextInput(
                attrs={
                    'placeholder': 'Anything else you would like to share about your rig?',
                },
            ),
        }


class CreatePcModelForm(BasePcModelForm):

    class Meta(BasePcModelForm.Meta):
        pass


class DeletePcModelForm(BasePcModelForm):
    
    class Meta(BasePcModelForm.Meta):
        pass

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['disabled'] = 'disabled'


class PcRatingModelForm(forms.ModelForm):
    class Meta:
        model = PcRating
        fields = ['rating_value']
        labels = {'rating_value': 'Rating',}
