import sqlite3
import mysql.connector


def sqlite_conn():
    conn = sqlite3.connect('database.db')
    return conn

