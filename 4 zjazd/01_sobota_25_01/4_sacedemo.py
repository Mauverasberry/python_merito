from selenium import webdriver          # Importuje webdriver, który umożliwia kontrolowanie przeglądarki
from selenium.webdriver.common.by import By
from selenium.common import NoSuchDriverException  # Importuje wyjątek, który wskazuje na problem z uruchomieniem przeglądarki
from time import sleep
import datetime

# Definicja funkcji do robienia screenshotów:
def make_screenshot(window):
    teraz = datetime.datetime.now()
    filename = teraz.strftime ('screens\\screenshot_%H_%M_%S.png') # gdy w nazwie nie ma rzadnego specjalnegio znaku może być 1x \
    window.get_screenshot_as_file(filename)

# Uruchomienie przeglądarki i otwarcie strony:
driver = webdriver.Chrome()
driver.get('https://saucedemo.com/')
sleep(2)
# Wyszukiwanie pola logowania (błąd w ID):
try:
    username_field = driver.find_element('id', 'user-nameA')   # Szukamy elementu (pola tekstowego) o id 'user-nameA'
except NoSuchDriverException:   #pobrane importrem - # Jeśli napotkamy wyjątek NoSuchDriverException - coś poszło nie tak z przeglądarką
    print('Nie zbaleziono pola')
    make_screenshot(driver)
    driver.quit()
    raise

# Wpisanie danych logowania (zakładając, że ID jest poprawne):
username_field.send_keys('standard_user')
sleep(2)
password_field = driver.find_element('id', 'password')
password_field.send_keys('secret_sauce')
login_button = driver.find_element(By.XPATH, '/html/body/div/div/div[2]/div[1]/div/div/form/input')
login_button.click()
sleep(2)

make_screenshot(driver)
driver.quit() # Zamyka całą przeglądarkę oraz wszystkie otwarte karty

