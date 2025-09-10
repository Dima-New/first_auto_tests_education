import math
import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


def test_wait_until_ec():
    link = "https://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()

    try:
        browser.get(link)
        WebDriverWait(browser, 12).until(
            EC.text_to_be_present_in_element((By.CSS_SELECTOR, "h5#price"), text_="$100")
        )
        browser.find_element(By.CSS_SELECTOR, "button#book").click()
        x = browser.find_element(By.CSS_SELECTOR, "#input_value").text
        y = calc(x)
        browser.find_element(By.TAG_NAME, "input").send_keys(y)
        browser.find_element(By.CSS_SELECTOR, "button#solve").click()

    finally:
        time.sleep(5)
        # закрываем браузер после всех манипуляций
        browser.quit()

    if __name__ == "__main__":
        pytest.main()
