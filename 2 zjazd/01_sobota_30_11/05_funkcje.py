
def przywitanie():  # deklaracja funcji
    print('Witaj, jest piękny dzień')

def przywitanie2(imie): #funkcja przyjmuje 1 argument
    print(f'Witaj {imie}, jest pięny dzien')

def przywitanie3(imie,wiek):
    if wiek <= 18:
        print(f'Cześć {imie}')
    else:
        if imie[-1] != "a":
            print(f'Szanowny Pan {imie}')
        else:
            print(f'Szanowna Pani {imie}')
przywitanie() # wywołanie funkcji
przywitanie2('Ola')
przywitanie3('Aleksandra', 36)



