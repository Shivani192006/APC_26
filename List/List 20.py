books = ["Python", "Java", "C++"]

books.append("HTML")        # Add

if "Java" in books:         # Search
    print("Book found")

books.remove("C++")         # Remove

print("Books:", books)
print("Total books:", len(books))
