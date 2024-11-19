import os
import time
import pyautogui
from selenium import webdriver
from utils import constants
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from features.pages.loginPage import LoginPage

def before_all(context):
    context.evidence_path = "screenshots/"
    context.step_counter = 0
def before_scenario(context, scenario):

    if "mobile_required" in scenario.effective_tags:
        mobile_emulation = {
            "deviceMetrics": {"width": 390, "height": 844, "pixelRatio": 1, "mobile": True,
            "deviceScaleFactor": 50}, "userAgent": "Mozilla/5.0 (Linux; Android 9; Pixel 2 Build/PPR1.180610.009) "
            "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.92 Mobile Safari/537.36"
        }

        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("mobileEmulation", mobile_emulation )

        context.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    else:
        context.driver = webdriver.Chrome()

    context.driver.maximize_window()
    login_page = LoginPage(context.driver)
    if "login_required" in scenario.effective_tags:
        context.driver.get(login_page.baseURL)
        time.sleep(3)
        login_page.click_login()
        time.sleep(3)
        login_page.write_email(constants.email_registrado)
        login_page.write_password(constants.password)
        login_page.click_confirm_login()
        time.sleep(5)


def after_scenario(context, scenario):
    context.driver.close()
    print("Cierro el webDriver correctamente\n")


import os

def after_step(context, step):
    # Verifica si el escenario tiene la etiqueta específica
    if 'capture' in context.scenario.effective_tags:
        # Carpeta del feature
        feature_folder = os.path.join(context.evidence_path, context.feature.name)
        if not os.path.exists(feature_folder):
            os.makedirs(feature_folder)

        # Carpeta del escenario dentro de la carpeta del feature
        scenario_name = context.scenario.name.split('--')[0].strip()  # Elimina el identificador de versión
        scenario_folder = os.path.join(feature_folder, scenario_name)
        if not os.path.exists(scenario_folder):
            os.makedirs(scenario_folder)

        context.step_counter += 1  # Incrementa el contador

        # Ruta de la captura de pantalla dentro de la carpeta del escenario
        screenshot_path = os.path.join(scenario_folder, f"{context.step_counter:04d}_{step.name}.png")

        try:
            context.driver.save_screenshot(screenshot_path)
            print(f"Captura de pantalla guardada correctamente en: {screenshot_path}")
        except Exception as e:
            print(f"Error al guardar la captura de pantalla: {e}")


