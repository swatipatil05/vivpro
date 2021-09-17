from django.db import models

# Create your models here.


class Song(models.Model):
    index = models.BigIntegerField(primary_key=True)
    id = models.CharField(max_length=50, unique=True)
    title = models.CharField(max_length=200)
    danceability = models.FloatField()
    energy = models.FloatField()
    key = models.IntegerField()
    loudness = models.FloatField()
    mode = models.IntegerField()
    acousticness = models.FloatField()
    instrumentalness = models.FloatField()
    liveness = models.FloatField()
    valence = models.FloatField()
    tempo = models.FloatField()
    duration_ms = models.IntegerField()
    time_signature = models.IntegerField()
    num_sections = models.IntegerField()
    num_segments = models.IntegerField()
    song_class = models.IntegerField()
    num_bars = models.IntegerField()
    star_ratings = models.IntegerField()

    def __str__(self):
        return self.title
