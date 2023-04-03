from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.models import User
from rest_framework import viewsets, permissions
from djangojams.serializers import *

# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer

def genre_list(request):
    list_genre = Genre.objects.values_list('name',)
    html = ''
    for genre in list_genre:
        html += '<h1>%s</h1>' % genre
    return HttpResponse(html)
class AlbumViewSet(viewsets.ModelViewSet):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer

def album_list(request):
    list_album = Album.objects.values_list('name', 'publish_date', 'cover_art', 'genres')
    html = ''
    for album in list_album:
        html += '<h1>%s</h1>' % album
    return HttpResponse(html)
