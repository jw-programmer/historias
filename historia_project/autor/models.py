from django.db import models
from django.contrib.auth.models import AbstractUser


class Autor(AbstractUser):
    descricao = models.TextField(
        default="Deveria colocar uma descrição sua aqui")

    def __str__(self):
        return self.username

    @classmethod
    def create_novo_autor(self, data):
        if "descricao" in data:
            autor = Autor(username=data["username"], descricao=data["descricao"])
            autor.set_password(data["password"])
            autor.save()
            return autor
        else:
            autor = Autor(username=data["username"])
            autor.set_password(data["password"])
            autor.save()
            return autor

    class Meta:
        verbose_name = "Autor"
        verbose_name_plural = "Autores"
