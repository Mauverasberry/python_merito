from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common import NoSuchDriverException  #pobieramy ten blad tylko z selenium
from time import sleep
import datetime

def make_screenshot(window):
    teraz = datetime.datetime.now()
    filename = teraz.strftime ('screens\\screenshot_%H_%M_%S.png')
    window.get_screenshot_as_file(filename)


driver = webdriver.Chrome()
driver.get('https://saucedemo.com/')
sleep(2)
try:
    username_field = driver.find_element('id', 'user-name')
    password_field = driver.find_element('id', 'password')
    login_button = driver.find_element(By.XPATH, '/html/body/div/div/div[2]/div[1]/div/div/form/input')

except NoSuchDriverException:   #pobrane importrem
    print('Nie zbaleziono pola')
    make_screenshot(driver)
    driver.quit()
    raise
username_field.send_keys('standard_user')
password_field.send_keys('secret_sauce')

print(f'Atrybut disabled: {login_button.get_attribute("disabled")}') #11:26
print(f'Atrybut isConnected: {login_button.get_attribute("isConnected")}')

if not login_button.get_attribute('disabled') is None:
    login_button.click()
else:
    print('Przycisk nieaktywny')

login_button.click()
sleep(2)

make_screenshot(driver)

driver.quit()