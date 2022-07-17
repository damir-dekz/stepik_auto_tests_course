from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = 'http://suninjuly.github.io/alert_accept.html'
    browser = webdriver.Chrome()
    browser.get(link)

    submit1 = browser.find_element(By.CSS_SELECTOR, ".container [type='submit']")
    submit1.click()

    prompt = browser.switch_to.alert
    prompt.accept()

    time.sleep(1)

    x_value = browser.find_element(By.ID, 'input_value')
    x = x_value.text
    y = calc(x)

    input1 = browser.find_element(By.ID, 'answer')
    input1.send_keys(y)

    submit2 = browser.find_element(By.CSS_SELECTOR, ".form-group button")
    submit2.click()

    time.sleep(1)

finally:
    time.sleep(5)
    browser.quit()
    
