from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

import time

import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()

browser.get("http://suninjuly.github.io/explicit_wait2.html")

# говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
price = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), '$100')
    )
browser.find_element(By.ID, "book").click()

time.sleep(1)
x = browser.find_element(By.ID, "input_value")
x = x.text
value = calc(x)
answer = browser.find_element(By.ID, "answer")
answer.send_keys(value)
    
submit = browser.find_element(By.CSS_SELECTOR, "[type='submit']")
submit.click()

time.sleep(10)
# закрываем браузер после всех манипуляций
browser.quit()

#message = browser.find_element(By.ID, "verify_message")

#assert "successful" in message.text
