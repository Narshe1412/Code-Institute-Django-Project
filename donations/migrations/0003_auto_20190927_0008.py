# -*- coding: utf-8 -*-
# Generated by Django 1.11.23 on 2019-09-27 00:08
from __future__ import unicode_literals

from decimal import Decimal
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donations', '0002_donation_amount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donation',
            name='amount',
            field=models.DecimalField(decimal_places=2, default=0.5, max_digits=12, validators=[django.core.validators.MinValueValidator(Decimal('0.50'))]),
        ),
    ]
