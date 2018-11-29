# Generated by Django 2.1 on 2018-09-15 20:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comentarios', '0002_auto_20180915_2046'),
        ('avaliacoes', '0001_initial'),
        ('core', '0003_pontosturisticos_atracoes'),
    ]

    operations = [
        migrations.AddField(
            model_name='pontosturisticos',
            name='avaliacoes',
            field=models.ManyToManyField(to='avaliacoes.Avaliacoes'),
        ),
        migrations.AddField(
            model_name='pontosturisticos',
            name='comentarios',
            field=models.ManyToManyField(to='comentarios.Comentarios'),
        ),
    ]
