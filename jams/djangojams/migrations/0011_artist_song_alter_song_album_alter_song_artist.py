# Generated by Django 4.2 on 2023-04-04 14:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('djangojams', '0010_alter_artist_options_alter_song_album_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='artist',
            name='song',
            field=models.ManyToManyField(related_name='song', to='djangojams.song'),
        ),
        migrations.AlterField(
            model_name='song',
            name='album',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='album', to='djangojams.album'),
        ),
        migrations.AlterField(
            model_name='song',
            name='artist',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='artist', to='djangojams.artist'),
        ),
    ]
