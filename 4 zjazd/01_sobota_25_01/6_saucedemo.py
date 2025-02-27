from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common import NoSuchDriverException
from time import sleep
import datetime

def make_screenshot(window):
    teraz = datetime.datetime.now()
    filename = teraz.strftime ('screens\\screenshot_%H_%M_%S.png')
    window.get_screenshot_as_file(filename)

driver = webdriver.Chrome()
driver.get('https://saucedemo.com/')
sleep(2)
# Próba znalezienia pól logowania i przycisku
try:
    username_field = driver.find_element('id', 'user-name')
    password_field = driver.find_element('id', 'password')
    login_button = driver.find_element(By.XPATH, '/html/body/div/div/div[2]/div[1]/div/div/form/input')     # Szukamy przycisku logowania po XPATH

#Obsługa błędu NoSuchDriverException
except NoSuchDriverException:   #pobrane importrem
    print('Nie zbaleziono pola')    # Jeśli Selenium nie znajdzie sterownika przeglądarki, program: Wypisuje komunikat "Nie znaleziono pola"
    make_screenshot(driver)
    driver.quit()
    raise

username_field.send_keys('standard_user')
password_field.send_keys('secret_sauce')
# Sprawdzanie atrybutów przycisku logowania
print(f'Atrybut disabled: {login_button.get_attribute("disabled")}') # Sprawdzamy, czy przycisk jest wyłączony, None oznacza, że nie jest wyłączony).
print(f'Atrybut isConnected: {login_button.get_attribute("isConnected")}') # Sprawdza, czy przycisk jest nadal częścią strony.

if not login_button.get_attribute('disabled') is None:
    login_button.click() #  # Klikamy w przycisk logowania, jeśli nie jest wyłączony
else:
    print('Przycisk nieaktywny')

sleep(2)
make_screenshot(driver)
driver.quit()