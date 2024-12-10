# dane = ['imie', ' nazwisko', 'wiek']
#
# for dana in dane:
#     name = input(f'Podaj {dana}')
#
# print(name)


#program, ktory przyjmuje dane dla x pracownikow
# program zwraca slownik w formacie {id: slownik danych}

pracownicy = {}
id = 0

while True:
    dane = input('Podaj dane (imie, nazwisko, wiek):  ').split() #rozdziela wpisany tekst po spacji
    pracownik = {'imie': dane[0], 'nazwisko': dane[1], 'wiek': dane[2]}
    id += 1
    pracownicy[id] = pracownik
    nastepny = input('Czy chcesz dodac nowa osobe T/N  ')
    if nastepny[0].lower() != 't':  # 1 znak jaki wpisze tylko bierzemy pod uwagę
        break

for id, dane in pracownicy.items():
    print(f'Pracownik o id {id} --- {dane}')

print(pracownicy[1]['nazwisko'])