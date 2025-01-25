from selenium import webdriver
from selenium.webdriver import Keys
from time import sleep

driver = webdriver.Chrome()
driver.get('https://www.google.com/')
sleep(2)
#znajdz element i w niego kliknij
driver.find_element('id', 'L2AGLb' ).click() #stare kursy find_element_by_id
sleep(2)
#id przycisku zaakceptuj wszystko

#button_accept = driver.find_element('id', 'L2AGLb')
#button_accept. click
#oba kody robią to samo ale w tej wersji zapisujemy zmienna wiec mozna sioę do niej jak potrzebujemy odniesc

search_field = driver.find_element('name', 'q')
search_field.send_keys('Kto gra na narodowym?') #wprowadz tu jakiś tekst
sleep(2)
# search_button = driver.find_element('name', 'btnK') #klikanie w szukaj
# search_button.click()  - albo mozna importowac Keys (w2 linijce)
search_field.send_keys(Keys.ENTER)  #dxzieki zasimportowaniu Keys

input('Czeka na enter') #- mozna tak

driver.quit()