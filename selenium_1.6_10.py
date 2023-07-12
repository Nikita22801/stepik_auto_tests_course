from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try: 
    link = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    name = browser.find_element(By.CSS_SELECTOR, "[placeholder='Input your name']")
    name.send_keys("Sasha")
    email = browser.find_element(By.CSS_SELECTOR, "[placeholder='Input your email']")
    email.send_keys("sasha@mail.ru")
    phone = browser.find_element(By.CSS_SELECTOR, "[placeholder='Input your phone']")
    phone.send_keys("+79177542011")
    address = browser.find_element(By.CSS_SELECTOR, "[placeholder='Input your address']")
    address.send_keys("Malinovskogo street, 36")
    
    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
