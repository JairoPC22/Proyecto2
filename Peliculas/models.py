from django.db import models


# Create your models here.
class Movie(models.Model):
    name = models.CharField(verbose_name='Titulo', max_length=150, unique=True)
    Sinopsis = models.TextField(verbose_name='Sinopsis', max_length=1200)
    elenco = models.TextField(verbose_name='Reparto', max_length=1200)
    director = models.CharField(verbose_name='Director', max_length=150)
    beto = models.CharField(verbose_name='Guion', max_length=150)
    calificacion = models.CharField(verbose_name='Calificacion', max_length=150)
    time = models.DecimalField(default=0.00, max_digits=5, decimal_places=2, verbose_name='Indicar el tiempo en horas')
    soundtrack = models.TextField(verbose_name='Soundtrack', max_length=1750)
    tamanio = models.CharField(verbose_name='Tamaño', max_length=150)
    poster = models.ImageField(verbose_name='Poster de la pelicula', upload_to='posters/peliculas/', null=True)

    def __str__(self):
        return self.name + ' ' + self.Sinopsis + ' ' + self.elenco + ' ' + self.director + ' ' + self.calificacion

    class Meta:
        verbose_name = 'Movie'
        verbose_name_plural = 'Movies'


class Actor(models.Model):
    Nombre_Actor = models.CharField(max_length=150, verbose_name='Nombre del Actor o Actriz')
    fechaNacimiento = models.DateField(verbose_name='Fecha de Nacimiento')
    Lugar = models.CharField(verbose_name='Lugar de nacimiento', max_length=150)
    trayectoria = models.TextField(verbose_name='Peliculas y series en las que ha participado', max_length=780)
    papel = models.CharField(verbose_name='Personaje', max_length=155)
    foto = models.ImageField(verbose_name='Fotograafia del actor', upload_to='posters/Fotografias/', null=True)

    def __str__(self):
        return self.Nombre_Actor

    class Meta:
        verbose_name = 'Actor'
        verbose_name_plural = 'Actors'


cali = [('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'),
        ('10', '10')]


class Score(models.Model):
    name_dos = models.CharField(verbose_name='Nombre de la pelicula', max_length=150)
    like = models.BooleanField(verbose_name='¿Te gusto la pelicula?', default=False)
    comment = models.CharField(choices=cali, verbose_name='Del 1-10 ¿Como calificas la pelicula?', max_length=15)


class Comment(models.Model):
    insert = models.TextField(verbose_name='Comentario', max_length=1000)
    answer = models.TextField(verbose_name='Añadir respuesta al comentario', max_length=1000)
    like = models.BooleanField(verbose_name='¿Te gusto el comentario?', default=False)


ESPECIALIDADES = [('A', 'A'), ('AA', 'AA'), ('B', 'B'), ('B-15', 'B-15'), ('C', 'C'), ('R', 'R'), ('PG-13', 'PG-13')]


class Clasificacion(models.Model):
    nombre_pelicula = models.CharField(verbose_name='Nombre de la pelicula', max_length=50)
    descripcion = models.CharField(verbose_name='Descripcion resumida', max_length=350)
    clasificacion_edad = models.CharField(choices=ESPECIALIDADES, verbose_name='Elige la clasificacion', max_length=15)

    def __str__(self):
        return self.nombre_pelicula + ' ' + self.clasificacion_edad + " "


class Trailer(models.Model):
    name_movie = models.CharField(verbose_name='Nombre de la pelicula', max_length=150, unique=True)
    duracion = models.DecimalField(default=0.00, max_digits=5, decimal_places=2, verbose_name='Duracion del trailer')
    tamanio_trailer = models.CharField(verbose_name='Tamaño', max_length=150)
    enlace = models.URLField(verbose_name='Enlace para ver el trailer', max_length=1000, unique=True)


GenerPeli = {('Acción', 'Acción'), ('Aventuras', 'Aventuras'), ('Ciencia Ficción', 'Ciencia Ficción'),
             ('Comedia', 'Comedia'), ('Drama', 'Drama'), ('Fantasía', 'Fantasía'), ('Musical', 'Musical'),
             ('Suspenso', 'Suspenso'), ('Terror', 'Terror'), ('Comedia Romantica', 'Comedia Romantica'),
             ('Comedia Dramatica', 'Comedia Dramatica')}


class Genero(models.Model):
    name_dos = models.CharField(verbose_name='Nombre de la pelicula', max_length=150, unique=True)
    genero = models.CharField(choices=GenerPeli, verbose_name='Elegi el genero de la pelicula', max_length=20)

    def __str__(self):
        return self.name_dos + ' ' + self.genero + " "
