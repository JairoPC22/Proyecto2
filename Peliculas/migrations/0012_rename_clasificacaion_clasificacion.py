# Generated by Django 3.2.9 on 2021-11-02 21:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Peliculas', '0011_rename_categoria_clasificacaion'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Clasificacaion',
            new_name='Clasificacion',
        ),
    ]