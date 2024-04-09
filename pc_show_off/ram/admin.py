from django.contrib import admin
from .models import Ram

# Register your models here.
@admin.register(Ram)
class RamAdmin(admin.ModelAdmin):

    list_display = [
        'model_name',
        'pk',
        'manufacturer',
        'series',
        'memory_type',
        'total_ram',
        'max_frequency',
        'cas_latency',
        'number_of_sticks',
        'is_verified',
        'contributor',
    ]

    list_filter = ['manufacturer', 'memory_type', 'max_frequency', 'total_ram',]
    empty_value_display = '-empty-'
    ordering = ['memory_type', 'max_frequency', 'manufacturer', 'pk',]

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
            'RAM Specification', {
                'fields': [
                    'total_ram',
                    'max_frequency',
                    'default_frequency',
                    'cas_latency',
                    'number_of_sticks',
                ]
            }
        ],
        [
            'Aesthetics', {
                'fields': [
                  'colour',
                  'rgb',
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
