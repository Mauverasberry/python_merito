from selenium import webdriver
import datetime
from selenium.webdriver.common.by import By

class LoginPage:

    def __init__(self, moj_driver):     # Konstruktor
        self.driver = moj_driver        # przechowuje obiekt przeglądarki
        self.username_field_id ='user-name'  #stworzone te selfy by sie do nich potrem 'prościej odnosić"
        self.password_field_id = 'password'  # ID pola hasła
        self.login_button_xpath = '/html/body/div/div/div[2]/div[1]/div/div/form/input'     # XPath przycisku logowania
        self.after_login_url = 'https://www.saucedemo.com/inventory.html'       # Adres po zalogowaniu


    def open(self):     # Otwiera stronę logowania
        self.driver.get('http://www.saucedemo.com/')

    def print_page_info(self):      # Wypisuje informacje o stronie
        print('Nazwa strony', self.driver.title)        # Wypisuje tytuł strony (title)
        print('adres', self.driver.current_url)         # oraz jej adres (current_url)

    def enter_username(self, username):     # Wpisuje nazwę użytkownika
        field = self.driver.find_element('id', self.username_field_id)      # Znajduje pole użytkownika
        field.clear()
        field.send_keys(username)       # Wpisuje nazwę użytkownika

    def enter_password(self, passwd='secret_sauce'):
        field = self.driver.find_element('id', self.password_field_id)
        field.clear()
        field.send_keys(passwd)     #Domyślne hasło ('secret_sauce') jest już wpisane.

    def click_login(self):          # Kliknięcie przycisku logowania
        field = self.driver.find_element('xpath', self.login_button_xpath)
        field.click()

    def make_screenshot(self):
        teraz = datetime.datetime.now()
        filename = teraz.strftime('screens\\screenshot_%H_%M_%S.png')
        self.driver.get_screenshot_as_file(filename)           # Zapisuje zrzut ekranu

    def close(self):
        self.driver.quit()

