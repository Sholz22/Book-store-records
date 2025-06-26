from datetime import datetime 

books = [
   {"id": 203, "title": "Clean Code 4", "author": "Robert C. Martin", "in_shelf": False, "times_borrowed": 12, "borrow_date": datetime(2025, 4, 1)},
     {"id": 101, "title": "The Pragmatic Programmer 1", "author": "Andrew Hunt", "in_shelf": True, "times_borrowed": 12},
    {"id": 283, "title": "Introduction to Algorithms 5", "author": "Thomas H. Cormen", "in_shelf": True, "times_borrowed": 7},
    {"id": 428, "title": "Design Patterns 6", "author": "Erich Gamma", "in_shelf": True, "times_borrowed": 4},
    {"id": 285, "title": "Python Crash Course 2", "author": "Eric Matthes", "in_shelf": False, "times_borrowed": 8, "borrow_date": datetime(2025, 4, 15)},
    {"id": 628, "title": "Data Science from Scratch 7", "author": "Joel Grus", "in_shelf": True, "times_borrowed": 3},
    {"id": 773, "title": "You Don't Know JS 3", "author": "Kyle Simpson", "in_shelf": True, "times_borrowed": 6},
    {"id": 838, "title": "Deep Learning 9", "author": "Ian Goodfellow", "in_shelf": True, "times_borrowed": 2},
    {"id": 937, "title": "Fluent Python 8", "author": "Luciano Ramalho", "in_shelf": True, "times_borrowed": 12},
    {"id": 100, "title": "Effective Java 10", "author": "Joshua Bloch", "in_shelf": False, "times_borrowed": 9,"borrow_date": datetime(2025, 4, 25) }
    ]

def get_all_books():
    return books


def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def get_book_by_title(book_title):
    new_books = []
    # print(book_title.lower())
    for book in books:
      if book_title.lower() == book["title"].lower():
        # print(book["title"].lower())
        new_books.append(book)
    # print(new_books)
    if len(new_books) == 0:
      return "Book not Found"
    return new_books

def pay_fine(present_book):
   borrowing_limit = 14
   amount = 500
   now = datetime.now()
   borrowed_date = present_book["borrow_date"]
   difference = now - borrowed_date
   day_difference = abs(difference.days)
   if day_difference > borrowing_limit:
      fine = (day_difference - borrowing_limit) * amount
   else:
      fine = 0
   return fine