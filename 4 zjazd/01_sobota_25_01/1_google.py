from selenium import webdriver
import time

#automatyzacja na google tylko po dogadaniu z goo9gle za kase - inaczej nielegalne :D
okno1_chrome = webdriver.Chrome() #okno przegladarki w chromie
okno2_firefox = webdriver.Firefox()
okno1_chrome.get('https://www.google.com/')
okno2_firefox.get('https://www.allegro.pl/')
time.sleep(2)

okno1_chrome.quit()
okno2_firefox.quit()

