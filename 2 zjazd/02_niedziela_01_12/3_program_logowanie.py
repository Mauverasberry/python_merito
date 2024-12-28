#
# import time #jakbysmy nazwali tak plik to by zaimportowal plik nie bibliotekę time
# for _ in range(5): # _ zmienna jak kazda inna - po prostu nie bedzie juz uzywana wiec nie nazywamy
#     print('siema')
#     time.sleep(1)

# import funkcje_3
# print(f'{funkcje_3.passwd_lenght('Kamil123')}')

# Napisz program, który ogarnia logowanie i rejestrację
# podaj nazwe uzytkownika i haslo
# program musi sprawdzic czy uzytkownik istnieje, jesli tak spr czy poprawne haslo, jesli tak dalsza cz. programu

import funkcje_3
name = input('Podaj nazwę użytkownika:  ')

# Jeśli użytkownik istnieje, program prosi o podanie hasła. Użytkownik ma 3 próby na podanie poprawnego hasła.
if funkcje_3.user_exist(name): #nie trzeba pisac == True
    counter_passwd = 0
    print(f'Witaj {name}')
    while True:
        passwd = input('Podaj haslo:   ')
        if funkcje_3.passwd_correct(name,passwd):
            break
        else:
            print('Zle haslo, sprobuj jeszcze raz:   ')
            counter_passwd += 1
            if counter_passwd == 3:
                print('Za dużo nieudanych prób. Program zakończony.')
                import sys
                sys.exit(0) #wyjscie z systemu 0 = bez bledu
# Jeśli użytkownik nie istnieje, program pyta, czy chce się zarejestrować.
# Jeśli tak, prosi o podanie hasła i rejestruje użytkownika. Jeśli nie, program kończy działanie.
else:
    print('Użytkownik nie istnieje. Czy chcesz się zarejestrować? (tak/nie)')
    answer = input('Podaj odpowiedź: ').strip().lower()
    if answer == 'tak':
        passwd = input('Podaj hasło do rejestracji: ')
        funkcje_3.register_user(name, passwd)
    else:
        print('Zakończono program.')