# Generated by Django 2.2.3 on 2020-03-25 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0020_auto_20200325_1635'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemon',
            name='description',
            field=models.TextField(blank=True, default='', verbose_name='Описание'),
            preserve_default=False,
        ),
    ]
