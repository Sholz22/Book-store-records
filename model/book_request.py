from pydantic import BaseModel

# Define a request model
class BookFullRequest(BaseModel):
    book_name: str
    author_name: str
    book_id: int

    def __getitem__(self, item):  # allow dict-style access
        return getattr(self, item)

class BookRequest(BaseModel):
    book_name: str
    author_name: str

    def __getitem__(self, item):  # allow dict-style access  
        return getattr(self, item)

class BookNameRequest(BaseModel):
    book_name: str

    def __getitem__(self, item):
        return getattr(self, item)
    
class BookAuthorRequest(BaseModel):
    author_name: str

    def __getitem__(self, item):
        return getattr(self, item)
