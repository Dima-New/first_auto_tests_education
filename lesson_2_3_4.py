import math
import time

from selenium import webdriver
from selenium.webdriver.common.by import By


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


link = "https://suninjuly.github.io/alert_accept.html"
browser = webdriver.Chrome()

try:
    browser.get(link)
    browser.find_element(By.CSS_SELECTOR, "button.btn").click()
    browser.switch_to.alert.accept()
    x = browser.find_element(By.CSS_SELECTOR, "#input_value").text
    y = calc(x)
    browser.find_element(By.TAG_NAME, "input").send_keys(y)
    browser.find_element(By.CSS_SELECTOR, "button.btn").click()

finally:
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
