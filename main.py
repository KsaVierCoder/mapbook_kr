
users=[
    {"name":"Beata","location":"Lublin","posts":500},
    {"name":"Michał","location":"Krasnystaw","posts":420},
    {"name":"Ksavier","location":"Grudziądz","posts":69},
    {"name":"Damian","location":"Kraków","posts":2137},

]

for user in users:
    print(f"Twój znajomy {user['name']}, z {user['location']} opublikował {user['posts']} postów")
