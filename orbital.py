from selenium import webdriver
import time

driver = webdriver.Firefox()

driver.get("https://www.cnbc.com/")


driver.execute_script("window.open('about:blank', 'tab2');")
driver.switch_to.window("tab2")
driver.get("https://www.cnn.com/")

driver.execute_script("window.open('about:blank', 'tab3');")
driver.switch_to.window("tab3")
driver.get("https://www.foxnews.com/")

driver.execute_script("window.open('about:blank', 'tab4');")
driver.switch_to.window("tab4")
driver.get("https://www.bbc.com/")
