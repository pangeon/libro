from utils import FileManager, DataFormatter
from models import Book, BoxedGame, DigitalGame, Magazine, MediaItem, Movie
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

                data_formatter.display_records_inline("Book", 9)
                info_about_operations()
            case "2":
                data_formatter.display_records_inline("Book", 9)

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
                data_formatter.show_item_header("Book", book_id)
                
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

    magazine_list: list[dict[str, object]] = magazines_manager.load_file()
    magazine_service: CollectionService = CollectionService(magazine_list)
    data_formatter: DataFormatter = DataFormatter(magazine_service.get_all())

    try:
        match user_operation:
            case "1":
                print("Your magazines list:")
                data_formatter.display_records_inline("Magazine", 8)
                info_about_operations()
            case "2":
                data_formatter.display_records_inline("Magazine", 8)

                print("You're adding a new magazine to your collection.")
                print("Please enter the following information.")

                try:
                    new_magazine = Magazine(
                        MediaItem.next_id(magazine_service.get_all()),
                        str(input("ISSN: ")),
                        str(input("Title: ")),
                        str(input("Publisher: ")),
                        int(input("Publication Year: ")),
                        str(input("Category: ")),
                        str(input("Series: ")),
                        str(input("Language: ")),
                    )
                except ValueError:
                    print("Incorrect input. Enter valid numbers.")
                    return

                magazine_service.add_record(new_magazine)
                magazines_manager.copy_file()
                magazines_manager.protected_save_file(magazine_service.get_all())

                print("Magazine added successfully ! \n")
                info_about_operations()
            case "3":
                try:
                    magazine_id: int = int(input("Which magazine you want to edit? [ID]: "))
                except ValueError:
                    print("Magazine ID must be a number.")
                    info_about_operations()
                    return

                if magazine_id <= 0:
                    print("Magazine id must be greater than 0.")
                    info_about_operations()
                    return

                magazine_to_edit: dict[str, object] = magazine_service.get_by_record(magazine_id)
                if magazine_to_edit is None:
                    print(f"Magazine with ID {magazine_id} does not exist.")
                    info_about_operations()
                    return

                print(f"Magazine to edit:")
                data_formatter.show_item_header("Magazine", magazine_id, 8)

                field_name: str = str(input("Enter field name: "))
                if field_name not in magazine_to_edit:
                    print("Incorrect field name")
                    info_about_operations()
                    return
                if field_name == "id":
                    print("Editing the magazine ID is not allowed.")
                    info_about_operations()
                    return

                value = input(f'Change "{magazine_to_edit[field_name]}" to: ')
                try:
                    if field_name in ("publication_year", "pages"):
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

                magazines_manager.copy_file()
                magazine_service.update_record(magazine_id, field_name, value)
                magazines_manager.protected_save_file(magazine_service.get_all())

                print("Operation success !")
                info_about_operations()
            case "4":
                try:
                    magazine_id: int = int(input("Which magazine you want to delete? [ID]: "))
                except ValueError:
                    print("Incorrect format. Enter a valid value.")
                    info_about_operations()
                    return

                if magazine_service.get_by_record(magazine_id) is None:
                    print(f"Magazine number: {magazine_id} not found. Try again.")
                    info_about_operations()
                    return

                if input(
                    f'Are you sure you want to delete [Y] '
                    f'[ {magazine_service.get_by_record(magazine_id)["title"]} ]: '
                ) == "Y":
                    magazines_manager.copy_file()
                    magazine_service.delete_record(magazine_id)
                    magazines_manager.protected_save_file(magazine_service.get_all())
                    print(f"Magazine {magazine_id} is deleted.")
                    info_about_operations()
                    return

                print("Operation interrupted.")
                info_about_operations()
            case "exit":
                print()
            case _:
                print("Invalid option.")
    except (OSError, RuntimeError) as error:
        print(f"Operation failed: {error}")

def user_gamebox_operation_choice(user_operation: str) -> None:
    game_list: list[dict[str, object]] = boxed_games_manager.load_file()
    game_service: CollectionService = CollectionService(game_list)
    data_formatter: DataFormatter = DataFormatter(game_service.get_all())

    try:
        match user_operation:
            case "1":
                print("Your shelf of games:")
                data_formatter.display_records_inline("BoxedGame", 9)
                info_about_operations()
            case "2":
                data_formatter.display_records_inline("BoxedGame", 9)

                print("You're adding a new boxed game to your collection.")
                print("Please enter the following information.")

                try:
                    new_game = BoxedGame(
                        MediaItem.next_id(game_service.get_all()),
                        str(input("Title: ")),
                        str(input("Producer: ")),
                        str(input("Publisher: ")),
                        int(input("Publication Year: ")),
                        str(input("Platform: ")),
                        str(input("Category: ")),
                        str(input("Language: ")),
                        str(input("Series: ")),
                    )
                except ValueError:
                    print("Incorrect input. Enter valid numbers.")
                    return

                game_service.add_record(new_game)
                boxed_games_manager.copy_file()
                boxed_games_manager.protected_save_file(game_service.get_all())

                print("Boxed game added successfully ! \n")
                info_about_operations()
            case "3":
                try:
                    game_id: int = int(input("Which game you want to edit? [ID]: "))
                except ValueError:
                    print("Game ID must be a number.")
                    info_about_operations()
                    return

                if game_id <= 0:
                    print("Game id must be greater than 0.")
                    info_about_operations()
                    return

                game_to_edit: dict[str, object] = game_service.get_by_record(game_id)
                if game_to_edit is None:
                    print(f"Game with ID {game_id} does not exist.")
                    info_about_operations()
                    return

                print(f"Game to edit:")
                data_formatter.show_item_header("BoxedGame", game_id, 9)

                field_name: str = str(input("Enter field name: "))
                if field_name not in game_to_edit:
                    print("Incorrect field name")
                    info_about_operations()
                    return
                if field_name == "id":
                    print("Editing the game ID is not allowed.")
                    info_about_operations()
                    return

                value = input(f'Change "{game_to_edit[field_name]}" to: ')
                try:
                    if field_name in ("publication_year", "pages"):
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

                boxed_games_manager.copy_file()
                game_service.update_record(game_id, field_name, value)
                boxed_games_manager.protected_save_file(game_service.get_all())

                print("Operation success !")
                info_about_operations()
            case "4":
                try:
                    game_id: int = int(input("Which game you want to delete? [ID]: "))
                except ValueError:
                    print("Incorrect format. Enter a valid value.")
                    info_about_operations()
                    return

                if game_service.get_by_record(game_id) is None:
                    print(f"Game number: {game_id} not found. Try again.")
                    info_about_operations()
                    return

                if input(
                    f'Are you sure you want to delete [Y] '
                    f'[ {game_service.get_by_record(game_id)["title"]} ]: '
                ) == "Y":
                    boxed_games_manager.copy_file()
                    game_service.delete_record(game_id)
                    boxed_games_manager.protected_save_file(game_service.get_all())
                    print(f"Game {game_id} is deleted.")
                    info_about_operations()
                    return

                print("Operation interrupted.")
                info_about_operations()
            case "exit":
                print()
            case _:
                print("Invalid option.")
    except (OSError, RuntimeError) as error:
        print(f"Operation failed: {error}")

def user_gamedig_operation_choice(user_operation: str) -> None:
    game_list: list[dict[str, object]] = digital_games_manager.load_file()
    game_service: CollectionService = CollectionService(game_list)
    data_formatter: DataFormatter = DataFormatter(game_service.get_all())

    try:
        match user_operation:
            case "1":
                print("Your digital games on cloud:")
                data_formatter.display_records_inline("DigitalGame", 9)
                info_about_operations()
            case "2":
                data_formatter.display_records_inline("DigitalGame", 9)

                print("You're adding a new digital game to your collection.")
                print("Please enter the following information.")

                try:
                    new_game = DigitalGame(
                        MediaItem.next_id(game_service.get_all()),
                        str(input("Title: ")),
                        str(input("Store: ")),
                        str(input("Producer: ")),
                        str(input("Publisher: ")),
                        int(input("Publication Year: ")),
                        str(input("Platform: ")),
                        str(input("Category: ")),
                        str(input("Language: ")),
                        str(input("Series: ")),
                    )
                except ValueError:
                    print("Incorrect input. Enter valid numbers.")
                    return

                game_service.add_record(new_game)
                digital_games_manager.copy_file()
                digital_games_manager.protected_save_file(game_service.get_all())

                print("Digital game added successfully ! \n")
                info_about_operations()
            case "3":
                try:
                    game_id: int = int(input("Which game you want to edit? [ID]: "))
                except ValueError:
                    print("Game ID must be a number.")
                    info_about_operations()
                    return

                if game_id <= 0:
                    print("Game id must be greater than 0.")
                    info_about_operations()
                    return

                game_to_edit: dict[str, object] = game_service.get_by_record(game_id)
                if game_to_edit is None:
                    print(f"Game with ID {game_id} does not exist.")
                    info_about_operations()
                    return

                print(f"Game to edit:")
                data_formatter.show_item_header("DigitalGame", game_id, 9)

                field_name: str = str(input("Enter field name: "))
                if field_name not in game_to_edit:
                    print("Incorrect field name")
                    info_about_operations()
                    return
                if field_name == "id":
                    print("Editing the game ID is not allowed.")
                    info_about_operations()
                    return

                value = input(f'Change "{game_to_edit[field_name]}" to: ')
                try:
                    if field_name in ("publication_year", "pages"):
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

                digital_games_manager.copy_file()
                game_service.update_record(game_id, field_name, value)
                digital_games_manager.protected_save_file(game_service.get_all())

                print("Operation success !")
                info_about_operations()
            case "4":
                try:
                    game_id: int = int(input("Which game you want to delete? [ID]: "))
                except ValueError:
                    print("Incorrect format. Enter a valid value.")
                    info_about_operations()
                    return

                if game_service.get_by_record(game_id) is None:
                    print(f"Game number: {game_id} not found. Try again.")
                    info_about_operations()
                    return

                if input(
                    f'Are you sure you want to delete [Y] '
                    f'[ {game_service.get_by_record(game_id)["title"]} ]: '
                ) == "Y":
                    digital_games_manager.copy_file()
                    game_service.delete_record(game_id)
                    digital_games_manager.protected_save_file(game_service.get_all())
                    print(f"Game {game_id} is deleted.")
                    info_about_operations()
                    return

                print("Operation interrupted.")
                info_about_operations()
            case "exit":
                print()
            case _:
                print("Invalid option.")
    except (OSError, RuntimeError) as error:
        print(f"Operation failed: {error}")

def user_movies_operation_choice(user_operation: str) -> None:
    movie_list: list[dict[str, object]] = movies_manager.load_file()
    movie_service: CollectionService = CollectionService(movie_list)
    data_formatter: DataFormatter = DataFormatter(movie_service.get_all())

    try:
        match user_operation:
            case "1":
                print("Your movies:")
                data_formatter.display_records_inline("Movie", 7)
                info_about_operations()
            case "2":
                data_formatter.display_records_inline("Movie", 7)

                print("You're adding a new movie to your collection.")
                print("Please enter the following information.")

                try:
                    new_movie = Movie(
                        MediaItem.next_id(movie_service.get_all()),
                        str(input("Title: ")),
                        int(input("Publication Year: ")),
                        str(input("Category: ")),
                        str(input("Language: ")),
                        str(input("Format: ")),
                        str(input("Director: ")),
                    )
                except ValueError:
                    print("Incorrect input. Enter valid numbers.")
                    return

                movie_service.add_record(new_movie)
                movies_manager.copy_file()
                movies_manager.protected_save_file(movie_service.get_all())

                print("Movie added successfully ! \n")
                info_about_operations()
            case "3":
                try:
                    movie_id: int = int(input("Which movie you want to edit? [ID]: "))
                except ValueError:
                    print("Movie ID must be a number.")
                    info_about_operations()
                    return

                if movie_id <= 0:
                    print("Movie id must be greater than 0.")
                    info_about_operations()
                    return

                movie_to_edit: dict[str, object] = movie_service.get_by_record(movie_id)
                if movie_to_edit is None:
                    print(f"Movie with ID {movie_id} does not exist.")
                    info_about_operations()
                    return

                print(f"Movie to edit:")
                data_formatter.show_item_header("Movie", movie_id)

                field_name: str = str(input("Enter field name: "))
                if field_name not in movie_to_edit:
                    print("Incorrect field name")
                    info_about_operations()
                    return
                if field_name == "id":
                    print("Editing the movie ID is not allowed.")
                    info_about_operations()
                    return

                value = input(f'Change "{movie_to_edit[field_name]}" to: ')
                try:
                    if field_name in ("publication_year", "pages"):
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

                movies_manager.copy_file()
                movie_service.update_record(movie_id, field_name, value)
                movies_manager.protected_save_file(movie_service.get_all())

                print("Operation success !")
                info_about_operations()
            case "4":
                try:
                    movie_id: int = int(input("Which movie you want to delete? [ID]: "))
                except ValueError:
                    print("Incorrect format. Enter a valid value.")
                    info_about_operations()
                    return

                if movie_service.get_by_record(movie_id) is None:
                    print(f"Movie number: {movie_id} not found. Try again.")
                    info_about_operations()
                    return

                if input(
                    f'Are you sure you want to delete [Y] '
                    f'[ {movie_service.get_by_record(movie_id)["title"]} ]: '
                ) == "Y":
                    movies_manager.copy_file()
                    movie_service.delete_record(movie_id)
                    movies_manager.protected_save_file(movie_service.get_all())
                    print(f"Movie {movie_id} is deleted.")
                    info_about_operations()
                    return

                print("Operation interrupted.")
                info_about_operations()
            case "exit":
                print()
            case _:
                print("Invalid option.")
    except (OSError, RuntimeError) as error:
        print(f"Operation failed: {error}")

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


        