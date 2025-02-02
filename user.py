import mysql.connector
from database_connection import connect_database

def add_user():
    conn = connect_database()
    if conn is not None:
        try:
            cursor = conn.cursor()
            
            name = input("Enter first and last name: ")
            library_id = input("Enter the library ID number: ")
            
            user_query = "INSERT INTO users (name, library_id) VALUES (%s, %s)"
            cursor.execute(user_query,(name,library_id))
            conn.commit()
            print ("User added successfully")
        except mysql.connector.Error as Err:
            print(f"could not add user {Err}")
        finally:
            cursor.close()
            conn.close()
            print("connection closed")

def view_users():
    conn = connect_database()
    if conn is not None:
        try:
            cursor = conn.cursor()
            
            user_search = input("Enter the name or ID number of the person you are looking for: ")
            
            search_query = "SELECT * FROM users WHERE name = %s OR library_id = %s"
            cursor.execute(search_query,(user_search,user_search))
            results = cursor.fetchall()
            
            if results:
                for user in results:
                    print(user)
            else:
                print("user not found")
        except mysql.connector.Error as Err:
            print(f"Can not find user: {Err}")
        finally:
            cursor.close()
            conn.close()
            print("connection closed")


def view_all_users():
    conn = connect_database()
    if conn is not None:
        try:
            cursor = conn.cursor()
            search_query = "SELECT * FROM users"
            cursor.execute(search_query)
            results = cursor.fetchall()
            
            if results:
                print("all users: ")
                for user in results:
                    print(user)
            else:
                print("Not user found.")
        except mysql.connector.Error as Err:
            print(f"could not get user: {Err}")
        finally:
            cursor.close()
            conn.close()
            print("connection closed")
view_all_users()
            