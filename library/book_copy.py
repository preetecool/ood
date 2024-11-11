class BookCopy:
    def __init__(self, book, copy_id):
        self.book = book
        self.copy_id = copy_id
        self.is_available = True
        self.current_loan = None
    
    def __repr__(self):
        return (f"Copy {self.copy} of {self.book.title}")