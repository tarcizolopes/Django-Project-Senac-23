# Generated by Django 4.1.6 on 2023-02-09 00:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produtos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='produto',
            name='estoque',
            field=models.IntegerField(default=0),
        ),
    ]
