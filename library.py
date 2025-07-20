
# Collect user's own books
own_books = input("Enter the name of a book you own:\n")
own_books2 = input("Enter the name of another book you own (or press Enter to skip):\n")

library = []
if len(own_books2) == 0:
    library.append(own_books)
else:
    library.append(own_books)
    library.append(own_books2)

print(f"Your personal library: {library}")

# Collect user's wishlist books
wish_books = input("Enter the name of a book you wish to buy in the future:\n")
wish_books2 = input("Enter the name of another book you wish to buy (or press Enter to skip):\n")

wish_library = []
if wish_books2 == "":
    wish_library.append(wish_books)
else:
    wish_library.append(wish_books)
    wish_library.append(wish_books2)

print(f"Your wishlist: {wish_library}")

# Remove a bought book from the wishlist
that_buy = input("Enter the name of the book you bought (to remove it from the wishlist):\n")

if that_buy in wish_library:
    wish_library.remove(that_buy)
    print(f"Your wishlist after removing the bought book: {wish_library}")
else:
    print("The book you entered is not in your wishlist.")
