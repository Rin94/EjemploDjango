# Generated by Django 3.1.7 on 2021-02-27 16:55

import django.core.validators
import django.db.models.deletion
import phonenumber_field.modelfields
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Entidad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lugar', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Entidad',
                'verbose_name_plural': 'Entidades',
            },
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombres', models.CharField(max_length=50)),
                ('apellidoPaterno', models.CharField(max_length=50)),
                ('apellidoMaterno', models.CharField(max_length=50)),
                ('nss', models.PositiveIntegerField(blank=True, null=True, validators=[
                    django.core.validators.MaxValueValidator(99999999999)])),
                ('email', models.EmailField(blank=True, max_length=100, null=True)),
                ('fechaNacimiento', models.DateField()),
                ('telefono', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('comentariosCliente', models.CharField(blank=True, max_length=255, null=True)),
                ('lugarNacimiento',
                 models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cliente.entidad')),
            ],
            options={
                'verbose_name': 'Cliente',
                'verbose_name_plural': 'Clientes',
            },
        ),
    ]
