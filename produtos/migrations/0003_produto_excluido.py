# Generated by Django 4.1.6 on 2023-02-10 22:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produtos', '0002_produto_estoque'),
    ]

    operations = [
        migrations.AddField(
            model_name='produto',
            name='excluido',
            field=models.BooleanField(default=False),
        ),
    ]
