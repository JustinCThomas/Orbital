from selenium import webdriver
import time
import os

driver = webdriver.Firefox()

try:
    extensions_path = os.environ["FireFox Extensions"]
    driver.install_addon(f'{extensions_path}\\uBlock0@raymondhill.net.xpi' , temporary=True)
except Exception as e:
    print("uBlock Extension was not installed.")
    print("Pages may load more slowly.")
    print("Threw exception " + str(e))

driver.get("https://www.cnbc.com/")
mainSection = driver.find_elements_by_class_name("HeroLedePlusThreeLeadItem-container")[0]
mainSection.click()

driver.execute_script("window.open('about:blank', 'tab2');")
driver.switch_to.window("tab2")
driver.get("https://www.cnn.com/")
time.sleep(3)
mainSection = driver.find_elements_by_class_name("zn-banner")[0]
mainSection.click()

driver.execute_script("window.open('about:blank', 'tab3');")
driver.switch_to.window("tab3")
driver.get("https://www.foxnews.com/")
time.sleep(3)
mainSection = driver.find_elements_by_class_name("main-content")[0].find_elements_by_class_name("story-1")[0]
mainSection.click()

driver.execute_script("window.open('about:blank', 'tab4');")
driver.switch_to.window("tab4")
time.sleep(3)
driver.get("https://www.bbc.com/")
mainSection = driver.find_elements_by_class_name("module--promo")[0].find_elements_by_class_name("media-list__item--1")[0]
mainSection.click()
