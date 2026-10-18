from .book import Book
from .boxed_game import BoxedGame
from .digital_game import DigitalGame
from .magazine import Magazine
from .media_item import MediaItem
from .movie import Movie

# __init__.py sprawia, że models jest pakietem Pythona i w obecnej wersji udostępnia klasy bezpośrednio z pakietu:

# Konkretne dataclasses deklarują pola w tej samej kolejności co rekordy JSON.
# default_factory=list tworzy osobną listę dla każdego obiektu.
# MediaItem udostępnia wspólne adnotacje pól dla wszystkich modeli.

__all__ = [
    "Book",
    "BoxedGame",
    "DigitalGame",
    "Magazine",
    "MediaItem",
    "Movie",
]
