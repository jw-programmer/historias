from django.db import models
from historia.models import Historia


class Capitulo(models.Model):

    index = models.IntegerField()
    titulo = models.CharField(max_length=50)
    notas = models.TextField(max_length=8000)
    data_publicacao = models.DateField( auto_now=True)
    texto = models.TextField()
    historia = models.ForeignKey(Historia, on_delete=models.PROTECT)

    def __str__(self):
        pass

    class Meta:
        verbose_name = 'Capitulo'
        verbose_name_plural = 'Capitulos'
