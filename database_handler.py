import sqlite3

class DatabaseHandler():
    DB_NAME='students.db'

    def _connect():
        return sqlite3.Connect(DatabaseHandler.DB_NAME)

    @staticmethod
    def creat_table():
        with DatabaseHandler._connect() as conn:
            conn.execute('''CREATE TABLE IF NOt EX ISTS students
                            (id INTEGER PRIMARY KEY AUTOINCREMENT,
                            name TEXT NOT NULL,
                            email TEXT NOT NULL,
                            age INTEGER NOT NULL,
                            gender TEXT NOT NULL)''')
        # conn.commit() not needed
        # conn.close()  not needed
    
    @staticmethod
    def insert_student(name,email,age,gender):
        with DatabaseHandler._connect() as conn:
            conn.execute('INSERT INTO students (name,email,age,gender)VALUES(?,?,?,?)',
                         (name,email,age,gender))
             
