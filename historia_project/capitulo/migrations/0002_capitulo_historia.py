# Generated by Django 2.2.10 on 2020-03-27 14:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('capitulo', '0001_initial'),
        ('historia', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='capitulo',
            name='historia',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='historia.Historia'),
        ),
    ]
