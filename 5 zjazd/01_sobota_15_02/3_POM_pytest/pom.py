import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By             # Import klasy By do lokalizacji elementów HTML.


class LoginPage:                                        # Inicjalizacja klasy LoginPage

    def __init__(self, moj_driver):
        self.driver = moj_driver                        # Przypisanie przekazanego obiektu `webdriver` do `self.driver`
        self.username_field_id = 'user-name'            # stworzone te selby by sie do nich potrem 'prościej odnosić" # ID pola użytkownika
        self.password_field_id = 'password'             # ID pola hasła
        self.login_button_xpath = '//*[@id="login-button"]' # XPath przycisku logowania
        self.after_login_url = 'https://www.saucedemo.com/inventory.html'       # Oczekiwany URL po zalogowaniu

# Metody klasy LoginPage
    def open(self):                                     # Otwieranie strony logowania
        self.driver.get('https://www.saucedemo.com/')

    def print_page_info(self):                          # Wypisywanie informacji o stronie
        print('Nazwa strony', self.driver.title)
        print('adres', self.driver.current_url)

    def current_url(self):                              # Pobieranie aktualnego adresu URL
        return self.driver.current_url

    def enter_username(self, username):                 # Wprowadzanie nazwy użytkownika
        field = self.driver.find_element(By.ID, self.username_field_id)      # Znajduje pole użytkownika
        field.clear()
        field.send_keys(username)

    def enter_password(self, passwd='secret_sauce'):    # Wprowadzanie hasła
        field = self.driver.find_element(By.ID, self.password_field_id)
        field.clear()
        field.send_keys(passwd)

    def click_login(self):                              # Kliknięcie przycisku logowania
        field = self.driver.find_element(By.XPATH, self.login_button_xpath)
        field.click()

    def make_screenshot(self):
        teraz = datetime.datetime.now()
        filename = teraz.strftime('screens\\screenshot_%H_%M_%S.png')
        self.driver.get_screenshot_as_file(filename)

    def close(self):
        self.driver.quit()