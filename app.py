from flask import Flask, request, render_template
from connection import connect
from models import User


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('base.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    message = None
    connection = connect()
    cursor = connection.cursor()
    if request.method == 'POST':
        new_user = User(request.form['username'], request.form['first_name'], request.form['last_name'], request.form['password'])
        adding_user = new_user.add_user(cursor)
        if adding_user == 'user_added':
            message = 'User added to data base'

    connection.close()

    return render_template('register.html', message=message)

@app.route('/users')
def user():
    return render_template('users.html')


if __name__ == '__main__':
    app.run()
