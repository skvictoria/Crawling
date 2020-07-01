from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


path = r"C:\Users\6\Downloads\chromedriver_win32 (1)\chromedriver.exe"

driver = webdriver.Chrome(path)
driver.get("https://www.facebook.com/")

driver.find_element_by_id("email").send_keys("iwbisnu@gmail.com")
driver.find_element_by_id("pass").send_keys("~~~~~~~~~~~~")
driver.find_element_by_id("pass").send_keys(Keys.ENTER)

time.sleep(3)
driver.find_element_by_xpath('//*[@id="mount_0_0"]/div/div/div[1]/div[2]/div[2]/div/div/div[1]/div/div[3]/label/input').send_keys("왕십리 맛집")
driver.find_element_by_xpath('//*[@id="mount_0_0"]/div/div/div[1]/div[2]/div[2]/div/div/div[1]/div/div[3]/label/input').send_keys(Keys.ENTER)

time.sleep(3)
driver.find_element_by_xpath('//*[@id="mount_0_0"]/div/div/div[1]/div[3]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div[1]/div/div/div/div/div[1]/div/div[1]/div/div/div/svg/g/image').click()
#time.sleep(2)
#driver.find_element_by_xpath('//*[@id="mount_0_0"]/div/div/div[1]/div[3]/div/div/div[2]/div/div[4]/div[1]/div/div/div/div/div/div/div/div/div[1]/div/div[2]/div/div[4]/div/div/div[1]/div[2]/div/span[1]/div/div/span/div[1]/div').click()
