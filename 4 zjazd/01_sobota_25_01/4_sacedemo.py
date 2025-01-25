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
    username_field = driver.find_element('id', 'user-nameA')
except NoSuchDriverException:   #pobrane importrem
    print('Nie zbaleziono pola')
    make_screenshot(driver)
    driver.quit()
    raise
username_field.send_keys('standard_user')
sleep(2)

password_field = driver.find_element('id', 'password')
password_field.send_keys('secret_sauce')

login_button = driver.find_element(By.XPATH, '/html/body/div/div/div[2]/div[1]/div/div/form/input')
login_button.click()
sleep(2)

make_screenshot(driver)

driver.quit()