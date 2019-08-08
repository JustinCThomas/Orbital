from selenium import webdriver
import time
import os

def move_to_new_tab(tab_num, website):
    driver.execute_script(f"window.open('about:blank', '{tab_num}');")
    driver.switch_to.window(tab_num)
    driver.get(website)
    time.sleep(3)

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

move_to_new_tab("tab2", "https://www.cnn.com/")
try:
    mainSection = driver.find_elements_by_class_name("zn-banner")[0]
    mainSection.click()
except Exception as e:
    mainSection = driver.find_elements_by_class_name("cn-list-hierarchical-xs")[0].find_elements_by_tag_name('li')[0]
    mainSection.click()
    
move_to_new_tab("tab3", "https://www.foxnews.com/")
mainSection = driver.find_elements_by_class_name("main-content")[0].find_elements_by_class_name("story-1")[0]
mainSection.click()

move_to_new_tab("tab4", "https://www.bbc.com/")
mainSection = driver.find_elements_by_class_name("module--promo")[0].find_elements_by_class_name("media-list__item--1")[0]
mainSection.click()

move_to_new_tab("tab5", "https://www.huffpost.com/")
mainSection = driver.find_element_by_id("zone-main").find_elements_by_class_name("card__headline__text")[0]
mainSection.click()
