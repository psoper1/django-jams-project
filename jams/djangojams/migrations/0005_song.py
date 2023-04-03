# Generated by Django 4.2 on 2023-04-03 21:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('djangojams', '0004_artist'),
    ]

    operations = [
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('album_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='djangojams.album')),
                ('artist_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='djangojams.artist')),
            ],
            options={
                'ordering': ['id'],
            },
        ),
    ]
