# Generated by Django 5.0.6 on 2024-08-05 01:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("slurpit_netbox", "0013_slurpitinitipaddress_ignore_status"),
    ]

    operations = [
        migrations.AddField(
            model_name="slurpitinitipaddress",
            name="ignore_description",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="slurpitinitipaddress",
            name="ignore_role",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="slurpitinitipaddress",
            name="ignore_tenant",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="slurpitinitipaddress",
            name="ignore_vrf",
            field=models.BooleanField(default=False),
        ),
    ]
