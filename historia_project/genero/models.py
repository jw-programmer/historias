from django.db import models

class Genero(models.Model):

    nome = models.CharField(max_length=20);

    def __str__(self):
        pass

    class Meta:
        verbose_name = 'Genero'
        verbose_name_plural = 'Generos'
