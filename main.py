from ufo.controller import get_user_info
from ufo.model import users

def main():


    while True:
        print("===============MENU================")
        print('0 - zamknij aplikacje')
        print('1 - wyświetl co u znajomych')
        print('2 - dodaj nowego użytkowanika')
        print('3 - usuń użytkownika')
        print('4 - edytuj użytkownika')
        print("===============MENU================")
        choice = input('wybierz opcje menu')
        if choice == '0':
            break
        if choice == '1':
            get_user_info(users)


if __name__ == '__main__':
    main()