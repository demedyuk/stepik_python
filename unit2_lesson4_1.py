from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()

browser.get("http://suninjuly.github.io/explicit_wait2.html")

# говорим Selenium проверять в течение 12 секунд, пока цена не будет равна $100
WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID,"price"), "$100"))

# Кликаем на кнопку
browser.find_element_by_id("book").click()

#Решаем математическую задачу и вводим ответ
x = browser.find_element_by_id("input_value")
res = calc(x.text)

browser.find_element_by_id("answer").send_keys(res)
    

# Отправляем заполненную форму
button = WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable((By.ID, "solve"))
    )
button.click()


# ожидание чтобы визуально оценить результаты прохождения скрипта
time.sleep(5)
# закрываем браузер после всех манипуляций
browser.quit()