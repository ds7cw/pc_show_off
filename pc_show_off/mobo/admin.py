from django.contrib import admin
from .models import Mobo

# Register your models here.
@admin.register(Mobo)
class MoboAdmin(admin.ModelAdmin):

    list_display = [
        'model_name',
        'pk',
        'manufacturer',
        'platform',
        'cpu_socket',
        'chipset',
        'atx_factor',
        'memory_type',
        'memory_slots',
        'maximum_ram',
        'gpu_interface',
        'is_verified',
        'contributor',
    ]

    list_filter = ['manufacturer', 'platform', 'chipset', 'memory_type', 'cpu_socket']
    empty_value_display = '-empty-'
    ordering = ['platform', 'manufacturer', 'memory_type', 'pk']

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
            'CPU Specifications', {
                'fields': [
                    'platform',
                    'cpu_socket',
                    'chipset',
                ]
            }
        ],
        [
            'Memory Specification', {
                'fields': [
                    'memory_type',
                    'memory_slots',
                    'maximum_ram',
                ]
            }
        ],
        [
            'Size & Interface', {
                'fields': [
                    'atx_factor',
                    'gpu_interface',
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