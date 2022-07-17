from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import math
import time
import os

try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    first = browser.find_element(By.NAME, "firstname")
    first.send_keys("Damir")
    
    last = browser.find_element(By.NAME, "lastname")
    last.send_keys('Les')

    email = browser.find_element(By.NAME, "email")
    email.send_keys('lesk@mail.ru')

    currend_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(currend_dir, "step.txt")
    attach = browser.find_element(By.ID, "file")
    attach.send_keys(file_path)
    
    button = browser.find_element_by_tag_name("button")
    button.click()
    
    time.sleep(1)

finally:
    time.sleep(5)
    browser.quit()

    
    
