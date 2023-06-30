from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


URL = 'https://practicetestautomation.com/practice-test-login/'


class LoginPage:

    def __init__(self, driver):
        self.driver = driver

    def go(self):
        self.driver.maximize_window()
        self.driver.get(URL)

    def input_user_name(self, username):
        x_path = '//input[@id="username"]'
        locator = (By.XPATH, x_path)
        elm = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
        elm.send_keys(username)
        return None

    def input_password(self, password):
        x_path = '//input[@id="password"]'
        locator = (By.XPATH, x_path)
        elm = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
        elm.send_keys(password)
        return None

    def click_submit_btn(self):
        x_path = '//button[@id="submit"]'
        locator = (By.XPATH, x_path)
        elm = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
        elm.click()
        return None


class HomePage:

    def __init__(self, driver):
        self.driver = driver

    @property
    def heading_text(self):
        x_path = '//h1[@class="post-title"]'
        locator = (By.XPATH, x_path)
        elm = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
        return elm.text


if __name__ == "__main__":
    pass
