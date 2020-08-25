from django.db import models
import json

# Create your models here.

class Movie(models.Model):
    movie_id = models.CharField(max_length=100)
    name = models.CharField(max_length=500)
    description = models.TextField()
    thumbnail_url = models.CharField(max_length=500)
    genre = models.TextField()
    rating_count = models.IntegerField()
    avg_rating = models.CharField(max_length=10)
    director = models.TextField(default=json.dumps({}))
    actor = models.TextField(default=json.dumps([]))
    duration = models.CharField(max_length=100)
    published_on = models.DateField(blank=True,null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return (self.name)
    
     
    