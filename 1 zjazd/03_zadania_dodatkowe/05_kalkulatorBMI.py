
try:
    weight = float(input('Podaj wagę w kilogramach:  '))
    height = float(input('Podaj wzrost w metrach:  '))
    bmi = weight / (height ** 2)
    if weight < 0 or height < 0:
        print('Waga i wzrost muszą być liczbami większymi od 0')
    elif bmi < 16:
        print('wygłodzenie')
    elif 16 <= bmi < 17:
        print('wychudzenie')
    elif 17 <= bmi <= 18.5:
        print('niedowaga')
    elif 18.5 <= bmi < 25:
        print('waga prawidłowa')
    elif 25 <= bmi < 30:
        print('nadwaga')
    elif 30 <= bmi < 35:
        print('otyłość I stopnia')
    elif 35 <= bmi < 40:
        print('otyłość II stopnia')
    else:
        print('otyłość III stopnia')
except:
    print('Podana wartość nie jest poprawana. Spróbuj jeszcze raz.')



