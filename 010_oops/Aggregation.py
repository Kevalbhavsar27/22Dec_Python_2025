class Book:

    def __init__(self,title):
        self.title = title

class Library:

    def __init__(self):
        self.book = []

    def add_book(self,book):
        self.book.append(book)

b1 = Book("Java")
b2 = Book("Python")

l = Library()
l.add_book(b1)
l.add_book(b2)

for i in l.book:
    print(i.title)
