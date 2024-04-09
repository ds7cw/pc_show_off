from django.contrib import admin
from .models import Storage

# Register your models here.
@admin.register(Storage)
class StorageAdmin(admin.ModelAdmin):

    list_display = [
        'model_name',
        'pk',
        'manufacturer',
        'series',
        'form_factor',
        'interface',
        'pcie_interface',
        'total_storage',
        'is_verified',
        'contributor',
    ]

    list_filter = ['manufacturer', 'form_factor', 'interface', 'total_storage',]
    empty_value_display = '-empty-'
    ordering = ['total_storage', 'form_factor', 'manufacturer', 'pk',]

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
            'Interfaces', {
                'fields': [
                    'form_factor',
                    'interface',
                    'pcie_interface',
                ]
            }
        ],
        [
            'Storage Specification', {
                'fields': [
                  'total_storage',
                  'read_speed',
                  'write_speed',
                ]
            }
        ],
        [
            'Dimensions', {
                'fields': [
                    'length',
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
