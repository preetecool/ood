
from datetime import datetime, timedelta
from book import Book
from member import Member
from book_copy import BookCopy
from loan import Loan

class Library:
    def __init__(self):
       self.books = {} #ISBN: Book
       self.book_copies = []
       self.members = {} #member_id: Member
       self.loans = []
       self.reservation = {} #ISBN: [] (list of members)
    
    def add_book(self, book, num_copies=1):
        self.books[book.ISBN] = book
        for i in range(num_copies):
            copy = BookCopy(book, f"{book.ISBN}-{i+1}")
            self.book_copies.append(copy)

    def book_checkout(self, member_id, ISBN):
        member = self.members.get(member_id)
        if not member:
            raise ValueError("Member not found")

        available_copy = next((copy for copy in self.book_copies if copy.book.ISBN == ISBN and copy.is_available), None)
        
        if not available_copy:
            if ISBN not in self.reservations:
                self.reservations[ISBN].append(member)
                raise ValueError("No copies available. Added member to book reservation list.")
        
        #create new book loan
        loan = Loan(member, available_copy)
        available_copy.is_available = False
        available_copy.current_loan = loan
        member.lent_books.append(loan)
        self.loans.append(loan)
        return loan
    
    def return_book(self, copy_id):
        copy = next((copy for copy in self.book_copies if copy.copy_id == copy_id), None)
        if not copy or not copy.current_loan:
            raise ValueError("Invalid return")
        
        loan = copy.current_loan
        loan.return_date = datetime.now()
        
        if loan.is_overdue():
            days_overdue = (loan.return_date - loan.due_date).days
            fee = days_overdue * 0.50
            loan.member.late_fees += fee
        
        copy.is_available = True
        copy.current_loan = None
        
        if copy.book.ISBN in self.reservations and self.reservations[copy.book.ISBN]:
            next_member = self.revervations[copy.book.ISBN].pop(0)
            self.notify_member(next_member, f"Book {copy.book.title} is now available")        
        
    def search_books(self, query):
        results = []
        for book in self.books.values():
            if(query.lower() in book.title.lower() or
               query.lower() in book.author.lower() or
               query in book.ISBN):
                   results.append(book)
            return results
    
