from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import os 

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    browser.find_element_by_xpath('//div/label[text()="First name* "]/following-sibling::* [@name="firstname"]').send_keys("Andrey")
    browser.find_element_by_xpath('//div/label[text()="Last name*"]/following-sibling::* [@name="lastname"]').send_keys("Demedyuk")
    browser.find_element_by_xpath('//div/label[text()="Email * "]/following-sibling::* [@name="email"]').send_keys("test@mail.ru")
    
    # выбираем файл и прикрепляем к странице
    element = browser.find_element_by_id("file")
    current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
    file_path = os.path.join(current_dir, 'file.txt')           # добавляем к этому пути имя файла 
    element.send_keys(file_path)
    
    # Отправляем заполненную форму
    button = browser.find_element_by_class_name("btn.btn-primary")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
