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

    def display_records_inline(self, number_of_details: int = 10) -> None:
            lines = ""
            header = f'{"ID":<22} | {"ISBN":<22} | {"Title":<22} | {"Author":<22} | {"Publisher":<22} | {"Year":<22} | {"Edition":<22} | \n'
            header += "-" * len(header)
            lines += header
            for record in self.records:
                lines += "\n"
                
                for _, value in list(record.items())[:number_of_details]:
                    if isinstance(value, list):
                        value = ", ".join(map(str, value))
                    else:
                        pass
                    
                    lines += f"{value:<22} | "

            print(lines)

    def show_book_header(self, book_id: int) -> None:
        for record in self.records:
            if record["id"] == book_id:
                print(
                    f'{"ID":<5} | '
                    f'{"ISBN":<15} | '
                    f'{"Title":<30} | '
                    f'{"Author":<25} | '
                    f'{"Publisher":<25} | '
                    f'{"Year":<6} | '
                    f'{"Edition":<8} | '
                    f'{"Category":<22} | '
                    f'{"Language":<8}'
                )
                print("-" * 160)
            
                print(
                    f'{record["id"]:<5} | '
                    f'{record["isbn"]:<15} | '
                    f'{record["title"]:<30} | '
                    f'{record["author"]:<25} | '
                    f'{record["publisher"]:<25} | '
                    f'{record["publication_year"]:<6} | '
                    f'{record["edition"]:<8} | '
                    f'{record["category"]:22} | '
                    f'{record["language"]:<8}'
                )
                print()

                for property_key, property_value in record.items():
                    if property_value is None or property_value == []:
                        print(f'--> {property_key} is empty.')


                