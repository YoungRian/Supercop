# Generated by Django 5.1.4 on 2024-12-19 03:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='curriculo',
            name='nome',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='curriculo',
            name='telefone',
            field=models.CharField(max_length=20),
        ),
    ]
