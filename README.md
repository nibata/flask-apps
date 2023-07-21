# App flask molde
Se crea una aplicación flask que no requiere base de datos. Esto quiere decir que todo requisito de datos se satisface mediante API.
En este caso la aplicación se conecta e identifica mediante la API generada por el proyecto [API DataMantainer](https://github.com/nibata/api-datamantainer) el cual es un proyecto que permite generar el desarrollo de una base de datos y servir dichos datos como servicios web (FastAPI).

Para iniciar la aplicación, además de requerir que el proyecto de API DataMantainer, esté funcionando, se inicia mediante `flask run`

Variables de entorno requeridas:

 - SECRET_KEY: Lo que quieras agregar en este punto
 - FLASK_DEBUG: 1 si es desarrollo
 - APP_NAME: Como quieras llamar a la aplicación 
 - DB_API_URL: URL donde está la API que presta servicios de datos a la aplicación
 - JWT_KEY: Mismo key con que se levanta el servicio de API DataMantainer (a mejorar)
 - JWT_ALGORITHM: Mismo algoritmo con el que se levanta el servicio de API DataMantainer
 - BABEL_DEFAULT_LOCALE: código de idioma con el que se levanta la aplicación (no es del todo necesario, ya que por defecto busca el que mejor se adapte al computador)