import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

link = "https://suninjuly.github.io/file_input.html"
browser = webdriver.Chrome()

try:

    browser.get(link)

    input1 = browser.find_element(By.TAG_NAME, "input")
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.CSS_SELECTOR, "[name='lastname']")
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.CSS_SELECTOR, "[name='email']")
    input3.send_keys("test@gmail.com")
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir,
                             'test_file.txt')  # собирает путь из исполняемого файла (.ру) и файла которой лежит в этой же папке
    input4 = browser.find_element(By.CSS_SELECTOR, "#file")
    input4.send_keys(file_path)
    #  input4.send_keys("C:/MyPythonProjects/python/tests/test_file.txt") можно и так, если файл лежит в другой папке
    browser.find_element(By.CSS_SELECTOR, "button.btn").click()

finally:
    time.sleep(5)
    browser.quit()
