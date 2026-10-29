cart = ["Pen", "Book", "Bag"]

cart.append("Bottle")       # Add
cart.remove("Pen")          # Remove

if "Book" in cart:          # Search
    print("Book found")

print("Cart:", cart)
print("Total items:", len(cart))
