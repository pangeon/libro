import unittest
from utils import FileManager
from service.collection_service import CollectionService
from models.book import Book

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

if __name__ == '__main__':
    unittest.main()