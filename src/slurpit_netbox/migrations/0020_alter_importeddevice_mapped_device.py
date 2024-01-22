# Generated by Django 4.2.8 on 2024-01-22 19:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dcim', '0185_gfk_indexes'),
        ('slurpit_netbox', '0019_alter_importeddevice_mapped_device'),
    ]

    operations = [
        migrations.AlterField(
            model_name='importeddevice',
            name='mapped_device',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='dcim.device'),
        ),
    ]
