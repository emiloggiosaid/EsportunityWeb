import time
from behave import *
from features.pages.loginPage import LoginPage

@given("Se encuentra en la web de Esportunity")
def step_impl(context):
    login = LoginPage(context.driver)
    context.driver.get(login.baseURL)
    login.check_web_base()

@when("Hace click en Login")
def step_impl(context):
    login = LoginPage(context.driver)
    login.click_login()
    login.check_web_login()

@step("Escribe {Email} en el campo Email")
def step_impl(context, Email):
    login = LoginPage(context.driver)
    login.write_email(Email)
    time.sleep(3)

@step("Escribe {Password} en el campo Password")
def step_impl(context, Password):
    login = LoginPage(context.driver)
    login.write_password(Password)
    time.sleep(3)

@step("Hace click en login luego de ingresar los datos")
def step_impl(context):
    login = LoginPage(context.driver)
    login.click_confirm_login()
    time.sleep(3)
@then("Visualiza el home con sesion iniciada")
def step_impl(context):
    login = LoginPage(context.driver)
    login.check_web_base()
    time.sleep(5)



