# Generated by Django 5.1 on 2024-08-22 02:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('actividades', '0003_auto_20240815_2022'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actividad',
            name='fecha_inicio',
            field=models.DateField(verbose_name='fecha de inicio'),
        ),
        migrations.AlterField(
            model_name='actividad',
            name='fecha_limite',
            field=models.DateField(verbose_name='fecha límite'),
        ),
    ]
