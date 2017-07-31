# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-30 23:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empleados', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='empleado',
            name='foto',
            field=models.ImageField(default='/profiles/no-img.jpg', upload_to=''),
        ),
        migrations.AlterField(
            model_name='empleado',
            name='color',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='empleado',
            name='email',
            field=models.CharField(max_length=255),
        ),
    ]