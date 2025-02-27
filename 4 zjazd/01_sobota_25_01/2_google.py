from selenium import webdriver
from selenium.webdriver import Keys                         #umożliwia symulowanie klawiszy (np. Entera)
from time import sleep

driver = webdriver.Chrome()                                   # Uruchamiamy przeglądarkę Chrome
driver.get('https://www.google.com/')
sleep(2)
#znajdz element i w niego kliknij
driver.find_element('id', 'L2AGLb' ).click()        # stare kursy find_element_by_id
sleep(2)
#id przycisku "Zaakceptuj wszystko" dla ciasteczek i klikamy go

#button_accept = driver.find_element('id', 'L2AGLb')
#button_accept. click
#oba kody robią to samo ale w tej wersji zapisujemy zmienna wiec mozna się do niej jak potrzebujemy odniesc

search_field = driver.find_element('name', 'q')         # Znajdujemy pole wyszukiwania na stronie Google
search_field.send_keys('Kto gra na narodowym?')                   # Wpisuje tekst do tego pola.
sleep(2)

# Możemy kliknąć przycisk "Szukaj" na dwa sposoby:
#1 (starsza metoda)
# search_button = driver.find_element('name', 'btnK')             # Znaleźć przycisk i kliknąć go
# search_button.click()

#2 (lepsza metoda)
search_field.send_keys(Keys.ENTER)                                 # dzieki zasimportowaniu Keys w 2 linijce naciska klawisz Enter
input('Czeka na enter')                                            # Program nie zamknie się od razu – czeka na Enter w terminalu.
driver.quit()

