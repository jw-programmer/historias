from django.db import models
from django.contrib.auth.models import AbstractUser
class Autor(AbstractUser):
    descricao = models.TextField()

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = "Autor"
        verbose_name_plural = "Autores"
