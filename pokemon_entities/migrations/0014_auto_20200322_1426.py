# Generated by Django 2.2.3 on 2020-03-22 14:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0013_auto_20200322_1425'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pokemon',
            old_name='title',
            new_name='title_ru',
        ),
    ]