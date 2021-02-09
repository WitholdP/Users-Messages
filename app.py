from flask import Flask, request, render_template


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('base.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    return render_template('register.html')

@app.route('/users')
def user():
    return render_template('users.html')


if __name__ == '__main__':
    app.run()
