from relationship_app.models import Author, Book, Library, Librarian

# 1. Query all books by a specific author (example: "George Orwell")
orwell = Author.objects.get(name="George Orwell")
books_by_orwell = Book.objects.filter(author=orwell)
print("Books by George Orwell:", books_by_orwell)

# 2. List all books in a library (example: "Central Library")
library = Library.objects.get(name="Central Library")
books_in_library = library.books.all()
print("Books in Central Library:", books_in_library)

# 3. Retrieve the librarian for a library (example: "Central Library")
librarian = Librarian.objects.get(library=library)
print("Librarian of Central Library:", librarian)
