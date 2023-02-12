from flask import Flask, render_template, request


app = Flask(__name__, static_url_path='/static')


@app.route('/')
def index():
    return render_template('home.html')

@app.route('/skill')
def skill():
    return render_template('skills.html')

@app.route('/blog')
def blog():
    return render_template('blog.html')


if __name__ == "__main__":
    app.run(debug=True)


