from django.contrib import admin

# Register your models here.
from .forms import DisplayMoviesForm
from .models import DisplayMovies


class DisplayMoviesAdmin(admin.ModelAdmin):
	list_display = ['name','popularity','director','genre','imdb_score']
	form = DisplayMoviesForm 

admin.site.register(DisplayMovies, DisplayMoviesAdmin)
