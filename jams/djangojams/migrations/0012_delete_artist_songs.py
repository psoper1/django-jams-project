# Generated by Django 4.2 on 2023-04-04 14:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('djangojams', '0011_artist_song_alter_song_album_alter_song_artist'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Artist_Songs',
        ),
    ]
