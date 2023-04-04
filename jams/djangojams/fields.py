from rest_framework import serializers
from .models import *

class AlbumField(serializers.RelatedField):
    def to_representation(self, instance):
        return instance.name

    def to_internal_value(self, data):
        return Album.objects.get(name=data)