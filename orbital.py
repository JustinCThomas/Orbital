from selenium import webdriver

driver = webdriver.Firefox()

driver.get("https://www.cnbc.com/")
mainSection = driver.find_elements_by_class_name("HeroLedePlusThreeLeadItem-container")[0]
mainSection.click()

driver.execute_script("window.open('about:blank', 'tab2');")
driver.switch_to.window("tab2")
driver.get("https://www.cnn.com/")
mainSection = driver.find_elements_by_class_name("zn-banner")[0]
mainSection.click()

driver.execute_script("window.open('about:blank', 'tab3');")
driver.switch_to.window("tab3")
driver.get("https://www.foxnews.com/")
mainSection = driver.find_elements_by_class_name("main-content")[0].find_elements_by_class_name("story-1")[0]
mainSection.click()

driver.execute_script("window.open('about:blank', 'tab4');")
driver.switch_to.window("tab4")
driver.get("https://www.bbc.com/")
mainSection = driver.find_elements_by_class_name("module--promo")[0].find_elements_by_class_name("media-list__item--1")[0]

mainSection.click()
