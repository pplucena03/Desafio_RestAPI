# Generated by Django 5.1.1 on 2024-09-06 22:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='data_hora_fim',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='event',
            name='data_hora_inicio',
            field=models.TextField(),
        ),
    ]
