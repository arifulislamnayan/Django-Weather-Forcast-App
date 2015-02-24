# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255, verbose_name='name')),
                ('location_id', models.CharField(help_text='Location IDs can be retrieved from URLs of weather at specific cities at Yahoo! Weather, e.g. GMXX0008 from http://weather.yahoo.com/forecast/GMXX0008.html', max_length=255, verbose_name='Location ID')),
            ],
            options={
                'verbose_name': 'Location',
                'verbose_name_plural': 'Locations',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='WeatherLog',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('timestamp', models.DateTimeField(verbose_name='timestamp')),
                ('temperature', models.IntegerField(verbose_name='temperature (C)')),
                ('humidity', models.IntegerField(verbose_name='humidity (%)')),
                ('wind_speed', models.DecimalField(verbose_name='wind speed (kmh)', max_digits=5, decimal_places=2)),
                ('visibility', models.DecimalField(verbose_name='visibility (km)', max_digits=5, decimal_places=2)),
                ('location', models.ForeignKey(verbose_name='location', to='weatherApp.Location')),
            ],
            options={
                'ordering': ('-timestamp',),
                'verbose_name': 'weather log',
                'verbose_name_plural': 'weather logs',
            },
            bases=(models.Model,),
        ),
    ]
