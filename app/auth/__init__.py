from flask import Blueprint

#Todas las rutas que empiecen con /auth van a ser dirigidas a este blueprint
auth = Blueprint('auth',__name__,url_prefix='/auth')

from . import views