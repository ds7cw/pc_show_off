from django.contrib import admin
from .models import Gpu

# Register your models here.
@admin.register(Gpu)
class GpuAdmin(admin.ModelAdmin):

    list_display = [
        'short_model_name',
        'pk',
        'manufacturer',
        'gpu_manufacturer',
        'series',
        'v_ram',
        'stream_processors',
        'memory_bus',
        'gpu_release_date',
        'is_verified',
        'contributor',
    ]

    list_filter = ['manufacturer', 'gpu_manufacturer', 'v_ram', 'short_model_name']
    empty_value_display = '-empty-'
    ordering = ['manufacturer', 'short_model_name','gpu_release_date', 'pk',]

    fieldsets = [
        [
            'Chip Manufacturer Details', {
                'fields': [
                    'manufacturer',
                    'model_name',
                    'short_model_name',
                ]
            }
        ],
        [
            'GPU Manufacturer Details', {
                'fields': [
                    'gpu_manufacturer',
                    'series',
                ]
            }
        ],
        [
            'GPU Specification', {
                'fields': [
                    'chip_architecture',
                    'v_ram',
                    'stream_processors',
                ]
            }
        ],
        [
            'Interface Specification', {
                'fields': [
                    'memory_bus',
                    'gpu_interface',
                ]
            }
        ],
        [
            'Other', {
                'fields': [
                    'recommended_psu',
                    'gpu_release_date',
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