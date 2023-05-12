from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
 
from my_spotify_songs.models import Songs
from my_spotify_songs.serializers import SongsSerializer
from rest_framework.decorators import api_view

@api_view(['GET', 'POST', 'DELETE'])
def my_spotify_songs_list(request):

    if request.method == 'GET':
        songs = Songs.objects.all()
        song_name = request.GET.get('song_name', None)

        if song_name is not None:
            songs = songs.filter(song_name__icontains=song_name)

        song_serializer = SongsSerializer(songs, many=True)

        return JsonResponse(song_serializer.data, safe=False)
    
    elif request.method == 'POST':
        song_data = JSONParser().parse(request)
        song_serializer = SongsSerializer(data=song_data)
        if song_serializer.is_valid():
            song_serializer.save()
            return JsonResponse(song_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(song_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        count = Songs.objects.all().delete()
        return JsonResponse({'message': '{} Songs were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)

 
@api_view(['GET', 'PUT', 'DELETE'])
def my_spotify_songs_detail(request, pk):
    # update a song info by the id in the request
    try: 
        song = Songs.objects.get(pk=pk) 
    except Songs.DoesNotExist: 
        return JsonResponse({'message': 'The song does not exist'}, status=status.HTTP_404_NOT_FOUND) 
 
    if request.method == 'GET': 
        song_serializer = SongsSerializer(song)
        return JsonResponse(song_serializer.data)
 
    elif request.method == 'PUT': 
        song_data = JSONParser().parse(request)
        song_serializer = SongsSerializer(song, data=song_data) 
        if song_serializer.is_valid(): 
            song_serializer.save() 
            return JsonResponse(song_serializer.data)
        return JsonResponse(song_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
 
    elif request.method == 'DELETE':
        song.delete() 
        return JsonResponse({'message': 'Song was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
        
@api_view(['GET'])
def my_spotify_songs_fav(request):
    # find all favorite songs
    if request.method == 'GET':
        songs = Songs.objects.filter(Favorite=True)

        song_serializer = SongsSerializer(songs, many=True)

        return JsonResponse(song_serializer.data, safe=False)
    else:
        return JsonResponse({'message': 'There is no matching song...'}, status=status.HTTP_204_NO_CONTENT)
        
    
