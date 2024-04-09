from django.contrib import admin
from .models import Psu

# Register your models here.
@admin.register(Psu)
class PsuAdmin(admin.ModelAdmin):

    list_display = [
        'model_name',
        'pk',
        'manufacturer',
        'wattage',
        'form_factor',
        'fan_size',
        'plus_rating',
        'height',
        'width',
        'depth',
        'warranty',
        'is_verified',
        'contributor',
    ]

    list_filter = ['manufacturer', 'wattage', 'plus_rating',]
    empty_value_display = '-empty-'
    ordering = ['wattage', 'manufacturer', 'pk',]

    fieldsets = [
        [
            'Manufacturer Details', {
                'fields': [
                    'manufacturer',
                    'model_name',
                ]
            }
        ],
        [
            'Power Specification', {
                'fields': [
                    'wattage',
                    'plus_rating',
                ]
            }
        ],
        [
            'Dimensions', {
                'fields': [
                  'form_factor',
                  'height',
                  'width',
                  'depth',
                  'fan_size',
                ]
            }
        ],
        [
            'Other', {
                'fields': [
                    'warranty',
                ]
            }
        ],
        [
            'Verification & Ownership', {
                'fields': [
                    'is_verified',
                    'contributor',
                ]
            }
        ],
    ]
