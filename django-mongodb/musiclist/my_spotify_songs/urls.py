from django.urls import re_path 
from my_spotify_songs import views
 
urlpatterns = [
    re_path(r'^api/my_spotify_songs/$', views.my_spotify_songs_list),
    re_path(r'^api/my_spotify_songs/(?P<pk>[0-9]+)/$', views.my_spotify_songs_detail),
    re_path(r'^api/my_spotify_songs/Favorite/$', views.my_spotify_songs_fav)
]