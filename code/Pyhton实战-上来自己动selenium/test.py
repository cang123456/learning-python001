import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Edge()
wait = WebDriverWait(driver,10)



driver.get("https://www.bilibili.com")




input = wait.until(EC.element_to_be_clickable((By.CLASS_NAME,'nav-search-input')))
input.send_keys('苍老师照片')
sub = wait.until(EC.element_to_be_clickable((By.ID,'nav-search-btn')))
sub.click()




time.sleep(3300)



























