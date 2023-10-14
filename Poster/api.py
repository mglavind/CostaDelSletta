from rest_framework import viewsets, permissions

from . import serializers
from . import models


class OpgaveViewSet(viewsets.ModelViewSet):
    """ViewSet for the Opgave class"""

    queryset = models.Opgave.objects.all()
    serializer_class = serializers.OpgaveSerializer
    permission_classes = [permissions.IsAuthenticated]


class GodkendelseViewSet(viewsets.ModelViewSet):
    """ViewSet for the Godkendelse class"""

    queryset = models.Godkendelse.objects.all()
    serializer_class = serializers.GodkendelseSerializer
    permission_classes = [permissions.IsAuthenticated]

class HoldViewSet(viewsets.ModelViewSet):
    """ViewSet for the Hold class"""

    queryset = models.Hold.objects.all()
    serializer_class = serializers.HoldSerializer
    permission_classes = [permissions.IsAuthenticated]