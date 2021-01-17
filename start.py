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

time.sleep(10)
driver.close()