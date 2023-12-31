# Generated by Django 4.2.6 on 2023-11-10 01:47

from django.db import migrations


def crear_estados(apps, schema_editor):
    Estado = apps.get_model('actividades', 'Estado')
    Estado.objects.get_or_create(titulo='Creada')
    Estado.objects.get_or_create(titulo='En progreso')
    Estado.objects.get_or_create(titulo='Terminada')
    Estado.objects.get_or_create(titulo='Cancelada')

def crear_importancias(apps, schema_editor):
    Importancia = apps.get_model('actividades', 'Importancia')
    Importancia.objects.get_or_create(titulo='Baja')
    Importancia.objects.get_or_create(titulo='Media')
    Importancia.objects.get_or_create(titulo='Alta')


class Migration(migrations.Migration):

    dependencies = [
        ('actividades', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(crear_estados),
        migrations.RunPython(crear_importancias),
    ]
