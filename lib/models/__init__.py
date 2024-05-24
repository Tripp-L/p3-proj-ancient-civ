import sqlite3

CONN = sqlite3.connect('development.db')
CURSOR = CONN.cursor()