from django import forms
from .models import Case


class BaseCaseModelForm(forms.ModelForm):

    class Meta:
        model = Case
        fields = [
            'manufacturer',
            'series',
            'model_name',
            'tower_size',
            'form_factor',
            'width',
            'height',
            'depth',
            'psu_max_len',
            'gpu_max_len',
            'front_fans',
            'top_fans',
            'bottom_fans',
            'rear_fans',
            'colour',
        ]
        labels = {
            'model_name': 'Model Name',
            'tower_size': 'Tower Size',
            'form_factor': 'Form Factor',
            'width': 'Width (mm)',
            'height': 'Height (mm)',
            'depth': 'Depth (mm)',
            'psu_max_len': 'Maximum PSU Length (mm)',
            'gpu_max_len': 'Maximum GPU Length (mm)',
            'front_fans': 'Number of Front Fans',
            'top_fans': 'Number of Top Fans',
            'bottom_fans': 'Number of Bottom Fans',
            'rear_fans': 'Number of Rear Fans',
            'colour': 'Case Colour',
        }

        widgets = {
            'series': forms.TextInput(
                attrs={
                    'placeholder': 'MasterBox 500',
                },
            ),
            'model_name': forms.TextInput(
                attrs={
                    'placeholder': 'MB500-KGNN-S00-B',
                },
            ),
        }


class CreateCaseModelForm(BaseCaseModelForm):

    class Meta(BaseCaseModelForm.Meta):
        pass


class DeleteCaseModelForm(BaseCaseModelForm):
    
    class Meta(BaseCaseModelForm.Meta):
        pass

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['disabled'] = 'disabled'
