from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = 'http://suninjuly.github.io/explicit_wait2.html'
    browser = webdriver.Chrome()
    browser.get(link)

    submit1 = browser.find_element(By.ID, "book")
    wait = WebDriverWait(browser, 12)
    wait.until(EC.text_to_be_present_in_element((By.ID, 'price'), '100'))
    submit1.click()

    x_value = browser.find_element(By.ID, 'input_value')
    x = x_value.text
    y = calc(x)

    input1 = browser.find_element(By.ID, 'answer')
    input1.send_keys(y)

    submit2 = browser.find_element(By.CSS_SELECTOR, "#solve")
    submit2.click()

    time.sleep(1)

finally:
    time.sleep(5)
    browser.quit()
    
