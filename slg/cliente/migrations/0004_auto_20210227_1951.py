# Generated by Django 3.1.7 on 2021-02-28 01:51

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('cliente', '0003_auto_20210227_1230'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='nombres',
            field=models.CharField(max_length=50, verbose_name='nombre(s)'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='nss',
            field=models.PositiveIntegerField(blank=True, null=True, unique=True,
                                              validators=[django.core.validators.MaxValueValidator(99999999999),
                                                          django.core.validators.MinLengthValidator(11)],
                                              verbose_name='Número de seguridad social'),
        ),
    ]