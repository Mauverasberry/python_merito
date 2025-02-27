from selenium import webdriver
from selenium.webdriver.common.by import By                         # importujemy By do łatwiejszego wyszukiwania elementów na stronie
from time import sleep
import datetime                                                     # Importujemy datetime do generowania nazw plików z timestampem

# Definiujemy funkcję do robienia screenshotów
def make_screenshot(window):
    teraz = datetime.datetime.now()
    filename = teraz.strftime ('screens\\screenshot_%H_%M_%S.png')  #11:57 dwa \\
    window.get_screenshot_as_file(filename)                         # Robimy screenshot i zapisujemy go

# Uruchamiamy Chrome i wchodzimy na stronę
driver = webdriver.Chrome()
driver.get('https://saucedemo.com/')
sleep(2)

#Próba znalezienia pola użytkownika
try:
    username_field = driver.find_element(By.ID, 'user-name')    # Szukamy pola loginu - specjalny błąd A by spr robienie screena
except:
    print('Nie zbaleziono pola')                                        # Jeśli Selenium nie znajdzie elementu, wyświetli komunikat
    #driver.get_screenshot_as_file('error_screen.png')
    make_screenshot(driver)                                             # Robimy screenshot błędu
    driver.quit()
    raise                                                               # Rzucamy wyjątek - przerywamy działanie programu

# Wpisujemy login i hasło
username_field.send_keys('standard_user')                               # Wpisujemy nazwę użytkownika
sleep(2)
password_field = driver.find_element(By.ID, 'password')           # Szukamy pola hasła
password_field.send_keys('secret_sauce')

# Klikamy przycisk logowania
#login_button = driver.find_element('id', 'login-button' ).click()  #kopiuj xpath by otrzymac lub znalezc w tekscie
login_button = driver.find_element(By.XPATH, '/html/body/div/div/div[2]/div[1]/div/div/form/input') #Szukamy przycisku logowania za pomocą XPath.
login_button.click()
sleep(2)

# driver.get_screenshot_as_file('screen1.png')  #zrob screena, ale nadpisuje za kazdym razem screena - potem zrobilismy funcje
make_screenshot(driver)                                                   # Robimy screenshot ekranu po zalogowaniu

driver.quit()

