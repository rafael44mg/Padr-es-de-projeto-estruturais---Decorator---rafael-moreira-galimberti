from abc import ABC, abstractmethod
from .book import Book

# Componente base
class BookDecorator(ABC):
    def __init__(self, book: Book):
        self.book = book

    @abstractmethod
    def get_info(self):
        pass

# Concrete Decorator - Adiciona etiqueta de destaque
class FeaturedBookDecorator(BookDecorator):
    def __init__(self, book: Book, feature: str):
        super().__init__(book)
        self.feature = feature

    def get_info(self):
        return f"{self.book.get_info()} - {self.feature}"
