# Generated by Django 3.1.7 on 2021-02-28 18:24

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('servicio', '0002_auto_20210227_1230'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicio',
            name='descripcionServicio',
            field=models.CharField(blank=True, max_length=1000, null=True, verbose_name='descripcionn'),
        ),
    ]