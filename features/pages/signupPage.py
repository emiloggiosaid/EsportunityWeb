from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils import constants
from selenium.webdriver.common.by import By

class SignupPage:

    def __init__(self, driver):
        self.driver = driver
        self.baseURL = "https://esportunity.com/"
        self.singUpURL = "https://esportunity.com/sign-up"
        self.crear_cuenta_btn = "//a[text()='Crear cuenta']"
        self.email_input = "email"
        self.password_input = "password"
        self.confirm_pass_input = "confirmPassword"
        self.crear_nueva_cuenta_btn = "//button[@type='submit']"
        self.mensaje_cuenta_validada = "//p[contains(text(),'Tu cuenta ha sido validada')]"

    def check_web_base(self):
        WebDriverWait(self.driver, 10).until(EC.url_to_be("https://esportunity.com/"))
    def click_crear_cuenta(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.crear_cuenta_btn)))
        element.click()
    def check_web_signup(self):
        WebDriverWait(self.driver, 10).until(EC.url_to_be("https://esportunity.com/sign-up"))
    def write_email(self):
        self.driver.find_element(By.NAME, self.email_input).send_keys(constants.email_no_registrado)
    def write_password(self):
        self.driver.find_element(By.NAME, self.password_input).send_keys(constants.password)
    def write_confirm_password(self):
        self.driver.find_element(By.NAME, self.confirm_pass_input).send_keys(constants.password)
    def click_crear_nueva_cuenta(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.crear_nueva_cuenta_btn)))
        element.click()
    def check_mensaje_cuenta_validada(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.mensaje_cuenta_validada)))
        element.click.is_displayed()

