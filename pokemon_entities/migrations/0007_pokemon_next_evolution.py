# Generated by Django 2.2.3 on 2020-03-21 03:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0006_auto_20200321_0302'),
    ]

    operations = [
        migrations.AddField(
            model_name='pokemon',
            name='next_evolution',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='pokemon_entities.Pokemon'),
        ),
    ]
