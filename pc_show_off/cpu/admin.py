from django.contrib import admin
from .models import Cpu

# Register your models here.
@admin.register(Cpu)
class CpuAdmin(admin.ModelAdmin):

    list_display = [
        'model_name',
        'pk',
        'manufacturer',
        'cpu_architecture',
        'cpu_socket',
        'total_cores',
        'p_core_base_clock',
        'p_core_boost_clock',
        'cpu_level_3_cache',
        'cpu_release_date',
        'is_verified',
        'contributor',
    ]

    list_filter = ['manufacturer', 'cpu_socket', 'total_cores',]
    empty_value_display = '-empty-'
    ordering = ['manufacturer', 'cpu_release_date', 'pk',]

    fieldsets = [
        [
            'Essentials', {
                'fields': [
                    'manufacturer',
                    'model_name',
                    'cpu_architecture',
                ]
            }
        ],
        [
            'CPU Specifications', {
                'fields': [
                    'cpu_socket',
                    'total_cores',
                    'p_core_base_clock',
                    'p_core_boost_clock',
                    'cpu_level_3_cache',
                ]
            }
        ],
        [
            'Supplemental Information', {
                'fields': [
                  'cpu_release_date'
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
