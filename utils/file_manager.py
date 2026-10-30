from datetime import datetime
import json
from tempfile import NamedTemporaryFile
import os

class FileManager:
    def __init__(self, file_path) -> None:
        self.file_path = file_path

    def load_file(self, encoding='utf-8') -> list[dict[str, object]]:
        try:
            with open(self.file_path, 'r', encoding=encoding) as file:
                return json.load(file)
        except FileNotFoundError:
            print(f"File not found: {self.file_path}")
        except json.JSONDecodeError:
            print(f"Error decoding JSON from file: {self.file_path}")

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

    def protected_save_file(self, data, encoding="utf-8") -> None:

        temp_path = None

        try:
            with NamedTemporaryFile(mode="w", encoding=encoding, dir="data/", suffix=".tmp", delete=False) as file:
                temp_path = file.name
                json.dump(data, file, indent=4, ensure_ascii=False)
                file.write("\n")
                file.flush()
                os.fsync(file.fileno())

            os.replace(temp_path, self.file_path)
        finally:
            if temp_path is not None and os.path.exists(temp_path):
                os.remove(temp_path)
           
    def _get_timestamp(self) -> str:
        return datetime.now().strftime("%Y%m%d_%H%M%S")
            