# Generated by Django 5.0.2 on 2024-04-06 08:54

import django.core.validators
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Gpu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model_name', models.CharField(max_length=50, unique=True)),
                ('is_verified', models.BooleanField(default=False)),
                ('manufacturer', models.CharField(choices=[('AMD', 'AMD'), ('Intel', 'Intel'), ('NVIDIA', 'NVIDIA')], max_length=8)),
                ('gpu_manufacturer', models.CharField(choices=[('Acer', 'Acer'), ('AMD', 'AMD'), ('ASRock', 'ASRock'), ('Biostar', 'Biostar'), ('EVGA', 'EVGA'), ('Gainward', 'Gainward'), ('Gigabyte', 'Gigabyte'), ('Inno3D', 'Inno3D'), ('Intel', 'Intel'), ('KFA2', 'KFA2'), ('MSI', 'MSI'), ('NVIDIA', 'NVIDIA'), ('Palit', 'Palit'), ('PNY', 'PNY'), ('PowerColor', 'PowerColor'), ('Saphire', 'Saphire'), ('XFX', 'XFX'), ('ZOTAC', 'ZOTAC')], max_length=10)),
                ('short_model_name', models.CharField(blank=True, max_length=25, null=True)),
                ('series', models.CharField(blank=True, max_length=35, null=True)),
                ('chip_architecture', models.CharField(blank=True, max_length=35, null=True)),
                ('v_ram', models.PositiveSmallIntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(48)])),
                ('stream_processors', models.PositiveIntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(50000)])),
                ('memory_bus', models.PositiveSmallIntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(8192)])),
                ('gpu_interface', models.CharField(blank=True, choices=[('PCIe 2.0', 'PCIe 2.0'), ('PCIe 3.0', 'PCIe 3.0'), ('PCIe 4.0', 'PCIe 4.0'), ('PCIe 5.0', 'PCIe 5.0')], max_length=8, null=True)),
                ('recommended_psu', models.PositiveSmallIntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(300), django.core.validators.MaxValueValidator(2050)])),
                ('gpu_release_date', models.DateField(blank=True, null=True)),
                ('contributor', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
