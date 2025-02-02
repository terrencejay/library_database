import mysql.connector
from database_connection import connect_database
import datetime

def add_book():
    conn = connect_database()
    if conn is not None:
        try:
            cursor = conn.cursor()

            title = input("What is the Title of the book you would like to add?: ")
            author = input("Enter the author's name: ")
            isbn = input("Enter ISBN (or leave blank): ") 
            publication_date = input("Enter publication date (YYYY-MM-DD): ") 
            availability = input("Is the book available to be rented? ((1)yes/(2)no): ").lower() 

            
            author_query = "SELECT author_id FROM authors WHERE name = %s"
            cursor.execute(author_query, (author,))  
            author_result = cursor.fetchone()

            if author_result:
                author_id = author_result[0]
            else:
                
                create_author = input(f"Author '{author}' not found. Create new author? (yes/no): ").lower()
                if create_author == 'yes':
                    try:
                        insert_author_sql = "INSERT INTO authors (name) VALUES (%s)"
                        cursor.execute(insert_author_sql, (author,))
                        conn.commit()  
                        author_id = cursor.lastrowid 
                        print(f"Author '{author}' added.")
                    except mysql.connector.Error as e:
                        conn.rollback()
                        print(f"Error creating author: {e}")
                        return  
                else:
                    print("Book addition cancelled.")
                    return  


            
            insert_book_sql = "INSERT INTO books (title, author_id, isbn, publication_date, availability) VALUES (%s, %s, %s, %s, %s)"
            book_data = (title, author_id, isbn if isbn else None, publication_date, availability) 
            cursor.execute(insert_book_sql, book_data)
            conn.commit()

            print("Book added successfully")

        except mysql.connector.Error as Error:
            print(f"Could not connect or insert: {Error}")
            if conn:
                conn.rollback()

        finally:
            cursor.close()
            conn.close()
            print("Connection closed")
            

def borrow_book():
    conn = connect_database()
    if conn is not None:
        try:
            cursor = conn.cursor()

            book_to_rent = input("What book would you like to rent? ")
            user_id = int(input("Enter your user ID: "))  

            
            book_availability = "SELECT book_id FROM books WHERE title = %s AND availability = 1"
            cursor.execute(book_availability, (book_to_rent,))
            book_result = cursor.fetchone()

            if book_result:
                book_id = book_result[0]

                
                update_availability = "UPDATE books SET availability = 0 WHERE book_id = %s"
                cursor.execute(update_availability, (book_id,))

                
                borrow_date = datetime.datetime.now()
                insert_borrowing = """
                    INSERT INTO borrowed_books (book_id, user_id, borrow_date)  -- Correct table and column names
                    VALUES (%s, %s, %s)
                """
                cursor.execute(insert_borrowing, (book_id, user_id, borrow_date))  # Use user_id

                conn.commit()
                print(f"'{book_to_rent}' borrowed successfully.")
                return True

            else:
                print(f"'{book_to_rent}' is not available or does not exist.")
                return False

        except mysql.connector.Error as Error:
            print(f"Database error: {Error}")
            conn.rollback()
            return False

        except ValueError:
            print("Invalid user ID. Please enter a number.")
            conn.rollback()
            return False

        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()
            print("Connection closed")
    return False



def return_book():
    conn = connect_database()
    if conn is not None:
        try:
            cursor = conn.cursor()
            
            book_id_to_return = input("Enter the book ID you're looking to return: ")
            
            check_query = "SELECT * FROM borrowed_books WHERE book_id = %s"
            cursor.execute(check_query, (book_id_to_return,))
            result = cursor.fetchone()
            
            if result:
                update_query = "UPDATE books SET availability = 1 WHERE book_id = %s"
                cursor.execute(update_query, (book_id_to_return,))
                
                delete_query = "DELETE FROM borrowed_books WHERE book_id = %s"
                cursor.execute(delete_query, (book_id_to_return,))
                
                conn.commit()
                print(f"The book with ID '{book_id_to_return}' has been successfully returned.")
            else:
                print(f"The book with ID '{book_id_to_return}' is not currently borrowed.")
        
        except mysql.connector.Error as err:
            print(f"Error: {err}")
        
        finally:
            cursor.close()
            conn.close()
            print("Connection closed")
            
def search_book():
    conn = connect_database()
    if conn is not None:
        try:
            cursor = conn.cursor()
            
            search_term = input("Enter the title or author of the book you are searching for: ")
            
            search_query = """
                SELECT books.title, authors.name, books.isbn, books.publication_date, books.availability
                FROM books
                JOIN authors ON books.author_id = authors.author_id
                WHERE books.title LIKE %s OR authors.name LIKE %s
            """
            cursor.execute(search_query, (f"%{search_term}%", f"%{search_term}%"))
            
            results = cursor.fetchall()
            
            if results:
                print("Search results:")
                for result in results:
                    title, author, isbn, publication_date, availability = result
                    print(f"Title: {title}, Author: {author}, ISBN: {isbn}, Publication Date: {publication_date}, Availability: {'Yes' if availability else 'No'}")
            else:
                print("No books found matching your search criteria.")
        
        except mysql.connector.Error as err:
            print(f"Error: {err}")
        
        finally:
            cursor.close()
            conn.close()
            print("Connection closed")

            
def display_all_books():
    conn = connect_database()
    if conn is not None:
        try:
            cursor = conn.cursor()
            
            select_query = "SELECT title, author_id, isbn, publication_date, availability FROM books"
            cursor.execute(select_query)
            
            books = cursor.fetchall()
            
            if books:
                print("List of all books:")
                for book in books:
                    title, author_id, isbn, publication_date, availability = book
                    print(f"Title: {title}, Author ID: {author_id}, ISBN: {isbn}, Publication Date: {publication_date}, Availability: {'Yes' if availability else 'No'}")
            else:
                print("No books found in the database.")
        
        except mysql.connector.Error as err:
            print(f"Error: {err}")
        
        finally:
            cursor.close()
            conn.close()
            print("Connection closed")
