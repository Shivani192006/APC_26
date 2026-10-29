# Maintain book records containing book ID, title, author, and availability status. 
#Implement operations to:  
#Add a book.  
#Search for a book.  
#Issue a book.  
#Return a book.  
#Display available books.

def add_book():
    f = open("books.txt", "a")
    id = input("Enter book ID: ")
    title = input("Enter title: ")
    author = input("Enter author: ")
    f.write(id + "," + title + "," + author + ",Available\n")
    f.close()

def search_book(id):
    f = open("books.txt", "r")

    for line in f:
        data = line.strip().split(",")
        if data[0] == id:
            print(data)
            f.close()
            return

    f.close()
    print("Book not found")

def change_status(id, status):
    f = open("books.txt", "r")
    lines = f.readlines()
    f.close()

    f = open("books.txt", "w")
    found = False

    for line in lines:
        data = line.strip().split(",")

        if data[0] == id:
            found = True

            if status == "Issued" and data[3] == "Available":
                data[3] = "Issued"
            elif status == "Available" and data[3] == "Issued":
                data[3] = "Available"
            else:
                print("Operation not possible")

            line = ",".join(data) + "\n"

        f.write(line)

    f.close()

    if not found:
        print("Book not found")

def display_books():
    f = open("books.txt", "r")

    for line in f:
        data = line.strip().split(",")
        if data[3] == "Available":
            print(data)

    f.close()

while True:
    print("1.Add 2.Search 3.Issue 4.Return 5.Available 6.Exit")
    ch = input("Enter choice: ")

    if ch == "1":
        add_book()
    elif ch == "2":
        search_book(input("Enter book ID: "))
    elif ch == "3":
        change_status(input("Enter book ID: "), "Issued")
    elif ch == "4":
        change_status(input("Enter book ID: "), "Available")
    elif ch == "5":
        display_books()
    elif ch == "6":
        break
    else:
        print("Invalid choice")
