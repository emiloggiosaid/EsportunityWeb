import time

from behave import *
from features.pages.oportunidadesPage import OportunidadesPage

@when("Hace click en Oportunidades")
def step_impl(context):
    oportunidades = OportunidadesPage(context.driver)
    oportunidades.click_oportunidades()
@step("Chequea el correcto redireccionamiento a la web de Oportunidades")
def step_impl(context):
    oportunidades = OportunidadesPage(context.driver)
    time.sleep(3)
    oportunidades.check_url_seccion_oportunidades()
@step("Hace click en la segunda oportunidad disponible")
def step_impl(context):
    oportunidades = OportunidadesPage(context.driver)
    oportunidades.click_segunda_oportunidad_btn()

@then("Visualiza el boton de postulacion de la segunda oportunidad")
def step_impl(context):
    oportunidades = OportunidadesPage(context.driver)
    oportunidades.check_postularme_btn()


