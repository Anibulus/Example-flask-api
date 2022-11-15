export FLASK_APP=main.py
echo $FLASK_APP
export FLASK_DEBUG=0
echo $FLASK_DEBUG
export FLASK_ENV=development
echo $FLASK_ENV
flask run

source run.sh


Flask esta configurado para buscar en un directorio los templates
Flask es ligero, pero puede crecer tanto como se requiera, y con ello instalacion de sus librerias:

Flask-Bootstrap #TODO Aprender a usar bootstrap 4 y 5 en flask
Flask-WTF #What the forms
Flask-Testing (Tambien se puede unit-test de python) #User comando `flask test`

Nota de las blueprints: Los blueprints funcionan similar a las apps de django

El archivo que inicializa el proyecto correctamente es app/__init__.py y luego es usado en main.py con el contenido  `app = create_app()`

# TODO
Revisar como implementar [https://platzi.com/tutoriales/1540-flask/7112-conectando-aplicacion-con-base-de-datos-relacional/](SQLAlchemy) con Flask