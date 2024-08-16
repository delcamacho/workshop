# Generated by Django 5.0.6 on 2024-08-16 01:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("slurpit_netbox", "0017_slurpitvlan_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="slurpitvlan",
            name="ignore_description",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="slurpitvlan",
            name="ignore_group",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="slurpitvlan",
            name="ignore_role",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="slurpitvlan",
            name="ignore_site",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="slurpitvlan",
            name="ignore_status",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="slurpitvlan",
            name="ignore_tenant",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="slurpitvlan",
            name="ignore_vid",
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name="slurpitvlan",
            name="group",
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
        migrations.AlterField(
            model_name="slurpitvlan",
            name="name",
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
    ]
