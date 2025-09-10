import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


def last_name(link):
    browser = webdriver.Chrome()
    browser.get(link)
    try:
        browser.implicitly_wait(1)
        input1 = browser.find_element(By.CSS_SELECTOR, "div.first_block input.first")
        input1.send_keys("Dmytro")
        input2 = browser.find_element(By.CSS_SELECTOR, "div.first_block input.second")
        input2.send_keys("Test")
        input3 = browser.find_element(By.CSS_SELECTOR, "div.first_block input.third")
        input3.send_keys("test@gmail.com")
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()
        time.sleep(1)
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elt.text
        return welcome_text
    finally:
        browser.quit()


def test_link1():
    link = "https://suninjuly.github.io/registration1.html"
    assert last_name(link) == "Congratulations! You have successfully registered!", "Error message"


def test_link2():
    link = "https://suninjuly.github.io/registration2.html"
    assert last_name(link) == "Congratulations! You have successfully registered!", "Error message"


if __name__ == "__main__":
    pytest.main()
