# Generated by Django 3.2.9 on 2021-11-03 04:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Peliculas', '0021_alter_genero_genero'),
    ]

    operations = [
        migrations.AlterField(
            model_name='genero',
            name='genero',
            field=models.CharField(choices=[('Fantasía', 'Fantasía'), ('Ciencia Ficción', 'Ciencia Ficción'), ('Terror', 'Terror'), ('Aventuras', 'Aventuras'), ('Drama', 'Drama'), ('Acción', 'Acción'), ('Musical', 'Musical'), ('Comedia', 'Comedia'), ('Comedia Dramatica', 'Comedia Dramatica'), ('Suspenso', 'Suspenso'), ('Comedia Romantica', 'Comedia Romantica')], max_length=20, verbose_name='Elegi el genero de la pelicula'),
        ),
    ]
