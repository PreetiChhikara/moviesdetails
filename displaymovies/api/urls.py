from django.contrib import admin
from django.urls import path

from .views import ( DisplayMoviesDetailAPIView,
	DisplayMoviesAPIView,)


urlpatterns = [
    path('',DisplayMoviesDetailAPIView.as_views(), name='list'),
    path('<int:id>/', DisplayMoviesAPIView.as_views(),name='alldetails'),
]