Feature: Seccion Oportunidades

  @login_required #Hook(se iniciar sesión automaticamente antes de ejecutar el caso de prueba)
  Scenario: Como usuario con sesión iniciada en Esportunity quiero ingresar a la sección
  Oportunidades y seleccionar la segunda oportunidad para ver sus detalles

    Given Se encuentra en la web de Esportunity
    When Hace click en Oportunidades
    And Chequea el correcto redireccionamiento a la web de Oportunidades
    And  Hace click en la segunda oportunidad disponible
    Then Visualiza el boton de postulacion de la segunda oportunidad