from flask import request, make_response, redirect, render_template, session, url_for, flash
import unittest

from app import create_app
from app.forms import LoginForm


app = create_app()

@app.cli.command()
def test():
    tests = unittest.TestLoader().discover('tests') #Directorio test
    unittest.TextTestRunner().run(tests) #flask tests

#Muestra paginas de error haciendo render del html, reciben el numero del error
@app.errorhandler(404)
def not_found(error):
    render = render_template('404.html', error=error)
    return render

@app.errorhandler(500)
def internal_server_error(error):
  return render_template('500.html')


#Path operations de flask
@app.route('/')
def index():
    user_ip = request.remote_addr 
    response = make_response(redirect('/hello'))
    session['user_ip'] = user_ip
    #response.set_cookie('user_ip', user_ip)
    return response


todos = ['TODO 1', 'TODO 2', 'TODO 3']

@app.route('/hello', methods=['GET','POST'])
def hello():
    user_ip = session.get('user_ip')
    login_form = LoginForm()
    username = session.get('username')

    context = {
        'user_ip':user_ip,
        'todos':todos,
        'login_form':login_form,
        'username':username
    }

    return render_template('hello.html',**context)


#if __name__ == '__main__':
#    app.run(debug=True)#template_folder='../templates', static_folder='../static')