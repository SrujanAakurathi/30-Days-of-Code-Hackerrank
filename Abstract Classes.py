class MyBook(Book):
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def display(self):
        print("Title: {}\nAuthor: {}\nPrice: {}".format(self.title, self.author, self.price))
