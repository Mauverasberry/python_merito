from doctest import set_unittest_reportflags

NFZ = {1234, 3476, 4544, 3423, 3254, 8769, 5436, 2345, 6532, 1243, 6435, 1298, 6732, 7688, 7648, 2345, 2356}
chorzy_rok = set([1234, 3476, 4544, 3423, 3254, 8769, 5436])
chorzy_miesiac = set([1234, 3476, 3098, 4544, 3423])
krzyki = {4544, 3423, 3254, 8769, 5436, 2345, 6532, 1243}
centrum = {7648, 2345, 2356, 3987, 1234, 3476, 3254}
zbior_pusty = set()

# ile osób chorowało w ostatnim roku na krzykach?

print(f'\nChorzy w ostatnim roku na Krzykach: {chorzy_rok & krzyki}')
print(f'ilość: {len(chorzy_rok & krzyki)}')

# sprawdzmy ile osób chorowało w ostanim roku w Centrum
print(f'\nChorzy w ostatnim roku w Centrum: {chorzy_rok & centrum}')
print(f'ilość: {len(chorzy_rok & centrum)}')

# ile osob mieszka w sumie w Centrum i na Krzykach?
print(f'Chorzy mieszkający na Krzykach i Centrum to {len(krzyki | centrum - krzyki & centrum)}')

# sprawdzmy poprawność danych:
print('Poprawność danych')
# każdy kto chorował w ostatnim miesiącu jednocześnie chorował w ostatnim roku
print(f'\n"Ludzie chorujący w ostatnim miesiącu i nie chorujący w ostatnim roku {chorzy_miesiac - chorzy_rok}')
print(f'Ilość {len(chorzy_miesiac - chorzy_rok)}')
if len(chorzy_miesiac - chorzy_rok) == 0:
    print(ok)
# nikt nie powinien jednocześnie mieszkać na Krzykach i w Centrum ,jeśli tak, to skądś trzeba usunac
duplikaty = krzyki & centrum
if len(duplikaty) != 0:
    print('\nZnaleziono duplikaty, uwsuwam')
    krzyki = krzyki - duplikaty
if len(duplikaty) == 0:
    print('ok, brak duplikatow')
# kazdy chory z Krzykow i z Centrum powinien być w NFZ
poza_nfz = (chorzy_rok | chorzy_miesiac | krzyki | centrum) - NFZ
print(f'Ludzie poza NFZ {poza_nfz}')
NFZ = NFZ | poza_nfz

# pesele żeńskie mają ostatnią cyfrę parzystą, męskie nieprzystą
# nowe zbiory, osobne dla K i M (w NFZ)
men = set()
woman = set()
for pesel in NFZ:
    if pesel % 2 == 0:
        woman.add(pesel)
    else:
        men.add(pesel)

# zadanie rekrutacyjne - usuwanie duplikatów
lista = [1, 2, 4, 6, 5, 6, 4, 2, 3, 3, 4, 2, 6]
print(list(set(lista)))

