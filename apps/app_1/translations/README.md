translation: https://python-babel.github.io/flask-babel/

### Inicio de la traducción:

 - Para reconocer las palabras:
 `pybabel extract -F babel.cfg -k lazy_gettext -o messages.pot .` 
 - Para crear las carpetas por idioma:
 `pybabel init -i messages.pot -d translations -l es`
 - Compilar las traducciones:
 `pybabel compile -d translations`
 - 
### Para agregar palabras a la traducción:

 - Para reconocer palabras: 
 `pybabel extract -F babel.cfg -k lazy_gettext -o messages.pot .`
 - Para actualizar carpeta de traducciones sin perder lo anterior: 
 `pybabel update -i messages.pot -d translations`
 - Compilar las traducciones: 
 `pybabel compile -d translations`
