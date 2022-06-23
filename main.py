import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException

chrome_driver_path = "C:\Development\chromedriver.exe"
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)

driver.get(url="https://www.python.org")

driver.implicitly_wait(2)
# time.sleep(2)

html = driver.page_source

# price = driver.find_element(by=By.CLASS_NAME, value="currency plus currency-module_currency_29IIm")
#
# price = driver.find_elements(by=By.TAG_NAME, value="span")

# the Class name is : medium-widget event-widget last
#repalce the spaces with .
events = driver.find_elements(by=By.CSS_SELECTOR, value=".medium-widget.event-widget.last li")

for event in events:
    print(event.text)


# events_in_list = True
# events_list = {}
# try:
#     count = 1
#     while events_in_list:
#         print(f"checking for events {count}")
#         event = driver.find_element(by=By.XPATH,
#                                     value=f'//*[@id="content"]/div/section/div[2]/div[2]/div/ul/li[{count}]/a').text
#         event_time = driver.find_element(by=By.XPATH,
#                                          value=f'//*[@id="content"]/div/section/div[2]/div[2]/div/ul/li[{count}]/time').text
#         print(event)
#         print(event_time)
#         events_list[count-1] = {
#             "time": event_time,
#             "name": event
#         }
#         count += 1
#
# except NoSuchElementException:
#     print("no further events found")
#     events_in_list = False

# print(events_list)

driver.close()  # Closes the tab which was opened earlier
driver.quit()  # Quits the entire browser.
