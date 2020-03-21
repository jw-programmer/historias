from rest_framework import viewsets
from .serializers import TipoCategoriaSerializer, TipoCategoria, CategoriaSerializer, Categoria

class TipoCategoriaViewset(viewsets.ReadOnlyModelViewSet):
    queryset = TipoCategoria.objects.all()
    serializer_class = TipoCategoriaSerializer

class CategoriaViewset(viewsets.ReadOnlyModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
