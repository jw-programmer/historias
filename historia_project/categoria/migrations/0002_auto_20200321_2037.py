# Generated by Django 2.2.10 on 2020-03-21 20:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('categoria', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='categoria',
            options={'verbose_name': 'Categoria', 'verbose_name_plural': 'Categorias'},
        ),
        migrations.AlterModelOptions(
            name='tipocategoria',
            options={'verbose_name': 'Tipo de categoria', 'verbose_name_plural': 'Tipos de Categorias'},
        ),
        migrations.AlterModelTable(
            name='categoria',
            table=None,
        ),
        migrations.AlterModelTable(
            name='tipocategoria',
            table=None,
        ),
    ]
