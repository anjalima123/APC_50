cart = []
cart.append("Book")
cart.append("Pen")
cart.append("Bag")
cart.remove("Pen")
if "Book" in cart:
    print("Book is available.")
print("Cart:", cart)
print("Total items:", len(cart))