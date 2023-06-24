from apps.app_1 import app as app_1
from werkzeug.middleware.dispatcher import DispatcherMiddleware

# En el caso de que quisiera agregar más aplicaciones debería realizarlo acá, asignando
# el path y la variable app de cada aplicación que se encuentra en el __init__.py
apps_pool = DispatcherMiddleware(app_1, {"/app_1": app_1})
