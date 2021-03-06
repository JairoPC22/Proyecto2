# Generated by Django 3.2.9 on 2021-11-02 03:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Peliculas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre_Actor', models.CharField(max_length=150, verbose_name='Nombre del Actor o Actriz')),
                ('fechaNacimiento', models.DateField(verbose_name='Fecha de Nacimiento')),
                ('Lugar', models.CharField(max_length=150, verbose_name='Lugar de nacimiento')),
                ('trayectoria', models.TextField(max_length=500, verbose_name='Peliculas y series en las que ha participado')),
                ('papel', models.CharField(max_length=155, verbose_name='Personaje')),
                ('foto', models.ImageField(null=True, upload_to='posters/Fotografias/', verbose_name='Fotograafia del actor')),
            ],
            options={
                'verbose_name': 'Actor',
                'verbose_name_plural': 'Actors',
            },
        ),
    ]
