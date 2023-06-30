import time
from main import LoginPage, HomePage
from selenium import webdriver


driver = webdriver.Chrome()


def test_login_user():
    page = LoginPage(driver)
    page.go()
    page.input_user_name("student")
    page.input_password("Password123")
    page.click_submit_btn()
    time.sleep(2)
    homepage = HomePage(driver)
    assert homepage.heading_text == "Logged In Successfully"
