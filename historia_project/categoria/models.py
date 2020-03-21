from django.db import models


class TipoCategoria(models.Model):

    nome = models.CharField(max_length=15)

    def __str__(self):
        return self.nome

    @property
    def lista_categorias(self):
        lista_categorias = list(self.categoria_set.all())
        return lista_categorias

    class Meta:
        verbose_name = 'Tipo de categoria'
        verbose_name_plural = 'Tipos de Categorias'


class Categoria(models.Model):

    nome = models.CharField(max_length=30)
    tipo_categoria = models.ForeignKey(TipoCategoria, on_delete=models.PROTECT)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
