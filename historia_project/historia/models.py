from django.db import models
from django.conf import settings
from categoria.models import Categoria
from genero.models import Genero


class Historia(models.Model):

    titulo = models.CharField(max_length=50)
    descricao = models.TextField()
    data_publicacao = models.DateField(auto_now=True)
    autor = models.ForeignKey(settings.AUTH_USER_MODEL,
                              on_delete=models.PROTECT)
    categorias = models.ManyToManyField(Categoria)
    genero = models.ManyToManyField(Genero)

    class Meta:
        verbose_name = ("Historia")
        verbose_name_plural = ("Historias")

    def __str__(self):
        return self.titulo
