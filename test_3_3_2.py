import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()


class TestAbs:
    def test_last_name(self):
        browser.get("https://suninjuly.github.io/registration1.html")
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
        assert "Congratulations! You have successfully registered!" == welcome_text
        time.sleep(5)
        browser.quit()

    def test_without_ast_name(self):
        browser.get("https://suninjuly.github.io/registration2.html")
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
        assert "Congratulations! You have successfully registered!" == welcome_text
        time.sleep(5)
        browser.quit()


if __name__ == "__main__":
    pytest.main()
