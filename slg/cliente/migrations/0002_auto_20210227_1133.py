# Generated by Django 3.1.7 on 2021-02-27 17:33

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('cliente', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='entidad',
            options={'ordering': ['-lugar'], 'verbose_name': 'Entidad', 'verbose_name_plural': 'Entidades'},
        ),
    ]
