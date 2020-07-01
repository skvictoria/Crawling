# first need to install selenium and install chrome driver

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

path = r"C:\Users\6\Downloads\chromedriver_win32 (1)\chromedriver.exe"
driver = webdriver.Chrome(path)

driver.get("https://www.naver.com")
driver.find_element_by_xpath('//*[@id="account"]/a').click()
#driver.find_element_by_class_name("link_login").click()
driver.find_element_by_id("id").send_keys("sk_victoria")
driver.find_element_by_id("pw").send_keys("###########")
driver.find_element_by_id("pw").send_keys(Keys.ENTER)
#driver.find_element_by_id("log.login").click()

driver.find_element_by_tag_name("body").send_keys(Keys.PAGE_DOWN)
