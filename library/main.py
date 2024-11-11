from library import Library
from book import Book
from member import Member

def main():
    library = Library()
    
    book1 = Book(123456, "The Great Gatsby", "Francis  Scott Fitzgerald", "Fiction", "A1", "1925", 2)
    library.add_book(book1, num_copies=2)
    
    member = Member(123456, "John", "Doe", "123-456-789", "123 Main St")
    library.members[member.id] = member
    
    try:
        loan = library.check_out_book(member.id, 123456)
        print(f"Checked out: {loan.book_copy}")
    except ValueError as err:
        print(f"Error: {err}")
    
    library.return_book(loan.book_copy.copy_id)


if __name__ == "main":
    main()
