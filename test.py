import unittest
from utils import FileManager

class TestFileManager(unittest.TestCase):

    def test_load_file_returns_list(self):
        file_manager = FileManager("data/books.json")
        self.assertIsInstance(file_manager.load_file(), list, "The loaded data should be a list.")
        self.assertTrue(len(file_manager.load_file()) > 0, "The loaded list should not be empty.")
        self.assertTrue(type(file_manager.load_file()[0].get("id")) is int, "The first item in the list should have a 'id' key of type int.")

if __name__ == '__main__':
    unittest.main()