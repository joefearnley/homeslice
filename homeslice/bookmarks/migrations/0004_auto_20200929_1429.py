# Generated by Django 3.0.7 on 2020-09-29 14:29

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('bookmarks', '0003_auto_20200929_1301'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookmark',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 9, 29, 14, 29, 44, 807414, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='bookmark',
            name='updated_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 9, 29, 14, 29, 44, 807469, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='tag',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 9, 29, 14, 29, 44, 808265, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='tag',
            name='updated_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 9, 29, 14, 29, 44, 808307, tzinfo=utc)),
        ),
    ]
