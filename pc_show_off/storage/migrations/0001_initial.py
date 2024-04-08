# Generated by Django 5.0.2 on 2024-04-06 20:25

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
            name='Storage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model_name', models.CharField(max_length=50, unique=True)),
                ('is_verified', models.BooleanField(default=False)),
                ('manufacturer', models.CharField(choices=[('ADATA', 'ADATA'), ('Apacer', 'Apacer'), ('Corsair', 'Corsair'), ('Crucial', 'Crucial'), ('Gigabyte', 'Gigabyte'), ('HP', 'HP'), ('Intel', 'Intel'), ('Kingston', 'Kingston'), ('Lenovo', 'Lenovo'), ('Lexar', 'Lexar'), ('Micron', 'Micron'), ('Patriot', 'Patriot'), ('Samsung', 'Samsung'), ('SanDisk', 'SanDisk'), ('Seagate', 'Seagate'), ('Silicon Power', 'Silicon Power'), ('SK Hynix', 'SK Hynix'), ('TeamGroup', 'TeamGroup'), ('Thermaltake', 'Thermaltake'), ('Transcend', 'Transcend'), ('WD', 'WD')], max_length=15)),
                ('series', models.CharField(blank=True, max_length=35, null=True)),
                ('form_factor', models.CharField(blank=True, choices=[('M.2 (2280)', 'M.2 (2280)'), ('M.2 (2242)', 'M.2 (2242)'), ('M.2 (2230)', 'M.2 (2230)'), ('M.2 (2260)', 'M.2 (2260)'), ('2.5"', '2.5"')], max_length=10, null=True)),
                ('interface', models.CharField(blank=True, choices=[('NVMe', 'NVMe'), ('SATA 3', 'SATA 3')], max_length=8, null=True)),
                ('pcie_interface', models.CharField(blank=True, choices=[('N/A', 'N/A'), ('PCIe 3.0', 'PCIe 3.0'), ('PCIe 4.0', 'PCIe 4.0'), ('PCIe 5.0', 'PCIe 5.0')], max_length=8, null=True)),
                ('total_storage', models.PositiveSmallIntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(8192)])),
                ('read_speed', models.PositiveSmallIntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(30000)])),
                ('write_speed', models.PositiveSmallIntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(30000)])),
                ('length', models.PositiveSmallIntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(200)])),
                ('contributor', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]