from django.db import models

# Genre Model

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

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name