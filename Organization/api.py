from rest_framework import viewsets, permissions

from . import serializers
from . import models


class BrugerViewSet(viewsets.ModelViewSet):
    """ViewSet for the Bruger class"""

    queryset = models.Bruger.objects.all()
    serializer_class = serializers.BrugerSerializer
    permission_classes = [permissions.IsAuthenticated]