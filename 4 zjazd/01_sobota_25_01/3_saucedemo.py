from selenium import webdriver
from selenium.webdriver.common.by import By
#25,01 11:00 ??? nie wiem co to robi szukanie po czyms konkretnie ale wybieranie z funcji
from time import sleep
import datetime

def make_screenshot(window):
    teraz = datetime.datetime.now()
    filename = teraz.strftime ('screens\\screenshot_%H_%M_%S.png')  #11:57 dwa \\
    window.get_screenshot_as_file(filename)


driver = webdriver.Chrome()
driver.get('https://saucedemo.com/')
sleep(2)
try:
    username_field = driver.find_element('id', 'user-nameA')
except:
    print('Nie zbaleziono pola')
    #driver.get_screenshot_as_file('error_screen.png')
    make_screenshot(driver)
    driver.quit()
    raise # 11:23 nie wiem co to robi
username_field.send_keys('standard_user')
sleep(2)

password_field = driver.find_element('id', 'password')
password_field.send_keys('secret_sauce')

#login_button = driver.find_element('id', 'login-button' ).click()  #kopiuj xpath by otrzymac lub znalezc w tekscie
login_button = driver.find_element(By.XPATH, '/html/body/div/div/div[2]/div[1]/div/div/form/input')
login_button.click()
sleep(2)

# driver.get_screenshot_as_file('screen1.png')  #zrob screena, ale nadpisuje za kazdym razem screena - potem zrobilismy funcje
make_screenshot(driver)

driver.quit()