import mysql.connector
from database_connection import connect_database

def add_author():
    conn = connect_database()
    if conn is not None:
        try:
            cursor = conn.cursor()
            name = input("Enter the authors name: ")
            biography = input("Enter author Bio: ")
            
            sql = "INSERT INTO authors (name,biography) VALUES (%s,%s)"
            val = (name, biography)
            cursor.execute(sql, val)
            conn.commit()
            
            print("Author added to database")
        
        except mysql.connector.Error as error:
            print(f"failed to add author to database: {error}")
        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()
                print ("Database connection closed")



def author_details():
    conn = connect_database()
    if conn is not None:
        try:
            cursor = conn.cursor()
            author = input("What is the name of the author who's details you want to view? ")
            
            sql = "SELECT * FROM Authors WHERE name = %s"
            val = (author,)
            cursor.execute(sql,val)
            results = cursor.fetchall()
            
            if results:
                print("Author details found.")
                for row in results:
                    print(row)
            else:
                print("Author not found")
        except mysql.connector.Error as Error:
            print(f"Could not retrieve details: {Error}")
        finally:
            conn.close()
            cursor.close()
            print("connection closed")


def display_all_authors():
    conn = connect_database()
    if conn is not None:
        try:
            cursor = conn.cursor()
            
            sql="SELECT * FROM authors"
            
            cursor.execute(sql)
            
            result = cursor.fetchall()
            if result:
                for row in result:
                    print(row)
                else:
                    print("No more results to display")
        except mysql.connector.Error as Err:
            print(f"Could not display details: {Err}")
        finally:
            cursor.close()
            conn.close()
            print ("connection closed")

