from ufo.controller import get_user_info, add_user, remove_user, update_user, get_map
from ufo.model import users

def main():

    while True:
        print("==========MENU=================")
        print("0 - zamknij aplikacje")
        print("1 - wyświetl co u znajomych")
        print("2 - dodaj nowego użytkownika")
        print("3 - usuń użytkownika")
        print("4 - edytuj użytkownika")
        print("5 - Przygotuj mapę znajomych")
        print("==============MENU===================")

        choice = input("wybierz opcje menu")
        if choice == '0': break
        if choice == '1': get_user_info(users)
        if choice == '2': add_user(users)
        if choice == '3': remove_user(users)
        if choice == '4': update_user(users)
        if choice == '5': get_map(users)


if __name__ == "__main__":
        main()
