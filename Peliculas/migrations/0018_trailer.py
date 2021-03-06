# Generated by Django 3.2.9 on 2021-11-03 02:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Peliculas', '0017_alter_clasificacion_clasificacion_edad'),
    ]

    operations = [
        migrations.CreateModel(
            name='Trailer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_movie', models.CharField(max_length=150, verbose_name='Nombre de la pelicula')),
                ('duracion', models.DecimalField(decimal_places=2, default=0.0, max_digits=5, verbose_name='Duracion del trailer')),
                ('tamanio_trailer', models.CharField(max_length=150, verbose_name='Tamaño')),
                ('enlace', models.URLField(max_length=1000, unique=True, verbose_name='Enlace para ver el trailer')),
            ],
        ),
    ]
