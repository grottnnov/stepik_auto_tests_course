from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try: 
    
    link = "https://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)
    input = browser.find_element(By.ID, "answer")
    input.send_keys(y)
    option1 = browser.find_element(By.CLASS_NAME, "form-check-label")
    option1.click()
    option2 = browser.find_element(By.ID, "robotsRule")
    option2.click()
    option3 = browser.find_element(By.XPATH, "/html/body/div/form/button")
    option3.click()

finally:
    
    time.sleep(30)
    browser.quit()

