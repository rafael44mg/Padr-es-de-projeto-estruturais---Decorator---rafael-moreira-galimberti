# library/loan.py

from .book import Book

class Loan:
    def __init__(self, book: Book, user: str):
        self.book = book
        self.user = user
        self.is_active = True

    def end_loan(self):
        self.is_active = False

    def get_loan_info(self):
        status = "Active" if self.is_active else "Closed"
        return f"Loan for '{self.book.title}' by {self.user}. Status: {status}"
