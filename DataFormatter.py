class DataFormatter:
    def __init__(self, records: list[dict[str, object]]) -> None:
        self.records = records

    def display_records(self, number_of_records: int = 100) -> None:
        for record in self.records[:number_of_records]:
            print(f"------------{record.get('id')}------------")
            for key, value in record.items():
                # 1. isinstance(value, list) sprawdza, czy wartość jest listą.
                # 2. przechodzi po kolejnych elemtach listy i skleja je z napisem
                # 3. inny sposób: value = ", ".join(str(item) for item in value)
                if isinstance(value, list):
                    items = []
                    for item in value:
                        items.append(str(item))
                    value = ", ".join(items)
                else:
                    pass
                    
                print(f"{key}: {value}")

    def display_records_inline(self, number_of_details: int = 10) -> None:
            lines = ""
            for record in self.records:
                lines += "\n"
                # podkreślenie _ to nazwa dla wartości, której nie zamierzamy używać. 
                # klucz _ jest pomijany, bo funkcja wypisuje same wartości.
                for _, value in list(record.items())[:number_of_details]:
                    if isinstance(value, list):
                        # 1. map(str, value) stosuje str() do każdego elementu listy. To zamienia elementy na napisy, nawet jeśli są np. liczbami.
                        # 2. ", ".join(...) łączy te napisy, wstawiając między nie separator ", ".
                        value = ", ".join(map(str, value))
                    else:
                        pass
                    
                    lines += f"{value} | "

            print(lines)
                