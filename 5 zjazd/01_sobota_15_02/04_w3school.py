from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()         # Tworzymy obiekt przeglądarki (Chrome)
driver.maximize_window()            # Maksymalizujemy okno przeglądarki
driver.get("https://www.w3schools.com/")    # Otwieramy stronę W3Schools
time.sleep(1)
driver.find_element(By.ID, 'accept-choices').click()        # Klikamy w przycisk akceptacji cookies

menu = driver.find_element(By.ID, 'navbtn_tutorials')       # Pobieramy przycisk "Tutorials"
HTMLtutorial = driver.find_element(By.XPATH,'/html/body/div[2]/div[2]/div/nav[1]/div[1]/div/div[2]/div[1]/div[1]/a[2]')  # Pobieramy link do kursu HTML

webdriver.ActionChains(driver).move_to_element(menu).click().move_to_element(HTMLtutorial).click().perform()
# ActionChains(driver) – używa łańcucha akcji, by symulować ruchy myszy.
# move_to_element(menu).click() – najpierw przesuwa kursor na przycisk menu i klika.
# move_to_element(HTMLtutorial).click() – przesuwa kursor na link do HTML i klika.
# perform() wykonuje cały zestaw akcj

HTML_forms_attributes = driver.find_element(By.XPATH, '//*[@id="leftmenuinnerinner"]/a[41]')  # Znajduje "HTML Forms Attributes" w bocznym menu.
HTML_forms_attributes.click()
tryityourself = driver.find_element(By.XPATH, '//*[@id="main"]/div[3]/a') # znajduje "Try it Yourself", który otwiera stronę z edytorem kodu HTML.
tryityourself.click()
time.sleep(1)

currentWindowName = driver.current_window_handle        # Pobiera identyfikator aktualnie otwartego okna
windowNames = driver.window_handles                     # Pobiera listę wszystkich otwartych okien
print(currentWindowName)
print(windowNames)

# driver.switch_to.window(windowNames[1])

for okno in windowNames:
    if okno != currentWindowName:
        driver.switch_to.window(okno)                   # Jeśli ID okna różni się od bieżącego, przełączamy się na nie (switch_to.window(okno)).

input()
driver.switch_to.frame(driver.find_element(By.ID, 'iframeResult'))  # Przechodzimy do iframe (czyli osadzonego okna w HTML), gdzie znajduje się edytowalny formularz.
firstName = driver.find_element(By.ID, 'fname')                     # Znalezienie pola input o ID 'fname'

if firstName.is_enabled():                                                # Sprawdzenie, czy pole jest aktywne
    firstName.clear()
    firstName.send_keys('Kamil')                                          # Wpisanie tekstu "Kamil"
else:
    print('Nie da się wpisać')

driver.close()                                                            # Zamknięcie bieżącej karty
driver.quit()                                                             # Zamknięcie całej przeglądarki

