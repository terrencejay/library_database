import mysql.connector
from authors import add_author, display_all_authors, author_details
from books import add_book, borrow_book, return_book, display_all_books, search_book
from user import add_user, view_users, view_all_users

def main():
    print("Welcome to the Library Management System with Database Integration!")
    while True:
        print("\nMain Menu:")
        print("1. Book Operations")
        print("2. User Operations")
        print("3. Author Operations")
        print("4. Quit")

        choice = input("Enter your choice: ")

        if choice == '1':
            book_operations()
        elif choice == '2':
            user_operations()
        elif choice == '3':
            author_operations()
        elif choice == '4':
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
            
def book_operations():
    while True:
        print("\nBook Operations Menu:")
        print("1. Add Book")
        print("2. Borrow Book")
        print("3. Return Book")
        print("4. Display All Books")
        print("5. Search Book")
        print("6. Back to Main Menu")

        choice = input("Enter your choice: ")

        if choice == '1':
            add_book()
        elif choice == '2':
            borrow_book()
        elif choice == '3':
            return_book()
        elif choice == '4':
            display_all_books()
        elif choice == '5':
            search_book()
        elif choice == '6':
            break
        else:
            print("Invalid choice. Please try again.")

def user_operations():
    while True:
        print("\nUser Operations Menu:")
        print("1. Add User")
        print("2. View Users")
        print("3. View All Users")
        print("4. Back to Main Menu")

        choice = input("Enter your choice: ")

        if choice == '1':
            add_user()
        elif choice == '2':
            view_users()
        elif choice == '3':
            view_all_users()
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")

def author_operations():
    while True:
        print("\nAuthor Operations Menu:")
        print("1. Add Author")
        print("2. Display All Authors")
        print("3. View Author Details")
        print("4. Back to Main Menu")

        choice = input("Enter your choice: ")

        if choice == '1':
            add_author()
        elif choice == '2':
            display_all_authors()
        elif choice == '3':
            author_details()
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")



if __name__ == "__main__":
    main()