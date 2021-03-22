from flask import Flask, render_template, redirect, session, url_for, request
from flask_mysqldb import MySQL
import MySQLdb


app= Flask(__name__)
app.secret_key = "1234353234"

app.config["MYSQL_HOST"] = "localhost"
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = ""
app.config["MYSQL_DB"] = "loginproject"

db = MySQL(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'name' in request.form and 'password' in request.form:
            name = request.form['name']
            password = request.form['password']
            cursor = db.connection.cursor(MySQLdb.cursors.DictCursor)
            cursor.execute("SELECT * FROM 'login' WHERE 'email'=%s AND 'password'=%s",(name,password))
            info = cursor.fetchone()
            if info['email'] == name and info['password'] == password:
                return "login successful"
            else:
                return "nu e bine"

    return render_template("login.html")

if __name__ == '__main__':
    app.run(debug=True)