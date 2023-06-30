import time

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


URL = 'https://practicetestautomation.com/practice-test-login/'

driver = webdriver.Chrome()
driver.maximize_window()
driver.get(URL)


# comment 2
def input_user_name(username):
    x_path = '//input[@id="username"]'
    locator = (By.XPATH, x_path)
    elm = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(locator))
    elm.send_keys(username)
    return None


def input_password(password):
    x_path = '//input[@id="password"]'
    locator = (By.XPATH, x_path)
    elm = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(locator))
    elm.send_keys(password)
    return None


def click_submit_btn():
    x_path = '//button[@id="submit"]'
    locator = (By.XPATH, x_path)
    elm = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(locator))
    # elm = driver.find_element(locator)
    elm.click()
    return None


if __name__ == "__main__":
    input_user_name("student")
    input_password("Password123")
    click_submit_btn()
    time.sleep(5)
