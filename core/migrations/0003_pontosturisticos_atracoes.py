# Generated by Django 2.1 on 2018-09-15 19:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('atracoes', '0002_auto_20180915_1936'),
        ('core', '0002_auto_20180915_1929'),
    ]

    operations = [
        migrations.AddField(
            model_name='pontosturisticos',
            name='atracoes',
            field=models.ManyToManyField(to='atracoes.Atracoes'),
        ),
    ]