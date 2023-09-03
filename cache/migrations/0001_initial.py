# Generated by Django 4.2.4 on 2023-08-04 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CapFeedAdmin1',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('polygon', models.TextField(blank=True, null=True)),
                ('multipolygon', models.TextField(blank=True, null=True)),
                ('min_latitude', models.FloatField(blank=True, null=True)),
                ('max_latitude', models.FloatField(blank=True, null=True)),
                ('min_longitude', models.FloatField(blank=True, null=True)),
                ('max_longitude', models.FloatField(blank=True, null=True)),
            ],
            options={
                'db_table': 'cap_feed_admin1',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='CapFeedAlert',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('url', models.CharField(max_length=255, unique=True)),
                ('identifier', models.CharField(max_length=255)),
                ('sender', models.CharField(max_length=255)),
                ('sent', models.DateTimeField()),
                ('status', models.CharField()),
                ('msg_type', models.CharField()),
                ('source', models.CharField(max_length=255)),
                ('scope', models.CharField()),
                ('restriction', models.CharField(max_length=255)),
                ('addresses', models.TextField()),
                ('code', models.CharField(max_length=255)),
                ('note', models.TextField()),
                ('references', models.TextField()),
                ('incidents', models.TextField()),
            ],
            options={
                'db_table': 'cap_feed_alert',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='CapFeedAlertAdmin1',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'cap_feed_alertadmin1',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='CapFeedAlertInfo',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('language', models.CharField(max_length=255)),
                ('category', models.CharField()),
                ('event', models.CharField(max_length=255)),
                ('response_type', models.CharField()),
                ('urgency', models.CharField()),
                ('severity', models.CharField()),
                ('certainty', models.CharField()),
                ('audience', models.CharField()),
                ('event_code', models.CharField(max_length=255)),
                ('effective', models.DateTimeField()),
                ('onset', models.DateTimeField(blank=True, null=True)),
                ('expires', models.DateTimeField()),
                ('sender_name', models.CharField(max_length=255)),
                ('headline', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
                ('instruction', models.TextField(blank=True, null=True)),
                ('web', models.CharField(blank=True, max_length=200, null=True)),
                ('contact', models.CharField(max_length=255)),
                ('parameter', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'cap_feed_alertinfo',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='CapFeedAlertInfoArea',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('area_desc', models.TextField()),
                ('altitude', models.CharField()),
                ('ceiling', models.CharField()),
            ],
            options={
                'db_table': 'cap_feed_alertinfoarea',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='CapFeedAlertInfoAreaCircle',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('value', models.TextField()),
            ],
            options={
                'db_table': 'cap_feed_alertinfoareacircle',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='CapFeedAlertInfoAreaGeocode',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('value_name', models.CharField(max_length=255)),
                ('value', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'cap_feed_alertinfoareageocode',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='CapFeedAlertInfoAreaPolygon',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('value', models.TextField()),
            ],
            options={
                'db_table': 'cap_feed_alertinfoareapolygon',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='CapFeedAlertInfoParameter',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('value_name', models.CharField(max_length=255)),
                ('value', models.TextField()),
            ],
            options={
                'db_table': 'cap_feed_alertinfoparameter',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='CapFeedContinent',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'cap_feed_continent',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='CapFeedCountry',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('iso3', models.CharField(unique=True)),
                ('polygon', models.TextField(blank=True, null=True)),
                ('multipolygon', models.TextField(blank=True, null=True)),
                ('centroid', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'cap_feed_country',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='CapFeedFeed',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('url', models.CharField(max_length=255, unique=True)),
                ('format', models.CharField()),
                ('polling_interval', models.IntegerField()),
                ('official', models.BooleanField()),
                ('status', models.CharField()),
                ('author_name', models.CharField()),
                ('author_email', models.CharField()),
                ('notes', models.TextField()),
            ],
            options={
                'db_table': 'cap_feed_feed',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='CapFeedFeedlog',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('exception', models.CharField(max_length=255)),
                ('error_message', models.TextField()),
                ('description', models.TextField()),
                ('response', models.TextField()),
                ('alert_url', models.CharField(max_length=255)),
                ('timestamp', models.DateTimeField()),
                ('notes', models.TextField()),
            ],
            options={
                'db_table': 'cap_feed_feedlog',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='CapFeedLanguageInfo',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('language', models.CharField()),
                ('logo', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'cap_feed_languageinfo',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='CapFeedRegion',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('polygon', models.TextField(blank=True, null=True)),
                ('centroid', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'cap_feed_region',
                'managed': False,
            },
        ),
    ]
