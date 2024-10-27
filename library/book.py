class Book:
    def __init__(self, title: str, author: str, copies: int):
        self.title = title
        self.author = author
        self.copies = copies

    def get_info(self):
        return f"{self.title} by {self.author} ({self.copies} copies available)"
