import sqlite3

conn = sqlite3.connect('lr8.db')
cursor = conn.cursor()

cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()
print("Tables:", tables)

cursor.execute("SELECT * FROM courier;")
courier_data = cursor.fetchall()
print("Courier Data:", courier_data)

cursor.execute("SELECT * FROM sender;")
sender_data = cursor.fetchall()
print("Sender Data:", sender_data)

conn.close()
