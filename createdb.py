import sqlite3
connection = sqlite3.connect('snippets.db')
database = connection.cursor()
database.execute('CREATE TABLE snippets (name text, content text, lang text)')
connection.commit()
connection.close()