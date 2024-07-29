class LibraryManager:
    def __init__(self):
        self.books = {}

    def add_book(self, isbn, details):
        if isbn in self.books:
            print(f"Book with ISBN {isbn} already exists.")
        else:
            self.books[isbn] = details
            print(f"Book with ISBN {isbn} added.")

    def remove_book(self, isbn):
        if isbn in self.books:
            del self.books[isbn]
            print(f"Book with ISBN {isbn} removed.")
        else:
            print(f"Book with ISBN {isbn} not found.")

    def get_book_details(self, isbn):
        return self.books.get(isbn, "Book not found.")

    def search_books(self, title=None, author=None):
        results = []
        for book in self.books.values():
            if (title and title.lower() in book['title'].lower()) or (author and author.lower() in book['author'].lower()):
                results.append(book)
        return results

    def list_books(self):
        return self.books.values()

    def update_book(self, isbn, updated_details):
        if isbn in self.books:
            self.books[isbn].update(updated_details)
            print(f"Book with ISBN {isbn} updated.")
        else:
            print(f"Book with ISBN {isbn} not found.")

    def is_book_available(self, isbn):
        return isbn in self.books
