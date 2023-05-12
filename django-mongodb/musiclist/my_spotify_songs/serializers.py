from rest_framework import serializers 
from my_spotify_songs.models import Songs
 
 
class SongsSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Songs
        fields = ('id',
                  'song_name',
                  'artist',
                  'acousticness',
                  'danceability',
                  'liveness',
                  'Favorite')