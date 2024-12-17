
def stawka_ubezpieczenia(wiek, waga, czy_pali):
    stawka_bazowa = 200
    if wiek > 50:
        stawka_bazowa += wiek
    if waga > 100:
        stawka_bazowa += waga
    if czy_pali:
        stawka_bazowa *= 2
    return stawka_bazowa

ubezpieczenie_ola = stawka_ubezpieczenia(36, 99, '') #mozna zostawić pusty sring albo napisać inaczej if,
# można też zapisać True, False w warunkach
print(f'Ola zaplaci {ubezpieczenie_ola}')

def ubezpieczenie_zwierzecia(typ, wiek):
    print(f'zwierze: {typ} w wieku {wiek} lat')
    if typ == 'pies':
        return (100 * 1.5) + (wiek - 5) * 10
    else:
        return (200 * 1.2) + (wiek - 7) * 8

print(f'zapłacisz {ubezpieczenie_zwierzecia('pies', 12)}')