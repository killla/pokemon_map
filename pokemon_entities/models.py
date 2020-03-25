from django.db import models

class Pokemon(models.Model):
    title = models.CharField(max_length=200, verbose_name='Имя на русском')
    title_en = models.CharField(max_length=200,
                                blank=True,
                                verbose_name='Имя на английском')
    title_jp = models.CharField(max_length=200,
                                blank=True,
                                verbose_name='Имя на японском')
    photo = models.ImageField(upload_to='pokemons',
                              null=True,
                              blank=True,
                              verbose_name='Фото')
    description = models.TextField(verbose_name='Описание',
                                    blank = True,
                                   )
    previous_evolution = models.ForeignKey('self',
                                           null=True,
                                           blank = True,
                                           on_delete=models.SET_NULL,
                                           related_name='next_evolutions',
                                           verbose_name='Из кого эволюционирует')

    def __str__(self):
        return '{}'.format(self.title)

class PokemonEntity(models.Model):
    pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE, related_name='entities', verbose_name='Покемон')
    lat = models.FloatField(verbose_name='Широта')
    lon = models.FloatField(verbose_name='Долгота')

    appeared_at = models.DateTimeField(verbose_name='Появится в', null=True, blank = True)
    disappeared_at = models.DateTimeField(verbose_name='Исчезнет в', null=True, blank = True)

    level = models.IntegerField(verbose_name='Уровень', null=True, blank = True)
    health = models.IntegerField(verbose_name='Здоровье', null=True, blank = True)
    strength = models.IntegerField(verbose_name='Сила', null=True, blank = True)
    defence = models.IntegerField(verbose_name='Защита', null=True, blank = True)
    stamina = models.IntegerField(verbose_name='Выносливость', null=True, blank = True)