import sqlite3

con = sqlite3.connect('sample.db')
cursor = con.cursor()

cursor.execute("SELECT * FROM User")
# print(next(cursor))
# print(next(cursor))
# .fetchall()：現在のcursor以下全てをタプルのリストで返す
print(cursor.fetchall())
# .fetchone()：現在のcursorのレコードをタプルで返す
print(cursor.fetchone())
