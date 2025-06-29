import sqlite3
import logging
import datetime
import os
from werkzeug.security import generate_password_hash

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

#acces a la directory de la base
db_path = os.path.join(BASE_DIR, '..', 'flask', 'instance', 'ceagen.db')

db_path = os.path.normpath(db_path)

def get_db_connection():
	conn = sqlite3.connect(db_path)
	conn.row_factory = sqlite3.Row
	return conn

def createTableUser():
	conn = get_db_connection()
	cursor = conn.cursor()
	try:
		cursor.execute("""
            CREATE TABLE IF NOT EXISTS USER(
				ID INTEGER PRIMARY KEY AUTOINCREMENT,
				Login VARCHAR(20) NOT NULL,
				Pwd VARCHAR(80) NOT NULL,
				DateCreated DATETIME DEFAULT (datetime('now','localtime'))
				)
        """)
	except Exception as e:
		conn.rollback()
		print(f"There was an error: {e}")
		logging.error(f"An error occured: {e}")
	finally:
		conn.close()

def createAuthentification(name,password):
	conn = get_db_connection()
	cursor = conn.cursor()
	hashedPassword = generate_password_hash(password)
	try:
		cursor.execute("INSERT INTO USER (Login, Pwd) VALUES (?,?)",(name,hashedPassword,))
		conn.commit()
	except Exception as e:
		conn.rollback()
		print(f"There was an error: {e}")
		logging.error(f"An error occured: {e}")
	finally:
		conn.close()
		
def getLogin(name):
	conn = get_db_connection()
	cursor = conn.cursor()
	try:
		cursor.execute("SELECT * FROM USER WHERE Login = ?", (name,))
		return cursor.fetchone()
	except Exception as e:
		print(f"There was an error: {e}")
		logging.error(f"An error occured: {e}")
	finally:
		conn.close()

name = 'Ceagen'
pwd = '#Allen02walker'

#createAuthentification(name,pwd)