# a = int(input('Podaj liczbe:   '))
# b = int(input('Podaj liczbe:   '))
#
#
# try:
#     wynik = a / b
# except ZeroDivisionError:
#     print('Nie moge dzielic przez 0')
#     print('przyjmuje wynik 1')
#     wynik = 1
#
# except TypeError:
#     wynik=int(a) / int(b)
#     print('niepoprawy typ, zrzucam do inta')  #gdy dzielimy mniejsza przez wieksza
#
# print(wynik)

#jesli sie nie uda nie wyświetli wynik

import datetime
teraz = datetime.datetime.now()
print(teraz)
print(type(teraz))
# Formatowanie daty na czytelny sposób
sformatowana_data = teraz.strftime("%Y-%m-%d %H:%M:%S")
print(sformatowana_data)



