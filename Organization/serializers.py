from rest_framework import serializers

from . import models

class BrugerSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Bruger
        fields = [
            "username",
            "role",
            "created",
            "last_updated",
        ]