# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aldryn_forms', '0004_auto_20151207_1825'),
    ]

    operations = [
        migrations.DeleteModel(
            name='FormData',
        ),
        migrations.AlterModelOptions(
            name='formsubmission',
            options={'ordering': ['-sent_at'], 'verbose_name': 'Form submission', 'verbose_name_plural': 'Form submissions'},
        ),
        migrations.AlterField(
            model_name='emailfieldplugin',
            name='required',
            field=models.BooleanField(default=False, verbose_name='Field is required'),
        ),
        migrations.AlterField(
            model_name='fieldplugin',
            name='required',
            field=models.BooleanField(default=False, verbose_name='Field is required'),
        ),
        migrations.AlterField(
            model_name='fileuploadfieldplugin',
            name='required',
            field=models.BooleanField(default=False, verbose_name='Field is required'),
        ),
        migrations.AlterField(
            model_name='formsubmission',
            name='language',
            field=models.CharField(default='it', max_length=10, verbose_name='form language', choices=[('it', 'it'), ('en', 'en'), ('fr', 'fr')]),
        ),
        migrations.AlterField(
            model_name='imageuploadfieldplugin',
            name='required',
            field=models.BooleanField(default=False, verbose_name='Field is required'),
        ),
        migrations.AlterField(
            model_name='option',
            name='value',
            field=models.CharField(max_length=100, verbose_name='Value'),
        ),
        migrations.AlterField(
            model_name='textareafieldplugin',
            name='required',
            field=models.BooleanField(default=False, verbose_name='Field is required'),
        ),
    ]
