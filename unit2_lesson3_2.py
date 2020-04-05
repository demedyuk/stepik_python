from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import os 
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    browser.find_element_by_tag_name("button").click()
    
    #Переключаемся на вторую вкладку
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    
    x = browser.find_element_by_id("input_value")
    res = calc(x.text)
    
    browser.find_element_by_id("answer").send_keys(res)
    
    # Отправляем заполненную форму
    button = browser.find_element_by_class_name("btn.btn-primary")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
