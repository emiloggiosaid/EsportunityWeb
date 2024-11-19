import time
from behave import *
from features.pages.signupPage import SignupPage

@when("Hace click en Crear cuenta")
def step_impl(context):
    signup_page = SignupPage(context.driver)
    signup_page.click_crear_cuenta()
    signup_page.check_web_signup()


@step("Escribe Email")
def step_impl(context):
    signup_page = SignupPage(context.driver)
    signup_page.write_email()
    time.sleep(3)

@step("Escribe Password")
def step_impl(context):
    signup_page = SignupPage(context.driver)
    signup_page.write_password()
    time.sleep(3)


@step("Escribe Confirmacion de password")
def step_impl(context):
    signup_page = SignupPage(context.driver)
    signup_page.write_confirm_password()
    time.sleep(3)


@step("Hace click en Crear nueva cuenta")
def step_impl(context):
    signup_page = SignupPage(context.driver)
    signup_page.click_crear_nueva_cuenta()
    time.sleep(3)
@step("Ingresa codigo de email")
def step_impl(context):
    time.sleep(60)

@then("Visualiza mensaje de cuenta validada con exito")
def step_impl(context):
    signup_page = SignupPage(context.driver)
    signup_page.check_mensaje_cuenta_validada()
    time.sleep(10)


