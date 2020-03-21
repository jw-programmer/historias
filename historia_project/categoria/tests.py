from django.test import TestCase
from .models import TipoCategoria, Categoria

# Create your tests here.


class TipoCategoriaTestCase(TestCase):
    def setUp(self):
        TipoCategoria.objects.create(nome="Animes")

    def test_verificar_todas_as_categorias(self):
        tipo_categoria = TipoCategoria.objects.get(nome="Animes")
        # print(tipo_categoria.nome)
        categoria1 = Categoria.objects.create(
            nome="Code Geass", tipo_categoria=tipo_categoria)
        categoria2 = Categoria.objects.create(
            nome="Death note", tipo_categoria=tipo_categoria)

        self.assertEqual(
            tipo_categoria.lista_categorias[0].nome, categoria1.nome)
        self.assertEqual(
            tipo_categoria.lista_categorias[1].nome, categoria2.nome)

    def test_verificar_tipo_sem_categorias(self):
        tipo_categoria = TipoCategoria.objects.get(nome="Animes")
        self.assertListEqual(tipo_categoria.lista_categorias, [])
