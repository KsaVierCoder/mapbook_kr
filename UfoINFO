users = [
    {"name": "Damian", "location": "Kraków", "posts": 555},
    {"name": "Mikołaj", "location": "Przasnysz", "posts": 200},
    {"name": "Krzysztof", "location": "Poznań", "posts": 100},
    {"name": "Bartosz", "location": "Ostrołęka", "posts": 300},
]


import folium
map = folium.Map(location=(52.23, 21.00),zoom_start=6)
folium.Marker(location=(52.23, 21.00),popup='geoinformatyka rzadzi oh yeah 111').add_to(map)
map.save('mapa.html')
import requests
from bs4 import BeautifulSoup

# https://pl.wikipedia.org/wiki/Przybys%C5%82awice_(wojew%C3%B3dztwo_lubelskie)

def get_cordinates(city:str)->list:

    url=f'https://pl.wikipedia.org/wiki/Grudzi%C4%85dz/{city}'
    response = requests.get(url).text
    response_html = BeautifulSoup(response, 'html.parser')
    longitude=float(response_html.select('.longitude')[1].text.replace(   ',','.'))
    latitude=float(response_html.select('.latiitude')[1].text.replace(   ',','.'))
    return [longitude,latitude]

def get_map(users_data:list)->None:
    map = folium.Map(location=(52.23, 21.00),zoom_start=6)
    for user in users_data:
        coordinates = get_cordinates(user['location'])

    folium.Marker(
        location=(coordinates[0], coordinates[1]),
        popup=f"Twój znajomy {user['name']}, <br/> miejscowość: {user['posts']}"
        map.save('map.html')
