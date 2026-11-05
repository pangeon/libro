import unittest
from utils import FileManager, DataFormatter
from service.collection_service import CollectionService
from models import Book, Magazine, BoxedGame, DigitalGame, Movie


class TestFileManager(unittest.TestCase):

    def test_load_file_returns_list(self):
        file_manager = FileManager("data/books.json")
        self.assertIsInstance(file_manager.load_file(), list, "The loaded data should be a list.")
        self.assertTrue(len(file_manager.load_file()) > 0, "The loaded list should not be empty.")
        self.assertTrue(type(file_manager.load_file()[0].get("id")) is int, "The first item in the list should have a 'id' key of type int.")

class TestServiceCollection(unittest.TestCase):

    def setUp(self):
        self.collection = FileManager("data/books.json").load_file()
        self.service = CollectionService(self.collection)

    def test_get_all_returns_list(self):
        self.assertIsInstance(self.service.get_all(), list, "get_all should return a list.")

    def test_get_index_returns_correct_record(self):
        record = self.service.get_index(0)
        self.assertEqual(record.get("id"), 1, "get_index should return the correct record.")

    def test_get_by_record_returns_correct_record(self):
        record = self.service.get_by_record(1)
        self.assertEqual(record.get("id"), 1, "get_by_record should return the correct record.")

    def test_add_record_increases_collection_size(self):
        initial_size = len(self.service.get_all())
        new_record = {"id": 999, "title": "Test Book"}
        self.service.add_record(new_record)
        self.assertEqual(len(self.service.get_all()), initial_size + 1, "add_record should increase collection size by 1.")

    def test_delete_record_decreases_collection_size(self):
        new_record = {"id": 1000, "title": "Test Book to Delete"}
        self.service.add_record(new_record)
        initial_size = len(self.service.get_all())
        self.service.delete_record(1000)
        self.assertEqual(len(self.service.get_all()), initial_size - 1, "delete_record should decrease collection size by 1.")

    def test_update_record_changes_field_value(self):
        new_record = {"id": 1001, "title": "Old Title"}
        self.service.add_record(new_record)
        self.service.update_record(1001, "title", "New Title")
        updated_record = self.service.get_by_record(1001)
        self.assertEqual(updated_record.get("title"), "New Title", "update_record should change the field value.")

class TestBookModel(unittest.TestCase):

    def test_book_model_initialization(self):
        book = Book(1, "1234567890", "Book", "John Due", "ABC", 2020, "1", "Fiction", "PL")
        self.assertEqual(book.id, 1, "Book id should be initialized correctly.")
        self.assertEqual(book.isbn, "1234567890", "Book isbn should be initialized correctly.")
        self.assertEqual(book.title, "Book", "Book title should be initialized correctly.")
        self.assertEqual(book.author, "John Due", "Book author should be initialized correctly.")
        self.assertEqual(book.publisher, "ABC", "Book publisher should be initialized correctly.")
        self.assertEqual(book.publication_year, 2020, "Book year should be initialized correctly.")
        self.assertEqual(book.edition, "1", "Book edition should be initialized correctly.")
        self.assertEqual(book.category, "Fiction", "Book category should be initialized correctly.")
        self.assertEqual(book.language, "PL", "Book language should be initialized correctly.")

class TestMagazinesModel(unittest.TestCase):

    def test_magazines_model_initialization(self):
        magazine = Magazine(1, "1234567890", "Magazine", "XYZ", 2021, "Science", "Super S", "EN")
        self.assertEqual(magazine.id, 1, "Magazines id should be initialized correctly.")
        self.assertEqual(magazine.issn, "1234567890", "Magazines issn should be initialized correctly.")
        self.assertEqual(magazine.title, "Magazine", "Magazines title should be initialized correctly.")
        self.assertEqual(magazine.publisher, "XYZ", "Magazines publisher should be initialized correctly.")
        self.assertEqual(magazine.publication_year, 2021, "Magazines year should be initialized correctly.")
        self.assertEqual(magazine.category, "Science", "Magazines category should be initialized correctly.")
        self.assertEqual(magazine.series, "Super S", "Magazines series should be initialized correctly.")
        self.assertEqual(magazine.language, "EN", "Magazines language should be initialized correctly.")

class TestBoxedGameModel(unittest.TestCase):

    def test_boxed_game_model_initialization(self):
        boxed_game = BoxedGame(1, "Boxed Game", "Game Studio", "Game Publisher", 2022, "PC", "Action", "EN", "Silver")
        self.assertEqual(boxed_game.id, 1, "BoxedGame id should be initialized correctly.")
        self.assertEqual(boxed_game.title, "Boxed Game", "BoxedGame title should be initialized correctly.")
        self.assertEqual(boxed_game.producer, "Game Studio", "BoxedGame producer should be initialized correctly.")
        self.assertEqual(boxed_game.publisher, "Game Publisher", "BoxedGame publisher should be initialized correctly.")
        self.assertEqual(boxed_game.publication_year, 2022, "BoxedGame year should be initialized correctly.")
        self.assertEqual(boxed_game.platform, "PC", "BoxedGame platform should be initialized correctly.")
        self.assertEqual(boxed_game.category, "Action", "BoxedGame category should be initialized correctly.")
        self.assertEqual(boxed_game.language, "EN", "BoxedGame language should be initialized correctly.")
        self.assertEqual(boxed_game.series, "Silver", "BoxedGame series should be initialized correctly.")

class TestDigitalGameModel(unittest.TestCase):

    def test_digital_game_model_initialization(self):
        digital_game = DigitalGame(1, "Digital Game", "Game Store", "Game Studio", "Game Publisher", 2023, "PC", "Adventure", "EN", "Gold")
        self.assertEqual(digital_game.id, 1, "DigitalGame id should be initialized correctly.")
        self.assertEqual(digital_game.title, "Digital Game", "DigitalGame title should be initialized correctly.")
        self.assertEqual(digital_game.store, "Game Store", "DigitalGame store should be initialized correctly.")
        self.assertEqual(digital_game.producer, "Game Studio", "DigitalGame producer should be initialized correctly.")
        self.assertEqual(digital_game.publisher, "Game Publisher", "DigitalGame publisher should be initialized correctly.")
        self.assertEqual(digital_game.publication_year, 2023, "DigitalGame year should be initialized correctly.")
        self.assertEqual(digital_game.platform, "PC", "DigitalGame platform should be initialized correctly.")
        self.assertEqual(digital_game.category, "Adventure", "DigitalGame category should be initialized correctly.")
        self.assertEqual(digital_game.language, "EN", "DigitalGame language should be initialized correctly.")
        self.assertEqual(digital_game.series, "Gold", "DigitalGame series should be initialized correctly.")

class TestMovieModel(unittest.TestCase):

    def test_movie_model_initialization(self):
        movie = Movie(1, "Movie Title", 2024, "Action", "EN", "Blu-ray", "Director Name")
        self.assertEqual(movie.id, 1, "Movie id should be initialized correctly.")
        self.assertEqual(movie.title, "Movie Title", "Movie title should be initialized correctly.")
        self.assertEqual(movie.publication_year, 2024, "Movie year should be initialized correctly.")
        self.assertEqual(movie.category, "Action", "Movie category should be initialized correctly.")
        self.assertEqual(movie.language, "EN", "Movie language should be initialized correctly.")
        self.assertEqual(movie.format, "Blu-ray", "Movie format should be initialized correctly.")
        self.assertEqual(movie.director, "Director Name", "Movie director should be initialized correctly.")

class TestDataFormatter(unittest.TestCase):

    def setUp(self):
        self.records = [
            {"id": 1, "title": "Book One", "author": "Author A", "tags": ["fiction", "mystery"]},
            {"id": 2, "title": "Book Two", "author": "Author B", "tags": ["non-fiction", "history"]},
        ]
        self.formatter = DataFormatter(self.records)

    def test_display_records_inline(self):
        # Capture the output of display_records_inline
        import io
        import sys

        captured_output = io.StringIO()
        sys.stdout = captured_output
        self.formatter.display_records_inline()
        sys.stdout = sys.__stdout__

        output = captured_output.getvalue()
        self.assertIn("Book One", output)
        self.assertIn("Book Two", output)
        self.assertIn("fiction, mystery", output)
        self.assertIn("non-fiction, history", output)

if __name__ == '__main__':
    unittest.main()