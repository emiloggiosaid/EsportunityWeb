# EsportunityWeb

Descripción:
Este repositorio contiene los casos de prueba automatizados de la Web de Esportunity. Se encuentran escritos en python, selenium y behave.

Requisitos para ejecutar las pruebas:
- Tener Instalado:

Python

Pycharm

Selenium

Behave

Instalaciones:
Nombre Comandos o links

python	https://www.python.org/downloads/

pycharm	https://www.jetbrains.com/es-es/pycharm/download/#section=windows

Ejecutar en terminal de pycharm:

Para selenium:

pip install selenium 

Para behave:

pip install behave

Para reporte de los casos:

pip install behave-html-pretty-formatter


Versiones:

Python 3.11.2

Pycharm 2023

Selenium:  4.26.1

Behave: 1.2.6

Arbol de archivos:

/features: contiene el archivo environment(donde se definen los hooks) y cada uno de los features(casos de prueba)

/features/page: contiene los archivos page (donde se guardan los elementos webs, sus xpath o locators y los metodos y funciones logicas que se relizan en la web para luego ser utilizadas en los steps) 

/features/steps: contiene los archivos steps en los cuales se invocan las funciones que realizan comportamientos y chequeos de la web. 

/utils: contiene herramientas utiles para la ejecucion de las pruebas.

/utils/constants: archivo txt donde se guardan las constantes. 

/behave.ini: archivo donde se define el formato de los reportes.

Aclaraciones importantes:

Para ejecutar los casos de prueba individualmente:
1-Descargar Proyecto 
2-Instalar todo lo detallado anteriormente
3- Abrir Pycharm e importar el proyecto descargado
4- Abrir la terminal y ejecutar el siguiente script:
 behave features/"reemplace este texto por nombre del caso de prueba o feature"
 
Para ejecutar la testsuite completa(todos los casos de prueba desarrollados) ejecutar el siguiente script:
behave features/     

Para ejecutar y crear un reporte de la ejecucion:

behave -f html-pretty -o reporte-completo.html (reporte de todos los casos de pruebas existentes)

behave features/"cambie este texto por el nombre del caso de prueba" -f html-pretty -o reporte-completo.html (reporte de un caso de prueba en particular) 


