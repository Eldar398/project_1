from flask import Flask, render_template, request
from flask_mysqldb import MySQL

app = Flask(__name__, static_url_path='/static')
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Gfhjkm12345'
app.config['MYSQL_DB'] = 'test'

mysql = MySQL(app)
#object for database connection


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
        python_know = favorit_language

        cursor = mysql.connection.cursor()
        cursor.execute(''' INSERT INTO signup(login,password) VALUES(%s,%s)''', (fname, lname))
        mysql.connection.commit()
        cursor.close()
        return render_template('signup.html', method='POST', fav_lang = favorit_language, fname=fname,lname=lname)
    else:
        return render_template('signup.html', method='GET')

@app.route('/users')
def users():
    cursor = mysql.connection.cursor()
    cursor.execute(''' select * from signup ''')
    user_list = cursor.fetchall()
    cursor.close()
    result_users = []
    #tuple - []
    for item in user_list:
        result_users.append({'login': item[1], 'password': item[2]})
    return result_users

# TODO
# 1. login route and add login to header
# 2. check if password is correct
# 3. if it is correct change login to logout
# 4. not correct show some message (your password is not correct)




if __name__ == "__main__":
    app.run(debug=True)


