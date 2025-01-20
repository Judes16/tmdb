from django.db import models
from django.contrib.postgres.fields import JSONField



class Movie(models.Model):
    adult = models.BooleanField(default=False)
    backdrop_path = models.CharField(max_length=255, null=True, blank=True)
    genre_ids = models.JSONField(null=True, blank=True)  # Store genres as JSON
    movie_id = models.IntegerField(unique=True)  # To store the 'id' from API
    original_language = models.CharField(max_length=10)
    original_title = models.CharField(max_length=255)
    overview = models.TextField(null=True, blank=True)
    popularity = models.FloatField()
    poster_path = models.CharField(max_length=255, null=True, blank=True)
    release_date = models.DateField(null=True, blank=True)
    title = models.CharField(max_length=255)
    video = models.BooleanField(default=False)
    vote_average = models.FloatField()
    vote_count = models.IntegerField()

    def __str__(self):
        return self.title


