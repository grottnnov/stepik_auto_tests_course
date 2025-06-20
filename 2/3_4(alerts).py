from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))
 

link = "http://suninjuly.github.io/alert_accept.html"

try:

    browser = webdriver.Chrome()
    browser.get(link)
    browser.find_element(By.CLASS_NAME, "btn.btn-primary").click()
    alert = browser.switch_to.alert
    alert.accept()

    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)
    input = browser.find_element(By.ID, "answer")
    input.send_keys(y)
    browser.find_element(By.CLASS_NAME, "btn.btn-primary").click()

finally:
   
    time.sleep(30)
    browser.quit()


