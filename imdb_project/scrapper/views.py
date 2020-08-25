from django.core.exceptions import ObjectDoesNotExist
from .serializers import MovieSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view , permission_classes , authentication_classes
from rest_framework.parsers import JSONParser
from rest_framework import permissions
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated,IsAdminUser
import json
import pandas as pd
from bs4 import BeautifulSoup
import requests
from .models import *
@api_view(['POST'])
def scrap_movies_from_imdb(request):
    
    #try :
    data = JSONParser().parse(request)
    url = data['url']
    user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.143 Safari/537.36'
    headers = {'User-Agent': user_agent}
    raw_html = requests.get(url,headers=headers)
    soup_data = BeautifulSoup(raw_html.text,'html.parser')
    movies = soup_data.findAll('td',{'class':"titleColumn"})
    base_url = "https://www.imdb.com"
    for movie in movies:
        movie_link = base_url + movie.a.get('href')
        movie_html = requests.get(movie_link,headers=headers)
        movie_data = BeautifulSoup(movie_html.text,'html.parser')
        movie_data = movie_data.find('script',{'type':"application/ld+json"})
        movie_dict = str(movie_data)[35:-9]
        data = json.loads(movie_dict)
        movie_id = data.get('url',None)[7:-1]
        name = data['name']
        thumbnail_url = data['image']
        actor = data['actor']
        director = data['director']
        published_on = data['datePublished']
        genre = data['genre']
        rating_count = data['aggregateRating']['ratingCount']
        avg_rating = data['aggregateRating']['ratingValue']
        description = data['description']
        print(data['duration'])
        duration = data['duration'][2:-1].split('H')
        print(duration)
        try :
            duration = duration[0] + " Hour " + duration[1] + " Minutes"
        except:
            duration = duration[0] + " Hour "
        try :
            movie_object = Movie.objects.get(movie_id=movie_id)
        except :
            movie_object = Movie.objects.create(
                movie_id=movie_id,
                name=name,
                actor=actor,
                director=director,
                published_on=published_on,
                duration=duration,
                avg_rating = avg_rating,
                rating_count=rating_count,
                genre=genre,
                thumbnail_url=thumbnail_url,
                description=description
                )
            print(movie_object)
    # except Exception as E:
    #     print(E)
    #     pass
    result = dict()
    return Response(result)
    
@api_view(['GET'])
def movie_list(request):
    movie_queryset = Movie.objects.all()
    serializer = MovieSerializer(movie_queryset, many=True)
    return Response(serializer.data,status=status.HTTP_200_OK)

