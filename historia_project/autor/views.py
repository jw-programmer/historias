from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from .serializers import AutorSerializer, Autor


class AutorViewset(viewsets.ModelViewSet):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer
    permission_classes = [AllowAny]

    def create(self, request):
        obj = Autor.create_novo_autor(request.data)
        return Response(data=self.get_serializer(obj).data, status=status.HTTP_201_CREATED)

    def update(self, request, pk=None):
        if request.user.id != int(pk):
            return Response(data="PROIBIDO!!!", status=status.HTTP_403_FORBIDDEN)
        else:
            return super().update(request, pk)

    def destroy(self, request, pk=None):
        if request.user.id != int(pk):
            return Response(data="PROIBIDO!!!", status=status.HTTP_403_FORBIDDEN)
        else:
            return super().destroy(request, pk)
