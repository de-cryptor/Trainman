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

@api_view(['POST'])
def scrap_movies_from_imdb(request):
    
    try :
        data = JSONParser().parse(request)
        url = data['url']
    except:
        pass
    