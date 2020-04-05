from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    x = browser.find_element_by_id("input_value").text
    res = calc(x)
    
    input1 = browser.find_element_by_id("answer").send_keys(res)
    
    # Скролл до кнопки
    button = browser.find_element_by_tag_name("button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    
    browser.find_element_by_css_selector("[for=\"robotCheckbox\"]").click()
    browser.find_element_by_css_selector("[for=\"robotsRule\"]").click()
   
   # Отправляем заполненную форму
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
