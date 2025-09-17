import csv

def load_books(filename):
    bookshelf = []
    with open(filename) as file:
        shelf = csv.DictReader(file)
        for book in shelf:
            # Lowercase fields for consistent comparison
            book['author_lower'] = book['author'].lower()
            book['title_lower'] = book['title'].lower()
            bookshelf.append(book)
    return bookshelf
