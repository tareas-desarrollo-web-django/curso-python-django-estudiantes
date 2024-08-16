# Generated by Django 4.2.6 on 2024-08-13 01:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tarea',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=256, verbose_name='título')),
                ('descripcion', models.TextField(blank=True, null=True, verbose_name='descripción')),
                ('fecha_inicio', models.DateField(verbose_name='fecha inicio')),
                ('fecha_limite', models.DateField(verbose_name='fecha límite')),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True, verbose_name='fecha creación')),
            ],
        ),
    ]