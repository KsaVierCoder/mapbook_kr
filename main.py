users = [
    {"name": "Beata", "location": "Lublin", "posts": 500},
    {"name": "Michał", "location": "Krasnystaw", "posts": 420},
    {"name": "Ksavier", "location": "Grudziądz", "posts": 69},
    {"name": "Damian", "location": "Kraków", "posts": 2137},

]


def get_user_info(users_data: list) -> None:
    for user in users_data:
        print(f"Twój znajomy {user['name']}, z {user['location']} opublikował {user['posts']} postów")


get_user_info(users)
