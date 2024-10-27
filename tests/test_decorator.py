import unittest
from library.book import Book
from library.decorator import FeaturedBookDecorator

class TestBookDecorator(unittest.TestCase):

    def test_decorator(self):
        book = Book("The Catcher in the Rye", "J.D. Salinger", 5)
        decorated_book = FeaturedBookDecorator(book, "Best-seller")

        self.assertEqual(decorated_book.get_info(), 
                         "The Catcher in the Rye by J.D. Salinger (5 copies available) - Best-seller")

if __name__ == "__main__":
    unittest.main()
