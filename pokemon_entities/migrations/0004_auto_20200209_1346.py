# Generated by Django 2.2.3 on 2020-02-09 13:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0003_auto_20200209_1124'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pokemonentity',
            old_name='Pokemon',
            new_name='pokemon',
        ),
    ]
