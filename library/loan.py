from datetime import datetime, timedelta

class Loan:
    def __init__(self, member, book_copy):
        self.member = member
        self.book_copy = book_copy
        self.checkout_date = datetime.now()
        self.due_date = self.checkout_date + timedelta(days=14)
        self.return_date = None
        self.renewals = 0
    
    def renew(self):
        if self.renewals >=2:
            raise ValueError("Maximum renewals reached")
        self.due_date += timedelta(days=14)
        self.renewals += 1
        
    def is_overdue(self):
        if self.return_date:
            return self.return_date > self.due_date
        return datetime.now() > self.due_date
        