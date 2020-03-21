"""
high level support for doing this and that.
"""
from rest_framework import viewsets
from .serializers import GeneroSerializer, Genero


class GeneroViewset(viewsets.ReadOnlyModelViewSet):
    queryset = Genero.objects.all()
    serializer_class = GeneroSerializer
