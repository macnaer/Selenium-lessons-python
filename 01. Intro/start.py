import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

driver = webdriver.Chrome()
driver.get('http://rutracker.org/')

try:
    enter = driver.find_element_by_link_text("Вход")
    enter.click()
except NoSuchElementException:
    print("Element Вход: Not Found ")
    
try:
    login = driver.find_element_by_id("top-login-uname")
    if login.is_displayed():
        login.send_keys("Cyber1993")
except NoSuchElementException:
    print("Element Login: Not Found")

try:
    password = driver.find_element_by_id("top-login-pwd")
    if password.is_displayed():
        password.send_keys("Cyber1993")
except NoSuchElementException:
    print("Element Password: Not Found")

try:
    login_btn = driver.find_element_by_id("top-login-btn")
    login_btn.click()   
except NoSuchElementException:
    print("Element login button: Not Found")

try:
    search = driver.find_element_by_id("search-text")
    search.send_keys("Empson S., Roth H. - CCNP SWITCH Portable Command Guide")
    search_btn = driver.find_element_by_id("search-submit")
    search_btn.click()
    single_search = driver.find_element_by_link_text("Empson S., Roth H. - CCNP SWITCH Portable Command Guide [2010, PDF, ENG]")
    single_search.click()
except NoSuchElementException:
    print("Element Search: Not Found")
time.sleep(5)
try:
    torrent_file = driver.find_element_by_link_text("Скачать .torrent")
    torrent_file.click()
except NoSuchElementException:
    print("Element Скачать .torrent: Not Found")


time.sleep(10)
driver.close()