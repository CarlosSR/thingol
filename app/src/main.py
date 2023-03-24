import mysql.connector
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/index")
def index():
    database = mysql.connector.connect(
        host="db",
        port="3306",
        user="root",
        password="root",
        database="thingol"
    )
    cursor = database.cursor()
    cursor.execute("SHOW DATABASES")
    result = cursor.fetchall()
    return result


@app.route("/user/<name>")
def user(name):
    return render_template('user.html', name=name)