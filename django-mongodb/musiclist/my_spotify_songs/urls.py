from django.conf.urls import url 
from my_spotify_songs import views 
 
urlpatterns = [ 
    url(r'^api/my_spotify_songs$', views.my_spotify_songs_list),
    url(r'^api/my_spotify_songs/(?P<pk>[0-9]+)$', views.my_spotify_songs_detail),
    url(r'^api/my_spotify_songs/Favorite$', views.my_spotify_songs_list_fav)
]