# Generated by Django 3.1.7 on 2021-03-05 21:35

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('servicio', '0003_auto_20210228_1224'),
        ('cliente', '0009_auto_20210228_1224'),
        ('cal', '0002_event_bloqueado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='cliente',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='cliente.cliente'),
        ),
        migrations.AlterField(
            model_name='event',
            name='servicio',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='servicio.servicio'),
        ),
    ]
