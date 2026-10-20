from utils import FileManager, DataFormatter
from models import Book, Magazine, BoxedGame, DigitalGame, Movie

version = float(1.0)

books = FileManager("data/books.json")
magazines = FileManager("data/magazines.json")
boxed_games = FileManager("data/boxed_games.json")
digital_games = FileManager("data/digital_games.json")
movies = FileManager("data/movies.json")

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
    match (user_operation):
        case "1":
            print("Your book list:")
            DataFormatter(books.load_file()).display_records()
        case "2":
            # tworzę obiekt listy z wczytując plik JSON
            books_list = books.load_file()
            DataFormatter(books_list).display_records_inline(5)
            print("---------------------------------")

            print("You're adding a new book to your collection.")
            print("Please enter the following information.")
            # modyfikuje listę dodając do niej nowy rekord na podstawie wzorca z klasy Book.
            new_book = Book(
                    int(input("ID: ")),
                    str(input("ISBN: ")),
                    str(input("Title: ")),
                    str(input("Author: ")),
                    str(input("Publisher: ")),
                    int(input("Publication Year: ")),
                    int(input("Edition: ")),
                    str(input("Category: ")),
                    str(input("Language: ")),
                )
            
            # __dict__to słownik nazwa_pola: wartość.
            books_list.append(new_book.__dict__)
            try:
                # nadpisuje plik JSON nową listą z dodanym rekordem.
                books.save_file(books_list)
                print("Book added successfully ! \n")
                info_about_operations()
            except Exception as e:
                print(f"Error occurred while saving books, try again !")
                print(f"Error details: {e}")

        case "3":
            try:
                book_id = int(input("Which book you want to edit? [ID]: "))
                books_list = books.load_file()
                book_to_edit = []
                if book_id <= 0:
                    raise IndexError
                elif isinstance(book_id, str):
                    raise ValueError
                else:
                    for book in books_list:
                        if book["id"] == book_id:
                            book_to_edit = book
                            book_id = book["id"]
                            print("Book to edit:")
                            print(f'{book["id"]} | {book["isbn"]} | {book["title"]} | {book["author"]}')

                    field_name = input("Wchich field you want to edit: ")
                    if field_name not in book_to_edit:
                        raise Exception
                    for key, value in book_to_edit.items():
                        if str(key) == str(field_name):
                            value = input(f'Change "{book_to_edit[key]}" to: ')
                            book_to_edit[key] = value
                            print("Operation success !")

                    books.save_file(books_list)
                    
            except ValueError as e:
                print(f'Incorrect format data')
                print(e)
            except IndexError as e:
                print(f'Book id to must be higher than 0 and lower {len(books_list)}')
            except AttributeError as e:
                print(f'Book id does not exist. Try again.')
            except Exception as e:
                print(f"Attribute {field_name} doesn't exist")

            
        case "4":
            book_id = input("Which book you want to delete? [ID]: ")
            books_list = books.load_file()

            for book in books_list:
                if str(book["id"]) == book_id:
                    books_list.remove(book)
                    books.save_file(books_list)
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
            DataFormatter(magazines.load_file()).display_records()
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
            DataFormatter(boxed_games.load_file()).display_records()
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
            DataFormatter(digital_games.load_file()).display_records()
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
            DataFormatter(movies.load_file()).display_records()
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

main()


        