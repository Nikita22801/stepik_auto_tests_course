from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    iwant = browser.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    browser.switch_to.window(browser.window_handles[1])
    # Ваш код, который заполняет обязательные поля
    time.sleep(1)
    x = browser.find_element(By.ID, "input_value")
    x = x.text
    value = calc(x)
    answer = browser.find_element(By.ID, "answer")
    answer.send_keys(value)
    
    submit = browser.find_element(By.CSS_SELECTOR, "[type='submit']")
    submit.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
