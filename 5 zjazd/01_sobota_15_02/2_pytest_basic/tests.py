from kod import dodawanie

print('Cokolwiek')
# gdy funkcja zaczyna się od test można uroichomic normalknie pytestem, inaczej w terminalu -> pytest nazwa_pliku.py
# assert = sprawdz czy jest ok, podobnie jak if ale assert wyrzuca blad

def test_dodawanie_calkowite():
    assert dodawanie(1, 2) == 3         # Sprawdza, czy dodawanie(1, 2) == 3

def test_dodawanie_ulamki():
    assert dodawanie(0.1, 0.2) == 0.3   # aby test przeszedł zaokrągliliśmy w poprzednim pliku do 5 miejsc po przecinku

def test_dodawanie_string():                   # test przejdzie ponieważ '3' i '5' są konwertowane na float i sumowane.
    assert dodawanie('3', '5') == 8

def test_dodawanie_string2():                   # Sprawdza, czy niepoprawne dane wejściowe zwracają None
    assert dodawanie('3', 'A') == None

def test_dodawanie_string3():
    assert dodawanie('3', 'B') == None

