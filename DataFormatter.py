class DataFormatter:
    def __init__(self, records: list[dict[str, object]]) -> None:
        self.records = records

    def display_records(self, number_of_records: int = 100) -> None:
        for record in self.records[:number_of_records]:
            print(f"------------{record.get('id')}------------")
            for key, value in record.items():
                print(f"{key}: {value}")

    def display_records_inline(self, number_of_details: int = 10) -> None:
            lines = str(f"")
            for record in self.records:
                lines += "\n"
                for value in list(record.items())[:number_of_details]:
                    lines += f"{value[1]} | "

            print(f"{lines}")
                