# Generated by Django 3.2.9 on 2021-11-03 01:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Peliculas', '0013_auto_20211102_1920'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clasificacion',
            name='clasificacion_edad',
            field=models.CharField(choices=[('A', 'A'), ('AA', 'AA'), ('B', 'B'), ('B-15', 'B-15'), ('C', 'C'), ('R', 'R')], max_length=15, verbose_name='Elige la clasificacion'),
        ),
        migrations.AlterField(
            model_name='clasificacion',
            name='descripcion',
            field=models.CharField(max_length=350, verbose_name='Descripcion resumida'),
        ),
    ]