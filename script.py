import utils
import sorts

bookshelf = utils.load_books('books_small.csv')

# Print original titles
print("Original titles:")
for book in bookshelf:
    print(book['title'])

# ----------------------------
# Comparison functions
# ----------------------------

# Compare by title ascending
def by_title_ascending(book_a, book_b):
    return book_a['title_lower'] > book_b['title_lower']

# Compare by author ascending
def by_author_ascending(book_a, book_b):
    return book_a['author_lower'] > book_b['author_lower']

# Compare by total length of title + author
def by_total_length(book_a, book_b):
    len_a = len(book_a['title']) + len(book_a['author'])
    len_b = len(book_b['title']) + len(book_b['author'])
    return len_a > len_b

# ----------------------------
# Bubble Sort Tests
# ----------------------------
# Sort by title
bookshelf_title_sorted = sorts.bubble_sort(bookshelf.copy(), by_title_ascending)
print("\nTitles sorted by title:")
for book in bookshelf_title_sorted:
    print(book['title'])

# Sort by author
bookshelf_author_sorted = sorts.bubble_sort(bookshelf.copy(), by_author_ascending)
print("\nTitles sorted by author:")
for book in bookshelf_author_sorted:
    print(book['author'])

# ----------------------------
# Quicksort Tests
# ----------------------------
# Make copies to preserve original
bookshelf_quick_author = bookshelf.copy()

# Run quicksort by author
sorts.quicksort(bookshelf_quick_author, 0, len(bookshelf_quick_author) - 1, by_author_ascending)
print("\nQuicksort by author:")
for book in bookshelf_quick_author:
    print(book['author'])

# ----------------------------
# Total length sorting
# ----------------------------
# Load large bookshelf
long_bookshelf = utils.load_books('books_large.csv')

# Sort by total length using quicksort
sorts.quicksort(long_bookshelf, 0, len(long_bookshelf) - 1, by_total_length)
print("\nLong bookshelf sorted by total length (title + author):")
for book in long_bookshelf[:10]:  # Print only first 10 for brevity
    print(f"{book['title']} by {book['author']} - Total Length: {len(book['title']) + len(book['author'])}")
