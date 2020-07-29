from django.shortcuts import render

# Create your views here.

from .models import DisplayMovies

def displaydetails(request):
	return render(request,'displaymovies/details.html')

def displayall(request):

	movie = DisplayMovies.objects

	return render(request,'displaymovies/allmovies.html',{'movie':movie})