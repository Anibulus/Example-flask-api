from crypt import methods
from threading import currentThread
import unittest
from flask import request, make_response, redirect, render_template, session, url_for, flash
from flask_login import login_required, current_user
from app import create_app
from app.forms import LoginForm, TodoForm
from app.firestore_service import delete_todo, get_users, get_todos, put_todo


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
@login_required
def hello():
    user_ip = session.get('user_ip')
    login_form = LoginForm()
    username = current_user.id
    #username = session.get('username')
    todo_form = TodoForm()

    context = {
        'user_ip':user_ip,
        'todos':get_todos(username),
        'login_form':login_form,
        'username':username,
        'todo_form': todo_form
    }

    if todo_form.validate_on_submit():
        put_todo(user_id=username, description=todo_form.description.data)

        flash('Tu tarea se creo con exito')

        return redirect(url_for('hello.html'))

    users = get_users()

    for user in users:
        print(user)
        print(user.id)
        print(user.to_dict().get('password'))

    return render_template('hello.html',**context)

@app.route('/todos/delete/<todo_id>', methods=['POST'])
def delete(todo_id):
    user_id = current_user.id
    delete_todo(user_id=user_id, todo_id=todo_id)

    return redirect(url_for('hello.html'))


#if __name__ == '__main__':
#    app.run(debug=True)#template_folder='../templates', static_folder='../static')