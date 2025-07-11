from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math

def calc(sum):
    return int(x) + int(y)

try: 
    
    link = "https://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element(By.ID, "num1")
    y_element = browser.find_element(By.ID, "num2")
    x = x_element.text
    y = y_element.text
    z = calc(sum)
    
    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(str(z))     
    browser.find_element(By.XPATH, "/html/body/div/form/button").click()

finally:
    
    time.sleep(30)
    browser.quit()


