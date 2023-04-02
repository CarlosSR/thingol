import sqlite3
import mysql.connector


def sqlite():
    conn = sqlite3.connect('/thingol/db/sqlite/database.db')
    return conn

def mariadb():
    database = mysql.connector.connect(
        host="db",
        port="3306",
        user="root",
        password="root",
        database="thingol"
    )
    return database

