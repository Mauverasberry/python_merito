
try:
    liczba_punktow = int(input('Ile masz punktów?   '))
# Jeśli użytkownik wpisze coś, co nie jest liczbą, np. "abc", wystąpi ValueError i kod przejdzie do bloku except ValueError.
    wiek = int(input('Ile masz mat?    '))
# Jeśli użytkownik wpisze np. "dwadzieścia" zamiast liczby, wystąpi ValueError.
    poziom = liczba_punktow/ wiek   #Jeśli wiek = 0, wystąpi ZeroDivisionError
    imie = input("Jak masz na imie?   ")
    print(imie[6])                  #Jeśli imię jest krótsze niż 7 znaków, wystąpi IndexError
    #Próba otwarcia pliku i zapisania do niego danych
    with open('dane', 'w') as file:  # Otwieramy plik o nazwie dane w trybie zapisu ('w'). Jeśli plik nie istnieje, zostanie utworzony.
        file.write('nowa linia')     # file.write('nowa linia') – Zapisujemy do pliku tekst "nowa linia"
# Bloki except – obsługa błędów
except ValueError:  #błędne dane wejściowe
    print('Niepoprawny form,at wprowadzonych danych')
    liczba_punktow = 1
    wiek = 100
except ZeroDivisionError:
    print('wiek nie moze byc 0')
    wiek = 100
except IndexError:  #brak danego znaku w imieniu
    print('Brak danego elementu')
    raise   # po złapaniu błędu nie próbujemy naprawiać sytuacji, tylko przerywamy działanie programu.
except FileNotFoundError:   # brak pliku
    #print('Plik nie istnieje, dane nie zostana zapisane w pliku')
    open('dane', 'w')
    with open('dane', 'w') as file: #Tworzymy plik dane
        file.write ('stworzono plik automatycznie') #Otwieramy plik ponownie i zapisujemy w nim:
        file.write('nowa linia')


