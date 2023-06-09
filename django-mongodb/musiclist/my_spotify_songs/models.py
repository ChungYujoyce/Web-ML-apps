from django.db import models

# Create your models here.
class Songs(models.Model):
    # id field is added automatically.
    # Each field is specified as a class attribute, 
    # and each attribute maps to a database column.
    song_name = models.CharField(max_length=30, blank=False, default='Bad Habits')
    artist = models.CharField(max_length=20, blank=False, default='Ed Sheeran')
    acousticness = models.FloatField(default=0)
    danceability = models.FloatField(default=0)
    liveness = models.FloatField(default=0)
    Favorite = models.BooleanField(default=False)
