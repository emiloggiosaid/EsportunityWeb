import time

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils import constants
from selenium.webdriver.common.by import By


class LoginPage:

    def __init__(self, driver):
        self.driver = driver
        self.baseURL = "https://esportunity.com/"
        self.loginURL = "https://esportunity.com/login"
        self.homeURL = ""
        self.login_btn = "//a[@href='/login']"
        self.email_input = "email"
        self.password_input = "password"
        self.confirm_login_btn = "//button[@type='submit']"

    def check_web_base(self):
        WebDriverWait(self.driver, 10).until(EC.url_to_be(self.baseURL))
    def click_login(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.login_btn)))
        element.click()
    def check_web_login(self):
        WebDriverWait(self.driver, 10).until(EC.url_to_be(self.loginURL))
    def write_email(self, email):
        self.driver.find_element(By.NAME, self.email_input).send_keys(email)
    def write_password(self, password):
        self.driver.find_element(By.NAME, self.password_input).send_keys(password)
    def click_confirm_login(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.confirm_login_btn)))
        element.click()
