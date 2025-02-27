from pom import LoginPage       # from pom import LoginPage – importuje naszą klasę LoginPage
from time import sleep
from selenium import webdriver

driver = webdriver.Chrome()     # Tworzy instancję przeglądarki Chrome - Uruchamia Google Chrome w trybie Selenium.
page = LoginPage(driver)        # Tworzy obiekt klasy LoginPage - Tworzy stronę logowania (page).
page.open()                     # Otwiera stronę logowania
page.enter_username("Kamil")    # Wpisuje nazwę użytkownika
page.enter_password()           # Wpisuje domyślne hasło ('secret_sauce')
page.print_page_info()          # Wypisuje tytuł strony i adres URL.
page.click_login()
sleep(3)

