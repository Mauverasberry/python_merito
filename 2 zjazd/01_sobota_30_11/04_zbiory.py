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

# pesele żeńskie mają ostatnią cyfrę parzystą , męskie nieprzystą
# stworz osobną liste dla k i m

