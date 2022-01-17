"""
Para ejecutarse se debe tener esto en la app
@app.cli.command()
def test():
    tests = unittest.TestLoader().discover('tests') #Directorio tests
    unittest.TextTestRunner().run(tests)

Instalar flask_testing y ejecutar con:
flask tests
"""

from flask_testing import TestCase
from flask import current_app, url_for
from main import app

class MainTest(TestCase):
    def create_app(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False

        return app

    def test_app_exists(self):
        self.assertIsNotNone(current_app)
    
    def test_app_in_test_mode(self):
        """Verifica si se encuentra en entorno de pruebas (Redundante la forma en que es colocado)
        """
        self.assertTrue(current_app.config['TESTING'], True)

    def test_index_redirects(self):
        response = self.client.get(url_for('index'))
        self.assertRedirects(response, url_for('hello'))

    def test_hello_get(self):
        response = self.client.get(url_for('hello'))
        self.assert200(response)

    def test_hello_post(self):
        response = self.client.post(url_for('hello'))
        self.assertTrue(response.status_code, 405)

    #Testing the blueprints
    def test_auth_blueprint_exists(self):
        self.assertIn('auth', self.app.blueprints)
        #Flask guarda todos los blueprints en app.blueprints
    
    def test_auth_login_get(self):
        response = self.client.get(url_for('auth.login')) #auth. porque es dentro de la carpeta
        self.assert200(response)

    def test_auth_login_template(self):
        self.client.get(url_for('auth.login')) #auth. porque es dentro de la carpeta
        self.assertTemplateUsed('login.html')

    def test_auth_login_post(self):
        fake_form = {
            'username':'fake',
            'password':'fake_pasword'
        }
        response = self.client.post(url_for('auth.login'), data=fake_form)
        self.assertRedirects(response, url_for('index'))