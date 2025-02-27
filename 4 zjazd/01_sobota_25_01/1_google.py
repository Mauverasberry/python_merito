from selenium import webdriver # Selenium umożliwia automatyzację przeglądarki
import time

#automatyzacja na google tylko po dogadaniu z google za kase - inaczej nielegalne :D
okno1_chrome = webdriver.Chrome()       # Otwieramy nowe okno przeglądarki Google Chrome
okno2_firefox = webdriver.Firefox()     # Otwieramy nowe okno przeglądarki Mozilla Firefox
okno1_chrome.get('https://www.google.com/')     # Otwieramy stronę Google w Chrome
okno2_firefox.get('https://www.allegro.pl/')
time.sleep(2)

okno1_chrome.quit()
okno2_firefox.quit()

