Feature: SignUp Esportunity Web

  Scenario: Como usuario no registrado en la pagina de Esportunity quiero registrarme

    Given Se encuentra en la web de Esportunity
    When Hace click en Crear cuenta
    And  Escribe Email
    And  Escribe Password
    And  Escribe Confirmacion de password
    And  Hace click en Crear nueva cuenta
    And  Ingresa codigo de email
    Then Visualiza mensaje de cuenta validada con exito