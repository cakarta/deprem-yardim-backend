# Generated by Django 4.1.6 on 2023-02-06 16:08

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tweets', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweet',
            name='hashtags',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=255), null=True, size=None),
        ),
    ]