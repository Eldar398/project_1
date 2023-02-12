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

@app.route('/about')
def about_me():
    return render_template('about.html')

@app.route('/search')
def search():
    search_question = request.args.get('search')
    return "search result"+search_question

@app.route('/signup', methods=('GET', 'POST'))
def signup():
    if request.method == 'POST':
        favorit_language = request.form['fav_language']
        fname = request.form['fname']
        lname = request.form['lname']
        python_know = request.form['python_know']
        return render_template('signup.html', method='POST', fav_lang = favorit_language, fname=fname,lname=lname,python_know=python_know)
    else:
        return render_template('signup.html', method='GET')

@app.route('/login', methods=('GET', 'POST'))
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        return render_template('login.html', method='POST', username=username, password=password)
    else:
        return render_template('login.html', method='GET')




if __name__ == "__main__":
    app.run(debug=True)


