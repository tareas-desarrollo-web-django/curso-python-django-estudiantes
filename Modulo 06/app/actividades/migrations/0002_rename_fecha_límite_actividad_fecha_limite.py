# Generated by Django 5.1 on 2024-08-16 02:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('actividades', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='actividad',
            old_name='fecha_límite',
            new_name='fecha_limite',
        ),
    ]
