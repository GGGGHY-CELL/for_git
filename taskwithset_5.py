book = {"title": "Война и мир", "author": "Толстой", "year": 1869}

print(set(book.keys()))
print(set(book.values()))

book.update({"pages": 1274})
print(book)

book.update({"year": 1865})
print(book)

book.pop("author")
print(book)