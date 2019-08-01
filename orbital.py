from selenium import webdriver
from selenium.webdriver.common.keys import Keys
# from selenium.common.exceptions import TimeoutException
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
import os
import time

driver = webdriver.Firefox()

driver.get("http://www.google.com")
window_before = driver.window_handles[0]


driver.execute_script("window.open('about:blank', 'tab2');")
# window_after = driver.window_handles[1]
driver.switch_to_window("tab2")
time.sleep(5)
driver.get("https://www.cnn.com/")

# driver.get("https://www.foxnews.com/")
# print(driver.title)
#
# driver.get("https://www.bbc.com/")
# print(driver.title)
