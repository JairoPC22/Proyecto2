# Generated by Django 3.2.9 on 2021-11-02 21:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Peliculas', '0010_alter_categoria_clasificacion_edad'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Categoria',
            new_name='Clasificacaion',
        ),
    ]