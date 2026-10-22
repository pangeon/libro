from datetime import datetime
import json

class FileManager:
    def __init__(self, file_path) -> None:
        self.file_path = file_path

    def load_file(self, encoding='utf-8') -> dict:
        try:
            with open(self.file_path, 'r', encoding=encoding) as file:
                return json.load(file)
        except json.JSONDecodeError:
            print(f"Error decoding JSON from file: {self.file_path}")
        except FileNotFoundError:
            print(f"File not found: {self.file_path}")

    def save_file(self, data, encoding='utf-8') -> None:
        try:
            with open(self.file_path, 'w', encoding=encoding) as file:
                json.dump(data, file, indent=4)
        except json.JSONDecodeError:
            print(f"Error decoding JSON from file: {self.file_path}")
        except FileNotFoundError:
            print(f"File not found: {self.file_path}")

    def copy_file(self, destination_path = "data/copy/") -> None:
        timestamp: str = self._get_timestamp()
        copy_path: str = f"{destination_path}copy_{timestamp}.json"

        try:
            with open(self.file_path, 'r') as source_file:
                data = source_file.read()

            with open(copy_path, 'x') as copy_file:
                copy_file.write(data)

        except OSError as e:
            raise RuntimeError(f"Nie udało się utworzyć kopii pliku {self.file_path}: {e}") from e

    def _get_timestamp(self) -> str:
        return datetime.now().strftime("%Y%m%d_%H%M%S")
            