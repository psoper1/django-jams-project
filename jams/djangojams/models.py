from django.db import models

# Genre Model

class Genre(models.Model):
    name = models.CharField(max_length=100, null=False)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.name