import folium
import json

from django.http import HttpResponseNotFound
from django.shortcuts import render

from pokemon_entities.models import Pokemon, PokemonEntity

MOSCOW_CENTER = [55.751244, 37.618423]
DEFAULT_IMAGE_URL = "https://vignette.wikia.nocookie.net/pokemon/images/6/6e/%21.png/revision/latest/fixed-aspect-ratio-down/width/240/height/240?cb=20130525215832&fill=transparent"


def add_pokemon(folium_map, lat, lon, name, image_url=DEFAULT_IMAGE_URL):
    icon = folium.features.CustomIcon(
        image_url,
        icon_size=(50, 50),
    )
    folium.Marker(
        [lat, lon],
        tooltip=name,
        icon=icon,
    ).add_to(folium_map)


def show_all_pokemons(request):
    pokemons = Pokemon.objects.all()
    print(pokemons)

    folium_map = folium.Map(location=MOSCOW_CENTER, zoom_start=12)
    for pokemon in pokemons:
        for pokemon_entity in PokemonEntity.objects.filter(pokemon=pokemon):#pokemon['entities']:
            add_pokemon(
                folium_map, pokemon_entity.lat, pokemon_entity.lon,
                pokemon.title,
                request.build_absolute_uri(pokemon.photo.url))

    pokemons_on_page = []
    for pokemon in pokemons:
        pokemons_on_page.append({
            'pokemon_id': pokemon.id,
            'img_url': request.build_absolute_uri(pokemon.photo.url),
            'title_ru': pokemon.title,
        })

    return render(request, "mainpage.html", context={
        'map': folium_map._repr_html_(),
        'pokemons': pokemons_on_page,
    })


def show_pokemon(request, pokemon_id):
    requested_pokemon = Pokemon.objects.get(id=pokemon_id)

    if requested_pokemon.previous_evolution:
        previous_pokemon = requested_pokemon.previous_evolution
        previous_evolution = {
            'pokemon_id': previous_pokemon.id,
            'title_ru': previous_pokemon.title,
            'img_url': previous_pokemon.photo.url
        }
    else: previous_evolution = None

    if requested_pokemon.next_evolutions.first():
        next_pokemon = requested_pokemon.next_evolutions.first()
        next_evolution  = {
            'pokemon_id': next_pokemon.id,
            'title_ru': next_pokemon.title,
            'img_url': next_pokemon.photo.url
        }
    else: next_evolution = None

    pokemon = {
        'pokemon_id' : requested_pokemon.id,
        'title_ru' : requested_pokemon.title,
        'title_en' : requested_pokemon.title_en,
        'title_jp' : requested_pokemon.title_jp,
        'description' : requested_pokemon.description,
        'img_url' : requested_pokemon.photo.url,
        'previous_evolution' : previous_evolution,
        'next_evolution' : next_evolution
    }

    folium_map = folium.Map(location=MOSCOW_CENTER, zoom_start=12)
    for pokemon_entity in PokemonEntity.objects.filter(pokemon=requested_pokemon):
        add_pokemon(
            folium_map, pokemon_entity.lat, pokemon_entity.lon,
            requested_pokemon.title,
            request.build_absolute_uri(requested_pokemon.photo.url))


    return render(request, "pokemon.html", context={'map': folium_map._repr_html_(),
                                                    'pokemon': pokemon})