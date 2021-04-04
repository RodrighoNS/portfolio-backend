from rest_framework import serializers
from . import models


class ApoSerializer(serializers.ModelSerializer):
  class Meta:
        fields = ('copyright', 'date', 'explanation', 'hdurl', 'media_type',
        'service_version', 'title', 'url', 'created_at', 'updated_at',)
        model = models.Apo
