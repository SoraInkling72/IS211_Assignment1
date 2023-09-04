class Book:
    def __init__(self, author, title):
        self.author = author
        self.title = title

    def display(self):
      print (self.title,', written by' ,self.author)

a_author = ('J.K. Rowling')
a_title = ('Harry Potter and the Goblet of Fire')
b_author = ('Walter Scott')
b_title = ('Ivanhoe: A Romance')

book1 = Book(a_author, a_title)
book2 = Book(b_author, b_title)

book1.display()
book2.display()
