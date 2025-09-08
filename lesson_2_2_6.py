from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


link = "https://suninjuly.github.io/execute_script.html"
browser = webdriver.Chrome()

try:
    browser.get(link)
    x = browser.find_element(By.CSS_SELECTOR, "#input_value").text
    y = calc(x)
    browser.find_element(By.TAG_NAME, "input").send_keys(y)
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    browser.find_element(By.CSS_SELECTOR, "#robotCheckbox").click()
    browser.find_element(By.CSS_SELECTOR, "#robotsRule").click()
    button.click()


finally:
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
