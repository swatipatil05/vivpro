from rest_framework import serializers
from .models import Song


class SongSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Song
        fields = ('pk', 'index', 'title', 'id', 'danceability', 'energy', 'mode', 'acousticness',
                  'tempo', 'duration_ms', 'num_sections', 'num_segments', "star_ratings")
