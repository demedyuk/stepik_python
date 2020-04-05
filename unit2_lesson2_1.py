from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    num1 = browser.find_element_by_id("num1")
    num2 = browser.find_element_by_id("num2")
    
    sum = int(num1.text) + int(num2.text)
    print(sum)
    
    # Выбор правильного ответа из списка
    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(str(sum))
    
    # Отправляем заполненную форму
    button = browser.find_element_by_class_name("btn.btn-default")
    button.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
