class DataFormatter:

    def __init__(self, records: list[dict[str, object]]) -> None:
        self.records = records

    def display_records(self, number_of_records: int = 100) -> None:
        for record in self.records[:number_of_records]:
            print(f"------------{record.get('id')}------------")
            for key, value in record.items():
                if isinstance(value, list):
                    items = []
                    for item in value:
                        items.append(str(item))
                    value = ", ".join(items)
                else:
                    pass
                    
                print(f"{key}: {value}")

    def display_records_inline(self, class_name: str, number_of_columns: int = 10) -> None:
        if not self.records:
            print("No records to display. Your collection is empty.\n")
            return

        lines = self._get_collection_table_header(class_name, number_of_columns)
        for record in self.records:
            lines += "\n" + self._get_collection_table_values_row(
                record["id"], number_of_columns
            )

        print(lines)

    def show_item_header(self, class_name: str, item_id: int, number_of_columns: int = 7) -> None:
        for record in self.records:
            if record["id"] == item_id:
                print(self._get_collection_table_header(class_name, number_of_columns))
                print(self._get_collection_table_values_row(item_id, number_of_columns))
                print()

                for property_key, property_value in record.items():
                    if property_value is None or property_value == []:
                        print(f'--> {property_key} is empty.')

    def _get_collection_table_header(self, class_name: str, number_of_columns: int = 7) -> str:

        match class_name:
            case "Book":
                columns = (
                    ("ID", 5), ("ISBN", 15), ("Title", 30), ("Author", 25),
                    ("Publisher", 25), ("Year", 6), ("Edition", 8),
                    ("Category", 22), ("Language", 8),
                )
            case "Magazine":
                columns = (
                    ("ID", 5), ("ISSN", 15), ("Title", 30), ("Publisher", 25),
                    ("Year", 6), ("Category", 22), ("Series", 22),
                    ("Language", 8),
                )
            case "BoxedGame":
                columns = (
                    ("ID", 5), ("Title", 30), ("Producer", 25),
                    ("Publisher", 25), ("Year", 6), ("Platform", 22),
                    ("Category", 22), ("Language", 8), ("Series", 22),
                )
            case "DigitalGame":
                columns = (
                    ("ID", 5), ("Title", 30), ("Store", 25), ("Producer", 25),
                    ("Publisher", 25), ("Year", 6), ("Platform", 22),
                    ("Category", 22), ("Language", 8), ("Series", 22),
                )
            case "Movie":
                columns = (
                    ("ID", 5), ("Title", 30), ("Year", 6), ("Category", 22),
                    ("Language", 8), ("Format", 10), ("Director", 20),
                )
            case _:
                print("Classname in header is not defined.")
                return ""

        header = " | ".join(f"{name:<{width}}" for name, width in columns[:number_of_columns])
        return f"{header}\n{'-' * len(header)}"

    def _get_collection_table_values_row(self, item_id: int, number_of_columns: int) -> str:

        column_widths: dict[str, int] = { 
            "id": 5, "isbn": 15, "issn": 15, "title": 30, "author": 25, "producer": 25, "publisher": 25, "store": 25, 
            "publication_year": 6, "edition": 8, "category": 22, "platform": 22, "series": 22, "language": 8,
            "format": 10, "director": 20,
        }
        
        for record in self.records:
            if record["id"] == item_id:
                values = []
                for key, value in record.items():
                    if isinstance(value, list):
                        value = ", ".join(map(str, value))
                    values.append(f"{str(value):<{column_widths.get(key, 22)}}")

                    if len(values) == number_of_columns:
                        break
                return " | ".join(values)

        return ""
