from selenium.webdriver.common.by import By
from selenium import webdriver
import time
import os

import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    first_name = browser.find_element(By.CSS_SELECTOR, "[placeholder='Enter first name']")
    first_name.send_keys("Sasha")
    last_name = browser.find_element(By.CSS_SELECTOR, "[placeholder='Enter last name']")
    last_name.send_keys("Sasha")

    email = browser.find_element(By.CSS_SELECTOR, "[placeholder='Enter email']")
    email.send_keys("Sasha")


    browser.find_element(By.ID, "file").send_keys("C:/Users/79182/Desktop/stepik.txt")
    
    
    submit = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
    submit.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
