# Generated by Django 2.2.3 on 2020-03-21 03:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0008_auto_20200321_0338'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pokemon',
            old_name='next_evolution',
            new_name='previous_evolution',
        ),
    ]