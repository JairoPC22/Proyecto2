# Generated by Django 3.2.9 on 2021-11-02 04:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Peliculas', '0008_score_name_dos'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actor',
            name='trayectoria',
            field=models.TextField(max_length=780, verbose_name='Peliculas y series en las que ha participado'),
        ),
    ]