import sqlite3

con = sqlite3.connect("library.db")

cursor = con.cursor()

def create_table():
    cursor.execute("CREATE TABLE IF NOT EXISTS bookshelf(Name TEXT, Author TEXT, Publisher TEXT, page_number INT)")
    con.commit()

def add_data():
    cursor.execute("INSERT INTO bookshelf VALUES('The Paris Review', 'Joan Didion', 'abcdefg', 435)")
    con.commit()

def add_data2(name,author,publisher,page_number):
    cursor.execute("INSERT INTO bookshelf VALUES(?,?,?,?)", (name,author,publisher,page_number))
    con.commit()

def fetch_data():
    cursor.execute("SELECT * FROM bookshelf")
    List = cursor.fetchall()
    print("Book infos..")
    for i in List:
        print(i)

def fetch_data2():
    cursor.execute("SELECT name,author from bookshelf")
    List = cursor.fetchall()
    print("Book infos..")
    for i in List:
        print(i)


def fetch_data3(Publisher):
    cursor.execute("SELECT * FROM bookshelf WHERE publisher = ?",(Publisher,))
    List = cursor.fetchall()
    for i in List:
        print(i)



"""
name = input("Name:")
author = input("Author:")
publisher = input("Publisher:")
page_number = int(input("Number of page:"))
add_data2(name,author,publisher,page_number)
"""

fetch_data3("publisher2")
#add_data()
con.close()