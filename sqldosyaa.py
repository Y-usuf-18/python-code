import sqlite3

con = sqlite3.connect("dersler.db")

cursor = con.cursor()


def tabloolustur():

    cursor.execute("CREATE TABLE ogrenciler(ad TEXT,soyadTEXT,no INT,not INT)")

    con.commit()
    con.close()

    tabloolustur()