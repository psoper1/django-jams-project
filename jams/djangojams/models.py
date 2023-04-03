from django.db import models

class Genre(models.Model):
    name = models.CharField(max_length=100, null=False)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.name

class Album(models.Model):
    name = models.CharField(max_length=500, null=False)
    publish_date = models.DateField(null=True)
    cover_art = models.URLField(max_length=300, null=True)
    genres = models.ManyToManyField('Genre')

    class Meta:
        ordering = ['name']

    # def __str__(self):
    #     return self.name

class Artist(models.Model):
    name = models.CharField(max_length=500, null=False)
    bio = models.TextField(max_length=1000, null=True)
    image = models.URLField(max_length=300, null=True)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.name

class Song(models.Model):
    name = models.CharField(max_length=200, null=False)
    album = models.ForeignKey('Album', on_delete=models.PROTECT)
    artist = models.ForeignKey('Artist', on_delete=models.PROTECT)

    class Meta:
        ordering = ['id']

    # def __str__(self):
    #     return self.name

class Artist_Songs(models.Model):
    song = models.ForeignKey('Song', on_delete=models.PROTECT)
    artist = models.ForeignKey('Artist', on_delete=models.PROTECT)

    class Meta:
        ordering = ['id']

    # def __str__(self):
    #     return self.name

class Playlist(models.Model):
    name = models.CharField(max_length=200, null=False)
    artist = models.ForeignKey('Artist', on_delete=models.PROTECT)
    songs = models.ManyToManyField('Song')