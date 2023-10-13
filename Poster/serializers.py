from rest_framework import serializers

from . import models


class OpgaveSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Opgave
        fields = [
            "last_updated",
            "description",
            "created",
            "name",
        ]

class GodkendelseSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Godkendelse
        fields = [
            "last_updated",
            "created",
            "Status",
            "Hold",
            "Opgave",
        ]
