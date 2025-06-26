# 📚 Book Store Record API

A FastAPI-powered backend for managing a simple bookstore's inventory, borrowing, and return system. It supports book addition, retrieval, borrowing/return operations, fine calculation, and prime-suffix-based filtering.



## 🚀 Project Overview

This project provides a RESTful API to manage book records in a bookstore or library-like system. Built with FastAPI, it allows:
- Adding new books
- Searching books by title or author
- Borrowing and returning books
- Checking for overdue fines
- Listing books based on availability or popularity
- Filtering books with numeric suffixes that are prime numbers


## 📁 Project Structure

```
bookstore-record-api/
│
├── model/
│   └── book_request.py            
│
├── .gitignore                   
├── LICENSE                        
├── README.md                      
├── main.py                        
├── requirements.txt               
├── services.py                   

````



## 🛠️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/Sholz22/Book-store-records.git
cd Book-store-records
````

### 2. Create and Activate a Virtual Environment (optional but recommended)

```bash
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the FastAPI Server

```bash
uvicorn main:app --reload
```

Open in your browser:

* API Docs (Swagger UI): [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
* Redoc: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)



## 📬 API Endpoints

| Method | Endpoint                 | Description                                |
| ------ | ------------------------ | ------------------------------------------ |
| GET    | `/`                      | Welcome message                            |
| GET    | `/all-books`             | Get all books in the system                |
| POST   | `/get-book-by-name`      | Retrieve a book by title                   |
| POST   | `/get-books-by-author`   | Retrieve books by author                   |
| POST   | `/add-book`              | Add a new book to the system               |
| POST   | `/delete-by-name`        | Delete a book by its title                 |
| POST   | `/borrow-book-by-title`  | Borrow a book using the title              |
| POST   | `/borrow-book-by-author` | Borrow a book by author                    |
| POST   | `/return-book-by-title`  | Return a borrowed book using the title     |
| POST   | `/return-book-by-author` | Return a borrowed book by author           |
| GET    | `/get-borrowed-books`    | Get all books currently borrowed           |
| GET    | `/get-available-books`   | Get all books currently in shelf           |
| GET    | `/get-prime-suffix`      | Books with numeric suffixes that are prime |
| GET    | `/most-borrowed-book`    | Get the most borrowed book(s)              |



## 🧾 Example Request Body Formats

**POST `/add-book`**

```json
{
  "book_name": "God don't make mistakes",
  "author_name": "Olusola Owoso",
  "book_id": 22
}
```

**POST `/get-book-by-name`**

```json
{
  "book_name": "Design Patterns 6"
}
```

**POST `/get-books-by-author`**

```json
{
  "author_name": "Andrew Hunt"
}
```



## 📌 Features

* ✅ Add and retrieve book records
* 📖 Track whether a book is in shelf or borrowed
* ⏱️ Calculate fines based on borrow duration
* 🔍 Filter books with prime-number suffixes
* 📊 Identify most borrowed books



## ⚠️ Limitations & Areas for Improvement

* ❗ No persistent storage (data resets when server restarts)
* 🔐 No authentication or user tracking
* 💡 Fine calculation and return tracking could be extended to support multiple users
* 🧪 Add automated testing



## 📄 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.



## 👨‍💻 Authors

* [Olusola](https://github.com/Sholz22) – Developer



## 🙌 Acknowledgements

* [FastAPI](https://fastapi.tiangolo.com/)
* [Pydantic](https://pydantic-docs.helpmanual.io/)
* [Uvicorn](https://www.uvicorn.org/)

