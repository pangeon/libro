from .book import Book
from .boxed_game import BoxedGame
from .digital_game import DigitalGame
from .magazine import Magazine
from .media_item import MediaItem
from .movie import Movie

# __init__.py sprawia, że models jest pakietem Pythona i w obecnej wersji udostępnia klasy bezpośrednio z pakietu:

# 1. kw_only=True oznacza, że pola modelu trzeba podawać do konstruktora po nazwie, a nie jako pozycyjne argumenty
# 2. default_factory=list tworzy nową listę dla każdego obiektu.
# 3. klasy dziedziczą po MediaItem są to pola wspólne dla wszystkich modeli
# 4. additional_authors i tags nie będą None, jeśli ich nie podasz — dzięki field(default_factory=list) dostaną pustą listę []. 

__all__ = [
    "Book",
    "BoxedGame",
    "DigitalGame",
    "Magazine",
    "MediaItem",
    "Movie",
]
