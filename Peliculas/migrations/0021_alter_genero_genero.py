# Generated by Django 3.2.9 on 2021-11-03 04:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Peliculas', '0020_auto_20211102_2247'),
    ]

    operations = [
        migrations.AlterField(
            model_name='genero',
            name='genero',
            field=models.CharField(choices=[('Terror', 'Terror'), ('Fantasía', 'Fantasía'), ('Drama', 'Drama'), ('Musical', 'Musical'), ('Comedia', 'Comedia'), ('Suspenso', 'Suspense'), ('Aventuras', 'Aventuras'), ('Acción', 'Acción'), ('Comedia Dramatica', 'Comedia Dramatica'), ('Ciencia Ficción', 'Ciencia Ficción'), ('Comedia Romantica', 'Comedia Romantica')], max_length=20, verbose_name='Elegi el genero de la pelicula'),
        ),
    ]
