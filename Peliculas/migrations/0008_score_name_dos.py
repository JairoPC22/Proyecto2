# Generated by Django 3.2.9 on 2021-11-02 04:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Peliculas', '0007_alter_movie_soundtrack'),
    ]

    operations = [
        migrations.AddField(
            model_name='score',
            name='name_dos',
            field=models.CharField(default=22, max_length=150, verbose_name='Nombre de la pelicula'),
            preserve_default=False,
        ),
    ]