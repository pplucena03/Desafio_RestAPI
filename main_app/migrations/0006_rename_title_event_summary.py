# Generated by Django 5.1.1 on 2024-09-15 11:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_alter_event_end_date_alter_event_start_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='title',
            new_name='summary',
        ),
    ]
