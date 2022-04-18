import utils
import sorts

bookshelf = utils.load_books('books_small.csv')
bookshelf_v2 = bookshelf.copy()
long_bookshelf = utils.load_books('books_large.csv')

def by_title_ascending(book_a, book_b):
  return book_a['title_lower'] > book_b['title_lower']

def by_author_ascending(book_a, book_b):
  return book_a['author_lower'] > book_b['author_lower']

def by_total_length(book_a, book_b):
  return len(book_a['author_lower']) + len(book_a["title_lower"]) > len(book_b['author_lower']) + len(book_b["title_lower"])

sort_1 = sorts.bubble_sort(bookshelf.copy(), by_title_ascending)

for book in sort_1:
  print(book["title_lower"])

sort_2 = sorts.bubble_sort(bookshelf.copy(), by_author_ascending)

for book in sort_2:
  print(book["title_lower"])

sorts.quicksort(bookshelf_v2, 0, len(bookshelf) -1, by_author_ascending)

for book in bookshelf_v2:
  print(book["title_lower"])

sort_3 = sorts.bubble_sort(long_bookshelf.copy(), by_total_length)

for book in sort_3:
  print(len(book["author_lower"]) + len(book["title_lower"]))

sorts.quicksort(long_bookshelf, 0, len(long_bookshelf) -1, by_author_ascending)

for book in long_bookshelf:
  print(len(book["author_lower"]) + len(book["title_lower"]))
