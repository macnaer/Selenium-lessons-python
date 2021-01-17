import time
from selenium import webdriver

driver = webdriver.Chrome()
driver.get('http://rutracker.org/')

enter = driver.find_element_by_link_text("Вход")
enter.click()
login = driver.find_element_by_id("top-login-uname")
login.send_keys("Cyber1993")
password = driver.find_element_by_id("top-login-pwd")
password.send_keys("Cyber1993")
login_btn = driver.find_element_by_id("top-login-btn")
login_btn.click()
search = driver.find_element_by_id("search-text")
search.send_keys("Empson S., Roth H. - CCNP SWITCH Portable Command Guide")
search_btn = driver.find_element_by_id("search-submit")
search_btn.click()
time.sleep(5)
single_search = driver.find_element_by_link_text("Empson S., Roth H. - CCNP SWITCH Portable Command Guide [2010, PDF, ENG]")
single_search.click()
torrent_file = driver.find_element_by_link_text("Скачать .torrent")
torrent_file.click()

time.sleep(10)
driver.close()