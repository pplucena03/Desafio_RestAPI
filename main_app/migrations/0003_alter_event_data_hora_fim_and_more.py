# Generated by Django 5.1.1 on 2024-09-06 22:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_alter_event_data_hora_fim_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='data_hora_fim',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='event',
            name='data_hora_inicio',
            field=models.DateTimeField(),
        ),
    ]
