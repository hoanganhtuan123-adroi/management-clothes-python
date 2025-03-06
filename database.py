import mysql.connector
from mysql.connector import Error

class Database:
    def __init__(self):
        try:
            self.db = mysql.connector.connect(
                host='localhost',
                user='root',
                password='',
                database='clothes_db'
            )
            print("Kết nối thành công")
        except Error as e:
            print("Lỗi kết nối tới database:", e)
            self.db = None

    def get_connection(self):
        return self.db