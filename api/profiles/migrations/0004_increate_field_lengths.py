# Generated by Django 4.1.2 on 2022-10-30 01:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0003_update_profiles_fields'),
    ]

    operations = [
        migrations.AlterField(
            model_name='link',
            name='title',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='link',
            name='url',
            field=models.CharField(max_length=100),
        ),
    ]