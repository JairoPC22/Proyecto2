from django.contrib import admin
from .models import Movie, Actor, Score, Comment, Clasificacion, Trailer, Genero
from django.utils.html import format_html


# Register your models here.

class MovieAdmin(admin.ModelAdmin):
    list_display = ('name', 'Sinopsis', 'elenco', 'director', 'poster', 'foto')
    search_fields = ('name', 'Sinopsis', 'elenco', 'director', 'poster', 'foto')

    def foto(self, obj):
        return format_html('<img src=() width="130" height="100" />', obj.poster.url)


class ActorAdmin(admin.ModelAdmin):
    list_display = ('Nombre_Actor', 'fechaNacimiento', 'Lugar', 'trayectoria', 'papel')
    search_fields = ('Nombre_Actor', 'fechaNacimiento', 'Lugar', 'trayectoria', 'papel')


admin.site.register(Movie, MovieAdmin)
admin.site.register(Actor, ActorAdmin)
admin.site.register(Score)
admin.site.register(Comment)
admin.site.register(Clasificacion)
admin.site.register(Trailer)
admin.site.register(Genero)
