import pytest               # Import frameworka pytest do obsługi dekoratorów
from pom import LoginPage   # Import klasy LoginPage (POM - Page Object Model)
from time import sleep
from selenium import webdriver # Import Selenium do sterowania przeglądarką

# zestaw danych testowych dla dekoratora
test_data = [
    ('standard_user', 'secret_sauce', 'https://www.saucedemo.com/inventory.html'),
    ('locked_out_user', 'secret_sauce', 'https://www.saucedemo.com/'),
    ('problem_user', 'secret_sauce', 'https://www.saucedemo.com/inventory.html'),
    ('performance_glitch_user', 'secret_sauce', 'https://www.saucedemo.com/inventory.html'),
    ('standard_user', 'XX', 'https://www.saucedemo.com/'),
    ('locked_out_user', 'XX', 'https://www.saucedemo.com/'),
    ('problem_user', 'XX', 'https://www.saucedemo.com/'),
    ('performance_glitch_user', 'XX', 'https://www.saucedemo.com/')
]
# Test logowania
# wartości wewnatrz tych dekoratorów wrzucamy jako 1 stringa a nastepnie użyte parametry z test_data
@pytest.mark.skip(reason='Bo tak')             # Dekorator `@pytest.mark.skip` pomija  8 testów z parametrize
@pytest.mark.parametrize('username, passwd, url', test_data)    # Parametryzacja testu
# robi test z kazdym zestawem parametrów z test_data

def test_login_page_standard_user(username, passwd, url): # fukcja do logowania
    driver = webdriver.Chrome()                 # Uruchomienie przeglądarki Chrome
    page = LoginPage(driver)                    # Inicjalizacja obiektu LoginPage
    page.open()
    page.enter_username(username)
    page.enter_password(passwd)
    page.click_login()
    sleep(3)
    try:
        assert page.current_url() == url            ## Sprawdzenie, czy adres URL po zalogowaniu jest poprawny
    except AssertionError:                          # Błąd sprawdzania
        page.make_screenshot()
        print('Asercja nie przeszła\nstrona się nie zgadza')
        raise
    else:
        print('Asercja przeszła')                   ## Komunikat o sukcesie
    finally:
        print(f'Jesteś na stronie {page.current_url()}')
        print('Czyszcze dane')
        print('Zamykam stronę')
        page.close()

# Dodatkowe testy z różnymi oznaczeniami
@pytest.mark.skipif(len('piesek') == 5, reason='piesek jeszcze za mały')    #warunek pominięcia testu
def test1():
    assert 2 + 3 == 5       ## Zwykła asercja, byłaby pominięta gdyby `len('piesek') == 5`

@pytest.mark.xfail(reason='nie nasz dział') #sfailuj ale nazwij to inaczej
def test2():
    assert 2 + 3 == 5       ## Test przejdzie, ale oznaczony jako "oczekiwane niepowodzenie"

import sys
if sys.platform.startswith('win'): #jezeli w bibliotece systemowej moge zobaczyc na jakim systemie to robię, gdy zaczyna sie od 'win"
    @pytest.mark.skip('Linux-only tests')       ## Test zostanie pominięty na Windowsie
    def test3():
        assert 2 + 3 == 5