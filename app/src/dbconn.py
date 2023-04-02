import sqlite3
import mysql.connector


def sqlite():
    conn = sqlite3.connect('/thingol/db/sqlite/database.db')
    return conn

