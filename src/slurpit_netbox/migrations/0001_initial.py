# Generated by Django 4.2.8 on 2024-01-23 20:37

from django.db import migrations, models
import django.db.models.deletion
import taggit.managers
import utilities.json


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('dcim', '0185_gfk_indexes'),
        ('extras', '0105_customfield_min_max_values'),
    ]

    operations = [
        migrations.CreateModel(
            name='SlurpitLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False)),
                ('log_time', models.DateTimeField(auto_now=True)),
                ('level', models.CharField(default='default', editable=False, max_length=100)),
                ('category', models.CharField(default='init', editable=False, max_length=50)),
                ('message', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='SlurpitStagedDevice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('last_updated', models.DateTimeField(auto_now=True, null=True)),
                ('custom_field_data', models.JSONField(blank=True, default=dict, encoder=utilities.json.CustomFieldJSONEncoder)),
                ('slurpit_id', models.IntegerField(unique=True)),
                ('disabled', models.BooleanField(default=False)),
                ('hostname', models.CharField(max_length=255, unique=True)),
                ('fqdn', models.CharField(max_length=128)),
                ('device_os', models.CharField(max_length=128)),
                ('device_type', models.CharField(max_length=255)),
                ('brand', models.CharField(max_length=255)),
                ('createddate', models.DateTimeField()),
                ('changeddate', models.DateTimeField(null=True)),
                ('tags', taggit.managers.TaggableManager(through='extras.TaggedItem', to='extras.Tag')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SlurpitSource',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('last_updated', models.DateTimeField(auto_now=True, null=True)),
                ('custom_field_data', models.JSONField(blank=True, default=dict, encoder=utilities.json.CustomFieldJSONEncoder)),
                ('description', models.CharField(blank=True, max_length=200)),
                ('comments', models.TextField(blank=True)),
                ('name', models.CharField(max_length=100, unique=True)),
                ('url', models.CharField(max_length=200)),
                ('status', models.CharField(default='new', editable=False, max_length=50)),
                ('parameters', models.JSONField(blank=True, null=True)),
                ('last_synced', models.DateTimeField(blank=True, editable=False, null=True)),
                ('tags', taggit.managers.TaggableManager(through='extras.TaggedItem', to='extras.Tag')),
            ],
            options={
                'verbose_name': 'Data source',
                'verbose_name_plural': 'Data sources',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='SlurpitSnapshot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('last_updated', models.DateTimeField(auto_now=True, null=True)),
                ('custom_field_data', models.JSONField(blank=True, default=dict, encoder=utilities.json.CustomFieldJSONEncoder)),
                ('description', models.CharField(blank=True, max_length=200)),
                ('comments', models.TextField(blank=True)),
                ('hostname', models.TextField(max_length=255, null=True)),
                ('plan_id', models.TextField(max_length=10, null=True)),
                ('content', models.JSONField()),
                ('tags', taggit.managers.TaggableManager(through='extras.TaggedItem', to='extras.Tag')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SlurpitSetting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('last_updated', models.DateTimeField(auto_now=True, null=True)),
                ('custom_field_data', models.JSONField(blank=True, default=dict, encoder=utilities.json.CustomFieldJSONEncoder)),
                ('description', models.CharField(blank=True, max_length=200)),
                ('comments', models.TextField(blank=True)),
                ('server_url', models.CharField(max_length=200)),
                ('api_key', models.CharField(editable=False, max_length=50)),
                ('last_synced', models.DateTimeField(auto_now=True, null=True)),
                ('connection_status', models.CharField(default='', editable=False, max_length=50, null=True)),
                ('push_api_key', models.CharField(editable=False, max_length=200, null=True)),
                ('appliance_type', models.CharField(blank=True, max_length=50)),
                ('tags', taggit.managers.TaggableManager(through='extras.TaggedItem', to='extras.Tag')),
            ],
            options={
                'verbose_name': 'setting',
                'verbose_name_plural': 'setting',
            },
        ),
        migrations.CreateModel(
            name='SlurpitPlanning',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('last_updated', models.DateTimeField(auto_now=True, null=True)),
                ('custom_field_data', models.JSONField(blank=True, default=dict, encoder=utilities.json.CustomFieldJSONEncoder)),
                ('description', models.CharField(blank=True, max_length=200)),
                ('comments', models.TextField(blank=True)),
                ('external_id', models.CharField(max_length=32)),
                ('name', models.CharField(editable=False, max_length=100, unique=True)),
                ('disabled', models.BooleanField(editable=False)),
                ('selected', models.BooleanField(default=False)),
                ('last_synced', models.DateTimeField(blank=True, editable=False, null=True)),
                ('source', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='slurpit_netbox.slurpitsource')),
                ('tags', taggit.managers.TaggableManager(through='extras.TaggedItem', to='extras.Tag')),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='SlurpitPlan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('last_updated', models.DateTimeField(auto_now=True, null=True)),
                ('custom_field_data', models.JSONField(blank=True, default=dict, encoder=utilities.json.CustomFieldJSONEncoder)),
                ('description', models.CharField(blank=True, max_length=200)),
                ('comments', models.TextField(blank=True)),
                ('name', models.TextField(max_length=255, null=True)),
                ('plan_id', models.TextField(max_length=10, unique=True)),
                ('selected', models.BooleanField(default=False)),
                ('tags', taggit.managers.TaggableManager(through='extras.TaggedItem', to='extras.Tag')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SlurpitImportedDevice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('last_updated', models.DateTimeField(auto_now=True, null=True)),
                ('custom_field_data', models.JSONField(blank=True, default=dict, encoder=utilities.json.CustomFieldJSONEncoder)),
                ('slurpit_id', models.IntegerField(unique=True)),
                ('disabled', models.BooleanField(default=False)),
                ('hostname', models.CharField(max_length=255, unique=True)),
                ('fqdn', models.CharField(max_length=128)),
                ('device_os', models.CharField(max_length=128)),
                ('device_type', models.CharField(max_length=255)),
                ('brand', models.CharField(max_length=255)),
                ('createddate', models.DateTimeField()),
                ('changeddate', models.DateTimeField(null=True)),
                ('mapped_device', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='dcim.device')),
                ('mapped_devicetype', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='dcim.devicetype')),
                ('tags', taggit.managers.TaggableManager(through='extras.TaggedItem', to='extras.Tag')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
