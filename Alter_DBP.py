import sqlite3

connection = sqlite3.connect('AZHSP.db')

cur = connection.cursor()

cur.execute('''alter table Customer add column PHONE_NO TEXT''')

cur.close()

connection.close()