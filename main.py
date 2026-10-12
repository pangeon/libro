from FileLoader import FileLoader
from DataFormatter import DataFormatter

version = float(1.0)

books = FileLoader("data/books.json")
magazines = FileLoader("data/magazines.json")
boxed_games = FileLoader("data/boxed_games.json")
digital_games = FileLoader("data/digital_games.json")
movies = FileLoader("data/movies.json")

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
            DataFormatter(books.load_file()).display_records_inline()
        case "2" | "3" | "4":
            print("Unsupported operation...")
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


        