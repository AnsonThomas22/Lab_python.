class LibraryManager:
    def __init__(self):
        self.books = {}

    def add_book(self, isbn, title, author, publisher, volume, year, isbn_code):
        if isbn in self.books:
            print(f"Book with ISBN {isbn} already exists.")
            return
        self.books[isbn] = {
            "title": title,
            "author": author,
            "publisher": publisher,
            "volume": volume,
            "year": year,
            "isbn_code": isbn_code
        }
        print(f"Book {title} added successfully.")

    def remove_book(self, isbn):
        if isbn not in self.books:
            print(f"No book found with ISBN {isbn}.")
            return
        del self.books[isbn]
        print(f"Book with ISBN {isbn} removed successfully.")

    def get_book(self, isbn):
        return self.books.get(isbn, f"No book found with ISBN {isbn}.")

    def search_books(self, search_term):
        results = []
        for isbn, book in self.books.items():
            if search_term.lower() in book["title"].lower() or search_term.lower() in book["author"].lower():
                results.append(book)
        return results

    def list_books(self):
        return list(self.books.values())

    def update_book(self, isbn, title=None, author=None, publisher=None, volume=None, year=None, isbn_code=None):
        if isbn not in self.books:
            print(f"No book found with ISBN {isbn}.")
            return
        book = self.books[isbn]
        if title:
            book["title"] = title
        if author:
            book["author"] = author
        if publisher:
            book["publisher"] = publisher
        if volume:
            book["volume"] = volume
        if year:
            book["year"] = year
        if isbn_code:
            book["isbn_code"] = isbn_code
        print(f"Book with ISBN {isbn} updated successfully.")

    def is_book_available(self, isbn):
        return isbn in self.books

