
try:
    liczba_punktow = int(input('Ile masz punktów?   '))
    wiek = int(input('Ile masz mat?    '))
    poziom = liczba_punktow/ wiek
    imie = input("Jak masz na imie?   ")
    print(imie[6])
    with open('dane', 'w') as file:  #12:05
        file.write('nowa linia')
except ValueError:
    print('Niepoprawny form,at wprowadzonych danych')
    liczba_punktow = 1
    wiek = 100
except ZeroDivisionError:
    print('wiek nie moze byc 0')
    wiek = 100
except IndexError:
    print('Brak danego elementu')
    raise
except FileNotFoundError:
    #print('Plik nie istnieje, dane nie zostana zapisane w pliku')
    open('dane', 'w')
    with open('dane', 'w') as file: #12:16
        file.write ('stworzono plik automatycznie')
        file.write('nowa linia')