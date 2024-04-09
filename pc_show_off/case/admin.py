from django.contrib import admin
from .models import Case

# Register your models here.
@admin.register(Case)
class CaseAdmin(admin.ModelAdmin):

    list_display = [
        'model_name',
        'pk',
        'manufacturer',
        'series',
        'tower_size',
        'form_factor',
        'width',
        'height',
        'depth',
        'colour',
        'is_verified',
        'contributor',
    ]

    list_filter = ['manufacturer', 'form_factor', 'tower_size', 'colour',]
    empty_value_display = '-empty-'
    ordering = ['form_factor', 'tower_size', 'manufacturer', 'pk',]

    fieldsets = [
        [
            'Manufacturer Details', {
                'fields': [
                    'manufacturer',
                    'series',
                    'model_name',
                ]
            }
        ],
        [
            'Dimensions', {
                'fields': [
                    'tower_size',
                    'form_factor',
                    'width',
                    'height',
                    'depth',
                ]
            }
        ],
        [
            'Internal Clearance', {
                'fields': [
                    'psu_max_len',
                    'gpu_max_len',
                ]
            }
        ],
        [
            'Fan Configuration', {
                'fields': [
                    'front_fans',
                    'top_fans',
                    'bottom_fans',
                    'rear_fans',
                ]
            }
        ],
        [
            'Aesthetics', {
                'fields': [
                    'colour',
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
