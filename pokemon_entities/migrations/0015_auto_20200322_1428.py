# Generated by Django 2.2.3 on 2020-03-22 14:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0014_auto_20200322_1426'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pokemon',
            old_name='title_ru',
            new_name='title',
        ),
    ]
