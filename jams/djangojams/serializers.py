from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import *
# from .fields import AlbumField


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'url', 'username', 'email', 'groups']

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ['id', 'name']

class AlbumSerializer(serializers.ModelSerializer):
    genres = GenreSerializer(many=True)
    class Meta:
        model = Album
        fields = ['id', 'name', 'publish_date', 'cover_art', 'genres']

class AlbumListSerializer(serializers.ModelSerializer):
    genres = GenreSerializer(many=True)
    class Meta:
        model = Album
        fields = ['id', 'name', 'publish_date', 'cover_art', 'genres']

class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ['id', 'name', 'bio']

class SongSerializer(serializers.ModelSerializer):
    album = serializers.PrimaryKeyRelatedField(queryset=Album.objects.all())
    artist = serializers.PrimaryKeyRelatedField(queryset=Artist.objects.all())
    class Meta:
        model = Song
        fields = ["id", "name", "album", "artist"]

class SongListSerializer(serializers.ModelSerializer):
    album = AlbumSerializer()
    artist = ArtistSerializer()
    class Meta:
        model = Song
        fields = ["id", "name", "album", "artist"]
        

class PlaylistWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Playlist
        fields = ['id', 'name', 'songs']

class PlaylistReadOnlySerializer(serializers.ModelSerializer):
    songs = SongListSerializer(many=True, read_only=True)
    class Meta:
        model = Playlist
        fields = ['id', 'name', 'songs']