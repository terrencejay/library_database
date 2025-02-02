import mysql.connector
from mysql.connector import Error

def connect_database():
    db_name = "Library_management"
    user = "root"
    password = "Password123!"
    host = "127.0.0.1"

    try:
        conn = mysql.connector.connect(
            database = db_name,
            user = user,
            password = password,
            host = host
        )
        
        print ("connected to database")
        return conn
    
    except Error as err:
        print (f"could not connect to database: {err}")
        return None
    
