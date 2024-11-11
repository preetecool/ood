class Member:
    def __init__(self, id, first_name, last_name, phone_number, address):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.address = address
        self.lent_books = []
        self.late_fees = 0.0
        
    def get_active_loans(self):
        return [loan for loan in self.lent_books if not loan.return_date]

    def get_overdue_books(self):
        return [loan for loan in self.get_active_loans() if loan.is_overdue]
    
    def pay_late_fees(self, amount):
        if amount > self.late_fees:
            raise ValueError("Payment amount exceeds late fees")