from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import math
import time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    num1 = browser.find_element(By.ID, "num1")
    num2 = browser.find_element(By.ID, "num2")
    x = num1.text
    y = num2.text
    z = int(x)+int(y)

    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_visible_text(str(z))

    submit = browser.find_element(By.TAG_NAME, "button")
    submit.click()

    time.sleep(1)

finally:
    time.sleep(5)
    browser.quit()

    
    
