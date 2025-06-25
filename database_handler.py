import sqlite3

class DatabaseHandler():
    DB_NAME='students.db'

    def _connect():
        return sqlite3.connect(DatabaseHandler.DB_NAME)

    @staticmethod
    def create_table():
        with DatabaseHandler._connect() as conn: # context manager
            conn.execute('''CREATE TABLE IF NOt EXISTS students
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
             
    @staticmethod
    def get_all_students():
        with DatabaseHandler._connect() as conn:
            return conn.execute('SELECT * FROM students').fetchall()
        


DatabaseHandler.create_table()  # invoking and creat table to every method
         
