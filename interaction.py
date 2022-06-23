import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

chrome_driver_path = "C:\Development\chromedriver.exe"
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)

driver.get(url="http://secure-retreat-92358.herokuapp.com/")

driver.implicitly_wait(2)

# Find by e xpath
# article_count = driver.find_element(by=By.XPATH, value='//*[@id="articlecount"]/a[1]')

# Find by css selector
# article_count=driver.find_element(by=By.CSS_SELECTOR, value="#articlecount a")

# Click on element
# article_count.click()

# current_events=driver.find_element(by=By.LINK_TEXT,value="Current events")
#
# current_events.click()

name = driver.find_element(by=By.NAME, value="fName")
name.send_keys("werwer")

last_name = driver.find_element(by=By.NAME, value="lName")
last_name.send_keys("werwer")

email = driver.find_element(by=By.NAME, value="email")
email.send_keys("werwer@sdfsdf.com")

sign_up_button = driver.find_element(by=By.CSS_SELECTOR, value=".btn.btn-lg.btn-primary.btn-block")
sign_up_button.click()

# print(article_count.text)

driver.close()  # Closes the tab which was opened earlier
driver.quit()  # Quits the entire browser.
