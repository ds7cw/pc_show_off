from django.contrib import admin
from .models import Pc, PcRating, PcComment

# Register your models here.
@admin.register(Pc)
class PcAdmin(admin.ModelAdmin):

    list_display = [
        'pc_name',
        'pk',
        'cpu_part',
        'gpu_part',
        'mobo_part',
        'ram_part',
        'psu_part',
        'storage_part',
        'case_part',
        'approx_cost',
        'owner',
    ]

    list_filter = ['owner',]
    empty_value_display = '-empty-'
    ordering = ['owner', 'pc_name','approx_cost', 'pk']

    fieldsets = [
        [
            'Owner Details & PC Name', {
                'fields': [
                    'owner',
                    'pc_name',
                ]
            }
        ],
        [
            'Hardware Components', {
                'fields': [
                    'cpu_part',
                    'gpu_part',
                    'mobo_part',
                    'ram_part',
                    'psu_part',
                    'storage_part',
                    'case_part',
                ]
            }
        ],
        [
            'Description & Cost', {
                'fields': [
                    'description',
                    'approx_cost',
                ]
            }
        ],
    ]


@admin.register(PcRating)
class PcRatingAdmin(admin.ModelAdmin):

    list_display = [
        'pk',
        'rating_value',
        'pc',
        'reviewer',
    ]

    list_filter = [
        'pc',
        'reviewer',
    ]

@admin.register(PcComment)
class PcCommentAdmin(admin.ModelAdmin):

    list_display = [
        'pk',
        'author',
        'pc',
        'date_of_creation',
        'body',
    ]

    list_filter = [
        'pc',
        'author',
    ]
    
    ordering = ['-date_of_creation']
    