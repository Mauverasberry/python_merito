from selenium import webdriver
import datetime
from selenium.webdriver.common.by import By
class LoginPage:

    def __init__(self, moj_driver):
        self.driver = moj_driver
        self.username_field_id ='user-name' #stworzone te selby by sie do nich potrem 'prościej odnosić"
        self.password_field_id = 'password'
        self.login_button_xpath = '/html/body/div/div/div[2]/div[1]/div/div/form/input'
        self.after_login_url = 'https://www.saucedemo.com/inventory.html'


    def open(self):
        self.driver.get('http://www.saucedemo.com/')

    def print_page_info(self):
        print('Nazwa strony', self.driver.title)
        print('adres', self.driver.current_url)

    def current_url(self):
        return self.driver.current_url

    def enter_username(self, username):
        field = self.driver.find_element('id', self.username_field_id)
        field.clear()
        field.send_keys(username)

    def enter_password(self, passwd='secret_sauce'):
        field = self.driver.find_element('id', self.password_field_id)
        field.clear()
        field.send_keys(passwd)

    def click_login(self):
        field = self.driver.find_element('xpath', self.login_button_xpath)
        field.click()

    def make_screenshot(self):
        teraz = datetime.datetime.now()
        filename = teraz.strftime('screens\\screenshot_%H_%M_%S.png')
        self.driver.get_screenshot_as_file(filename)

    def close(self):
        self.driver.quit()
