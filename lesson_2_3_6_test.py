import math
import time

from selenium import webdriver
from selenium.webdriver.common.by import By


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


link = "https://suninjuly.github.io/redirect_accept.html"
browser = webdriver.Chrome()

try:
    browser.get(link)
    browser.implicitly_wait(5)
    browser.find_element(By.CSS_SELECTOR, "button.btn").click()
    new_winow = browser.window_handles[1]
    browser.switch_to.window(new_winow)
    x = browser.find_element(By.CSS_SELECTOR, "#input_value").text
    y = calc(x)
    browser.find_element(By.TAG_NAME, "input").send_keys(y)
    browser.find_element(By.CSS_SELECTOR, "button.btn").click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
