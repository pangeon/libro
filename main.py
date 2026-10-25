from utils import FileManager, DataFormatter
from models import Book, Magazine, BoxedGame, DigitalGame, Movie

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

def show_book_header(book: dict[str, object]) -> None:
    print(
        f'{"ID":<5} | '
        f'{"ISBN":<15} | '
        f'{"Title":<30} | '
        f'{"Author":<25} | '
        f'{"Publisher":<25} | '
        f'{"Year":<6} | '
        f'{"Edition":<8} | '
        f'{"Category":<20} | '
        f'{"Language":<8}'
    )
    print("-" * 160)

    print(
        f'{book["id"]:<5} | '
        f'{book["isbn"]:<15} | '
        f'{book["title"]:<30} | '
        f'{book["author"]:<25} | '
        f'{book["publisher"]:<25} | '
        f'{book["publication_year"]:<6} | '
        f'{book["edition"]:<8} | '
        f'{book["category"]:20} | '
        f'{book["language"]:<8}'
    )

    for property_key, property_value in book.items():
        if property_value is None:
            print(f'--> {property_key} is empty.')

def info_about_operations() -> None:
    print("Available operations: \n1. SHOW \n2. ADD NEW \n3. EDIT \n4. DELETE")

def user_book_operation_choice(user_operation: str) -> None:
    match (user_operation):
        case "1":
            print("Your book list:")
            DataFormatter(books_manager.load_file()).display_records_inline(8)
        case "2":
            books_list = books_manager.load_file()
            DataFormatter(books_list).display_records_inline(5)
            
            print("---------------------------------")
            print("You're adding a new book to your collection.")
            print("Please enter the following information.")

            new_book = Book(
                    int(len(books_list) + 1),
                    str(input("ISBN: ")),
                    str(input("Title: ")),
                    str(input("Author: ")),
                    str(input("Publisher: ")),
                    int(input("Publication Year: ")),
                    int(input("Edition: ")),
                    str(input("Category: ")),
                    str(input("Language: ")),
                )
            books_list.append(new_book.__dict__)
            try:
                books_manager.copy_file()
                books_manager.save_file(books_list)
                print("Book added successfully ! \n")
                info_about_operations()
            except Exception as e:
                print(f"Error occurred while saving books, try again !")
                print(f"Error details: {e}")

        case "3":
            try:
                book_id: int = int(input("Which book you want to edit? [ID]: "))
                
                if book_id <= 0:
                    print(f'Book id to must be higher than 0')
                else:
                    books_list: dict[str, object] = books_manager.load_file()

                    book_to_edit: dict[str, object] = next(
                        (book for book in books_list if book["id"] == book_id), 
                        None
                    )
                    if book_to_edit is None:
                        print(f"Book with ID {book_id} does not exist.")
                    else:
                        print("Book to edit:\n")
                        show_book_header(book_to_edit)
                        
                        field_name: str = str(input("Wchich field you want to edit: "))

                        if field_name not in book_to_edit:
                            print("Incorrect field name")
                        elif field_name == "id":
                            print("Editing the book ID is not allowed.")
                        else:
                            value = input(f'Change "{book_to_edit[field_name]}" to: ')
                    
                            if field_name in ("id", "publication_year", "edition", "pages"):
                                value = int(value)
                            elif field_name == "rating":
                                value = float(value)

                            books_manager.copy_file()
                            book_to_edit[field_name] = value
                            books_manager.save_file(books_list)
                            
                            print("Operation success !")

            except ValueError as e:
                print(f'Incorrect format data. Enter a valid number where required.')
        case "4":
            book_id = input("Which book you want to delete? [ID]: ")
            books_list = books_manager.load_file()

            for book in books_list:
                if str(book["id"]) == book_id:
                    books_list.remove(book)
                    books_manager.copy_file()
                    books_manager.save_file(books_list)
                    print(f'Book number: {book_id} deleted. \n')
                    break
            else:
                print(f'Book number: {book_id} not found. Try again.')

        case "exit":
            print()
        case _:
            print("Invalid option.")

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


        