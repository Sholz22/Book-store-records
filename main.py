from fastapi import FastAPI
# from pydantic import BaseModel
import re
from datetime import datetime 
from model.book_request import *
from services import *

app = FastAPI()


@app.get("/")
def read_root():
    return {"Python is the best programming language!"}


@app.get("/all-books")
def all_books():
    response = get_all_books()
    return response


@app.post("/get-book-by-name")
def book_by_name(request:BookNameRequest):
    book_name = request["book_name"]
    response = get_book_by_title(book_name)
    return response


@app.post("/get-books-by-author")
def book_by_author(request:BookAuthorRequest):
  author = request["author_name"]
  new_books = []
  for book in books:
      if author.lower() == book["author"].lower():
           new_books.append(book)
  if len(new_books) == 0:
      return "Book not Found"
  return new_books

@app.post("/add-book")
def add_book(request:BookFullRequest):
  book_id = request["book_id"]
  title = request["book_name"]
  author = request["author_name"]

  for book in books:
    if (title.lower() == book["title"].lower()) and (author.lower() == book["author"].lower()):
      return "Book already exists"
        
  books.append({"id": book_id, "title": title, "author": author, "in_shelf": True, "times_borrowed": 0})
  return {"reply":"New book added", "books": books}


@app.get("/get-prime-suffix")
def get_books_with_prime_suffix():
  new_books = []
  for book in books:
    title = book["title"]
    match = re.search(r"\d+", title)
    if match:
      number = int(match.group())
      
      if is_prime(number):
        new_books.append(book)

  return new_books

@app.post("/delete-by-name")
def delete_book_by_name(request:BookNameRequest):
  status = "Not found"
  title = request["book_name"]
  
  for index, book in enumerate(books):
        if title.lower() == book["title"].lower():
            del books[index]
            status = "Book Deleted"
            break 

  return {"status": status, "books":books}

@app.post("/borrow-book-by-author")
def borrow_book_by_author(request:BookAuthorRequest):
  author = request["author_name"]
  status = "Book Not Found"
  for book in books:
      if author.lower() == book["author"].lower():
        if book["in_shelf"] == True:
           book["in_shelf"] = False
           book["borrow_date"]= datetime.now()
           book["times_borrowed"] += 1
           status = "Book has been borrowed"
        else:
          status = "Book not in shelf"
        break

  return {"status": status}

@app.post("/borrow-book-by-title")
def borrow_book_by_title(request:BookNameRequest):
  title = request["book_name"]
  status = "Book Not Found"
  for book in books:
      if title.lower() == book["title"].lower():
        if book["in_shelf"] == True:
          book["in_shelf"] = False
          book["borrow_date"]= datetime.now()
          book["times_borrowed"] += 1
          status = "Book has been borrowed"
        else:
          status = "Book not in shelf"
          break

  return {"status": status}


@app.post("/return-book-by-author")
def return_book_by_author(request:BookAuthorRequest):
  author = request["author_name"]
  status = "Book Not Found"
  fine=0
  for book in books:
      if author.lower() == book["author"].lower():
        if book["in_shelf"] == False:
          book["in_shelf"] = True
          fine = pay_fine(book)
          status = "Book has been returned"
        else:
          status = "Book already in shelf"
        break

  return {"fine": fine, "status":status}

@app.post("/return-book-by-title")
def return_book_by_title(request:BookNameRequest):
  title = request["book_name"]
  status = "Book Not Found"
  fine=0
  for book in books:
      if title.lower() == book["title"].lower():
        if book["in_shelf"] == False:
          book["in_shelf"] = True
          fine = pay_fine(book)
          status = "Book has been returned"
        else:
          status = "Book already in shelf"
        break

  return {"fine": fine, "status": status}

@app.get("/get-borrowed-books")
def get_borrowed_books():
  new_books = []
  for book in books:
    if book["in_shelf"] == False:
      new_books.append(book)

  return new_books


@app.get("/get-available-books")
def get_available_books():
  new_books = []
  for book in books:
    if book["in_shelf"] == True:
      new_books.append(book)
      
  return new_books

@app.get("/most-borrowed-book")
def most_borrowed_book():
    if not books:
        return {"status": "No books in the library", "books": []}

    max_borrowed = max(book["times_borrowed"] for book in books)
    most_borrowed_books = [book for book in books if book["times_borrowed"] == max_borrowed]

    return {"status": "Success", "most_borrowed_books": most_borrowed_books}
