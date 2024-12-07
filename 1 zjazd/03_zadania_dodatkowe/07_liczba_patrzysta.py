while True:
    try:
            number = float(input('Podaj liczbę:   '))
            if number % 2 == 0:  # gdy nie ma reszty z dzielenia
                print ('Twoja liczba jest parzysta')
                break
            else:
                print ('Twoja liczba jest nieparzysta')
                break
    except:
        print('Podana wartość nie jest liczbą. Podaj liczbę')