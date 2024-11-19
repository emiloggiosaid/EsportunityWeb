from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils import constants
from selenium.webdriver.common.by import By


class OportunidadesPage:

    def __init__(self, driver):
        self.driver = driver
        self.baseURL = "https://esportunity.com/"
        self.oportunidadesURL = "/opportunities"
        self.oportunidades_btn = "//a[@href='/opportunities']"
        self.segunda_oportunidad_btn = "(//a//li)[2]"
        self.postularme_btn = "//button[text()='Postularme']"

    def click_oportunidades(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.oportunidades_btn)))
        element.click()
    def check_url_seccion_oportunidades(self):
        WebDriverWait(self.driver, 10).until(EC.url_contains(self.oportunidadesURL))
    def click_segunda_oportunidad_btn(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.segunda_oportunidad_btn)))
        element.click()
    def check_postularme_btn(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.postularme_btn)))
        element.is_displayed()
