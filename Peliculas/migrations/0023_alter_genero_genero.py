# Generated by Django 3.2.9 on 2021-11-03 04:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Peliculas', '0022_alter_genero_genero'),
    ]

    operations = [
        migrations.AlterField(
            model_name='genero',
            name='genero',
            field=models.CharField(choices=[('Acción', 'Acción'), ('Comedia Dramatica', 'Comedia Dramatica'), ('Musical', 'Musical'), ('Ciencia Ficción', 'Ciencia Ficción'), ('Comedia Romantica', 'Comedia Romantica'), ('Terror', 'Terror'), ('Drama', 'Drama'), ('Comedia', 'Comedia'), ('Aventuras', 'Aventuras'), ('Suspenso', 'Suspenso'), ('Fantasía', 'Fantasía')], max_length=20, verbose_name='Elegi el genero de la pelicula'),
        ),
    ]