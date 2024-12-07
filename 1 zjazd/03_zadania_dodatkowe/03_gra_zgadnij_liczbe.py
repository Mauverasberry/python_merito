# Napisz program, w którym komputer losuje liczbę od 1 do 100, a użytkownik ma za zadanie ją odgadnąć.
# Po każdej próbie program podpowiada, czy podana liczba jest za duża czy za mała.

import random
number = random.randint(0,100)

try:
    user_number = float(input('Zgadnij liczbę:  '))
    while True:
        if number > user_number:
            user_number = float(input('Podana liczba jest za mała.\nZgaduj dalej:  '))
        elif user_number == number:
            print('Brawo! Zgadłeś liczbę! ')
            break
        else:
            user_number = float(input('Podana liczba jest za duża.\nZgaduj dalej:  '))

except:
    print('Podana wartość jest nieprawidłowa, spróbuj ponownie.')