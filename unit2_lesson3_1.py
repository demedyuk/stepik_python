from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import os 
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    browser.find_element_by_tag_name("button").click()
    
    #Ловим allert
    confirm = browser.switch_to.alert
    confirm.accept()
    
    x = browser.find_element_by_id("input_value")
    print(x.text)
    res = calc(x.text)
    print("res = " + res)
    
    browser.find_element_by_id("answer").send_keys(res)
    
    # Отправляем заполненную форму
    button = browser.find_element_by_class_name("btn.btn-primary")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
