import time

from selenium import webdriver


driver = webdriver.Edge()

driver.get("https://www.bilibili.com")


input = driver.find_element('class name','nav-search-input')

input.send_keys('苍老师照片')

sub = driver.find_element('id','nav-searchform')
sub.click()


time.sleep(33)



























