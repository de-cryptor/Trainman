from django.conf.urls import url
from django.urls import path
from .views import *

urlpatterns = [

    path('scrap_movies_from_imdb/',scrap_movies_from_imdb,name='scrap_movies_from_imdb'),
    path('movie_list/',movie_list,name='movie_list')

]