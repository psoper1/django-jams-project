# Generated by Django 4.2 on 2023-04-03 21:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangojams', '0008_playlist'),
    ]

    operations = [
        migrations.AddField(
            model_name='playlist',
            name='songs',
            field=models.ManyToManyField(to='djangojams.song'),
        ),
    ]
