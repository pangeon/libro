from utils import FileManager, DataFormatter
from models import Book, MediaItem
from datetime import date
from service import CollectionService

version = float(1.0)

books_manager: FileManager = FileManager("data/books.json")
magazines_manager: FileManager = FileManager("data/magazines.json")
boxed_games_manager: FileManager = FileManager("data/boxed_games.json")
digital_games_manager: FileManager = FileManager("data/digital_games.json")
movies_manager: FileManager = FileManager("data/movies.json")

def welcome_message() -> None:
    print(
f"""-- LIBRO VER: {version} --

Choose any option or type 'exit' to exit the program:

1. Books
2. Magazines
3. Digital DVD/CD boxed games
4. Digital games 
5. HD/DVD/VCD movies

--------------------""")

def info_about_operations() -> None:
    print("Available operations: \n1. SHOW \n2. ADD NEW \n3. EDIT \n4. DELETE")

def user_book_operation_choice(user_operation: str) -> None:

    book_list: list[dict[str, object]] = books_manager.load_file()
    book_service: CollectionService = CollectionService(book_list)
    data_formatter: DataFormatter = DataFormatter(book_service.get_all())

    try:
        match user_operation:
            case "1":
                print("Your book list:")

                data_formatter.display_records_inline(7)
                info_about_operations()

            case "2":
                data_formatter.display_records_inline(7)

                print("---------------------------------")
                print("You're adding a new book to your collection.")
                print("Please enter the following information.")

                try:
                    new_book = Book(
                            MediaItem.next_id(book_service.get_all()),
                            str(input("ISBN: ")),
                            str(input("Title: ")),
                            str(input("Author: ")),
                            str(input("Publisher: ")),
                            int(input("Publication Year: ")),
                            int(input("Edition: ")),
                            str(input("Category: ")),
                            str(input("Language: ")),
                        )
                except ValueError:
                    print("Incorrect input. Enter valid numbers.")
                    return

                book_service.add_record(new_book)
                books_manager.copy_file()
                books_manager.protected_save_file(book_service.get_all())
                
                print("Book added successfully ! \n")
                info_about_operations()
            case "3":
                try:
                    book_id: int = int(input("Which book you want to edit? [ID]: "))
                except ValueError:
                    print("Book ID must be a number.")
                    info_about_operations()
                    return
                
                if book_id <= 0:
                    print(f'Book id to must be greater than 0')
                    info_about_operations()
                    return
                
                book_to_edit: dict[str, object] = book_service.get_by_record(book_id)

                if book_to_edit is None:
                    print(f"Book with ID {book_id} does not exist.")
                    info_about_operations()
                    return
                
                print("Book to edit:\n")
                data_formatter.show_book_header(book_id)
                
                field_name: str = str(input(
                    f'Wchich field you want to edit: \n'
                    f'--> Expected format date: YYYY-MM-DD\n'
                    f'--> Expected tags and additional_authors format: item_1, item_2, item_3\n'
                    f'Enter field name: '))

                if field_name not in book_to_edit:
                    print("Incorrect field name")
                    info_about_operations()
                    return
                if field_name == "id":
                    print("Editing the book ID is not allowed.")
                    info_about_operations()
                    return
                
                value = input(f'Change "{book_to_edit[field_name]}" to: ')

                try:
                    if field_name in ("id", "publication_year", "edition", "pages"):
                        value = int(value)
                    elif field_name == "rating":
                        value = float(value)
                    elif field_name in ("tags", "additional_authors"):
                        value = [item.strip() for item in value.split(",") if item.strip()]
                    elif field_name == "finished_date":
                        value = date.fromisoformat(value).isoformat() + "T00:00:00"
                except ValueError:
                    print("Incorrect format. Enter a valid value.")
                    info_about_operations()
                    return

                books_manager.copy_file()
                book_service.update_record(book_id, field_name, value)
                books_manager.protected_save_file(book_service.get_all())
                
                print("Operation success !")
                info_about_operations()
            case "4":
                try:
                    book_id: int = int(input("Which book you want to delete? [ID]: "))
                except ValueError:
                    print("Incorrect format. Enter a valid value.")
                    info_about_operations()
                    return

                if book_service.get_by_record(book_id) == None:
                    print(f"Book number: {book_id} not found. Try again.")
                    info_about_operations()
                    return
                else:    
                    if input(
                        f'Are you sure you want to delete [Y] '
                        f'[ {book_service.get_by_record(book_id)["title"]} ]: '
                    ) == "Y":
                        books_manager.copy_file()
                        book_service.delete_record(book_id)
                        books_manager.protected_save_file(book_service.get_all())
                        print(f'Book {book_id} is deleted.')
                        info_about_operations()
                        return
                    else:
                        print("Operation interrupted.")
                        info_about_operations()
                        return
                
            case "exit":
                print()
            case _:
                print("Invalid option.")
    except (OSError, RuntimeError) as error:
        print(f"Operation failed: {error}")

def user_magazines_operation_choice(user_operation: str) -> None:
    match (user_operation):
        case "1":
            print("Your magazines list:")
            DataFormatter(magazines_manager.load_file()).display_records()
        case "2" | "3" | "4":
            print("Unsupported operation...")
        case "exit":
            print()
        case _:
            print("Invalid option.")

def user_gamebox_operation_choice(user_operation: str) -> None:
    match (user_operation):
        case "1":
            print("Your shelf of games:")
            DataFormatter(boxed_games_manager.load_file()).display_records()
        case "2" | "3" | "4":
            print("Unsupported operation...")
        case "exit":
            print()
        case _:
            print("Invalid option.")

def user_gamedig_operation_choice(user_operation: str) -> None:
    match (user_operation):
        case "1":
            print("Your digital games on cloud:")
            DataFormatter(digital_games_manager.load_file()).display_records()
        case "2" | "3" | "4":
            print("Unsupported operation...")
        case "exit":
            print()
        case _:
            print("Invalid option.")

def user_movies_operation_choice(user_operation: str) -> None:
    match (user_operation):
        case "1":
            print("Your movies:")
            DataFormatter(movies_manager.load_file()).display_records()
        case "2" | "3" | "4":
            print("Unsupported operation...")
        case "exit":
            print()
        case _:
            print("Invalid option.")

def main():
    welcome_message()

    while(True):

        user_anwer = str(input())
        
        match(user_anwer):
            case "1":
                print("You choosed books catalog.\n")
                info_about_operations()
                while(True):
                    user_operation = str(input())
                    user_book_operation_choice(user_operation)

                    if (user_operation == "exit"):
                        break
                break
            case "2":
                print("You choosed magazines catalog.\n")
                info_about_operations()
                while(True):
                    user_operation = str(input())
                    user_magazines_operation_choice(user_operation)

                    if (user_operation == "exit"):
                        break
                break
            case "3":
                print("You choosed DVD/CD boxed games catalog.\n")
                info_about_operations()
                while(True):
                    user_operation = str(input())
                    user_gamebox_operation_choice(user_operation)

                    if (user_operation == "exit"):
                        break
                break
            case "4":
                print("You choosed digital games catalog.\n")
                info_about_operations()
                while(True):
                    user_operation = str(input())
                    user_gamedig_operation_choice(user_operation)

                    if (user_operation == "exit"):
                        break
                break
            case "5":
                print("You choosed movies catalog.\n")
                info_about_operations()
                while(True):
                    user_operation = str(input())
                    user_movies_operation_choice(user_operation)

                    if (user_operation == "exit"):
                        break
                break
            case "exit":
                print("Close program.")
                break
            case _:
                print("Invalid option.")

if __name__ == "__main__":
    main()


        