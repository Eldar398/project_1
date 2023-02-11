from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def index():
    return "Hello"

@app.route('/login/<login>/<password>')
def login(login, password):
    if login == 'test' and password == 'test':
        message = "Hello"
    else:
        message = "Go out!"
    return render_template('login.html', message=message)

if __name__ == "__main__":
    app.run()


