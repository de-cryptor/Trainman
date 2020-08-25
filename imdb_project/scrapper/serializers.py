from rest_framework import serializers
from .models import Movie

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['movie_id',
                  'name',
                  'description',
                  'thumbnail_url',
                  'genre',
                  'duration',
                  'rating_count',
                  'avg_rating',
                  'director',
                  'actor',
                  'published_on'
                  ]
