class Book:
    def __init__(self, ISBN, title, author, genre, location, publish_date, amount_available):
        self.ISBN =  ISBN
        self.title = title 
        self.author = author
        self.genre = genre
        self.location = location
        self.publish_date = publish_date
        self.amount_available = amount_available
        

    def __repr__(self):
        return (f"Book({self.ISBN, self.title}, {self.author}, {self.genre}, {self.location}, {self.publish_date}, {self.amount_available})")