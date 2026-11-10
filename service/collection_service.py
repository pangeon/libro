from dataclasses import asdict, is_dataclass

class CollectionService:

    def __init__(self, collection: list[dict[str, object]]):
        self.collection = collection

    def get_all(self) -> list[dict[str, object]]:
        return self.collection

    def get_index(self, id: int) -> dict[str, object]:
        return self.collection[id]

    def get_by_record(self, record_id: int) -> dict[str, object]:
        for record in self.collection:
            if record.get("id") == record_id:
                return record

    def add_record(self, record: dict[str, object] | object) -> None:
        if self.collection is None:
            self.collection = []
        
        if is_dataclass(record) and not isinstance(record, type):
            record = asdict(record)

        if not isinstance(record, dict):
            raise TypeError("Record must be a dictionary or dataclass.")

        self.collection.append(record)

    def delete_record(self, record_id: int) -> None:
        for record in self.collection:
            if record.get("id") == record_id:
                self.collection.remove(record)

    def update_record(self, record_id: int, field_name: str, value: str | int | list) -> None:
        for record in self.collection:
            if record.get("id") == record_id:
                record[field_name] = value
