# Generated by Django 4.2.1 on 2023-07-05 09:38

import django.core.validators
from django.db import migrations, models
import reservation.models


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='no_of_guests',
            field=models.IntegerField(validators=[reservation.models.validate_positive, django.core.validators.MaxValueValidator(6)]),
        ),
        migrations.AlterField(
            model_name='menu',
            name='inventory',
            field=models.IntegerField(validators=[reservation.models.validate_positive, django.core.validators.MaxValueValidator(5)]),
        ),
    ]
