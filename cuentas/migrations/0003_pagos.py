# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-08-29 15:54
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cuentas', '0002_formadepago'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pagos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_due_date', models.DateTimeField(verbose_name='fecha primer debito')),
                ('over_payment', models.IntegerField(blank=True)),
                ('number_of_payments', models.IntegerField(blank=True)),
                ('down_payment', models.IntegerField(blank=True)),
                ('last_payment_code', models.CharField(blank=True, max_length=255)),
                ('last_payment_amount', models.IntegerField(blank=True)),
                ('last_payment_date', models.DateTimeField(verbose_name='fecha ultimo debito')),
                ('last_payment_description', models.CharField(blank=True, max_length=255)),
                ('member_number', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='member_number_dee', to='cuentas.Member')),
            ],
        ),
    ]