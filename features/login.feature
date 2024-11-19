Feature: Login Esportunity Web

  Scenario Outline: Como usuario registrado en la pagina de Esportunity quiero iniciar sesión

    Given Se encuentra en la web de Esportunity
    When Hace click en Login
    And  Escribe <Email> en el campo Email
    And  Escribe <Password> en el campo Password
    And  Hace click en Login luego de ingresar los datos
    Then Visualiza el home con sesion iniciada

    Examples:
    |Email            |Password   |
    |lpdaemi@gmail.com|CocoNube12$|