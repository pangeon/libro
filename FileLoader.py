import json
import sys

class FileLoader:
    def __init__(self, file_path) -> None:
        self.file_path = file_path

    def load_file(self, encoding='utf-8') -> str:
        try:
            with open(self.file_path, 'r', encoding=encoding) as file:
                return json.load(file)
        except json.JSONDecodeError:
            print(f"Error decoding JSON from file: {self.file_path}")
            sys.exit(1)
        except FileNotFoundError:
            print(f"File not found: {self.file_path}")
            sys.exit(2)
        except Exception as e:
            print(f"An error occurred while loading the file: {e}")
            sys.exit(3)