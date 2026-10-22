**Najważniejsze problemy**
---
1. **Edycja zmienia typy danych**

    *main.py → user_book_operation_choice(), operacja 3*

    - Wartości pobierane przez input() są zawsze tekstem. W rezultacie edycja publication_year, edition, pages albo rating zmieni liczbę na str.

    - Przykładowo publication_year: 2012 może stać się publication_year: "2012". JSON nadal będzie poprawny składniowo, ale struktura danych przestanie być spójna. Dalszy kod może się na tym wyłożyć.

2. **Dodawanie nie kontroluje identyfikatorów**

    *main.py → operacja 2*

    - Użytkownik sam wpisuje ID. Nie ma sprawdzenia, czy identyfikator już istnieje, czy jest dodatni ani czy nie został przypadkowo użyty ponownie.

    - Dwa rekordy z id = 5 sprawią, że edycja lub usuwanie mogą dotyczyć niewłaściwego egzemplarza. ID powinno być generowane automatycznie.

3. **Błędna obsługa braku rekordu przy edycji**

    *main.py → operacja 3*

    - book_to_edit zaczyna jako pusta lista. Jeśli wskazanego książkowego ID nie ma, program nadal pyta o nazwę pola i dopiero później zgłasza wyjątek.

    - Dodatkowo except Exception przechwytuje błędy niezwiązane z nieistniejącym polem i wyświetla mylący komunikat. Lepiej jawnie sprawdzić wynik wyszukiwania i przerwać operację przed pytaniem o pole.

~~4. **Zapis może uszkodzić plik danych**~~

    *utils/file_manager.py*

    - save_file() otwiera plik w trybie w, który natychmiast go skraca. Jeśli zapis zostanie przerwany, np. przez awarię procesu, możesz stracić zawartość kolekcji.

    - Warto zapisywać najpierw do pliku tymczasowego w tym samym katalogu, a następnie podmieniać plik docelowy. Przy danych osobistej kolekcji kopia zapasowa również nie jest luksusem.

~~5. **FileManager kończy cały program**~~

    *utils/file_manager.py*

    - load_file() i save_file() wywołują sys.exit() przy błędach. Warstwa dostępu do plików nie powinna decydować o zakończeniu aplikacji.

    - Powinna zgłosić odpowiedni wyjątek. Interfejs zdecyduje, czy wyświetlić komunikat i pozwolić spróbować ponownie, czy zakończyć program.

6. **Testy nie sprawdzają działania CRUD**

    *test.py*

    - Obecny test sprawdza, czy dane można wczytać i czy lista nie jest pusta. Nie testuje dodawania, edycji, usuwania, niepoprawnych danych ani braku pliku.

    - Co gorsza, korzysta z prawdziwego data/books.json, więc rozbudowanie testów bez izolacji może przypadkiem zmienić Twoją kolekcję.

**Dodatkowe problemy w main.py**
---

- Warunek isinstance(book_id, str) po wcześniejszym int(input(...)) jest martwy. W tym miejscu book_id nie będzie tekstem.

- Komunikat o nieprawidłowym ID porównuje identyfikator z len(books_list). ID nie musi być kolejnym numerem na liście, więc komunikat może wprowadzać w błąd.

- Usuwanie usuwa pierwszy pasujący rekord. Przy zduplikowanych ID pozostawia pozostałe duplikaty.

- Po wyjściu z katalogu program nie wraca do głównego menu, tylko kończy działanie.

- Obsługa błędów jest niespójna: niektóre operacje mają try/except, inne mogą zakończyć się wyjątkiem.

- Wartości opcjonalne, takie jak translator, series czy finished_date, nie są dostępne podczas dodawania książki, mimo że model je obsługuje.


**Poblemy w UI**
---
| Obecnie                                           | Proponowana zmiana
| :-------------------------------------------------| :-----------------------------------------------------------|
| Użytkownik ręcznie wpisuje ID przy dodawaniu      | ID generowane automatycznie                                 |
| Użytkownik wpisuje nazwę pola do edycji           | Lista dostępnych pól do wyboru                              |
| Brak książki powoduje późniejszy wyjątek	        | Komunikat „Nie znaleziono książki o ID X” i powrót do menu  |
| Usuwanie następuje natychmiast                    | Wyświetlenie tytułu i prośba o potwierdzenie                |
| Błędna liczba może zostać zapisana jako tekst     | Walidacja i ponowne pytanie o poprawną wartość              |
| Lista rekordów jest drukowana bez kontroli widoku | Stronicowanie, wyszukiwanie i filtrowanie                   |
| Komunikaty mieszają języki                        | Jeden język interfejsu, najlepiej polski                    |


**Oczekiwany rezultat zmian**

```
Edycja książki: Solaris (ID: 1)

1. Tytuł: Solaris
2. Autor: Stanisław Lem
3. Wydawnictwo: Wydawnictwo Literackie
4. Rok wydania: 2012
5. Ocena: 9.0
0. Powrót

Wybierz pole:
```

**Plan refaktoryzacji Libro**
----
~~1. Zabezpieczyć zapis i obsługę błędów~~
~~    - Usunąć sys.exit() z FileManager, dodać bezpieczny zapis pliku i czytelne wyjątki.~~

2. Naprawić CRUD książek
    - Automatyczne ID, walidacja typów, obsługa brakujących rekordów i poprawne usuwanie.

3. Wydzielić CatalogService
    - Przenieść wspólne operacje poza main.py i nie kopiować CRUD dla każdej kolekcji.

4. Dodać testy izolowane
    - Testować CRUD na tymczasowych plikach JSON, bez modyfikowania prywatnych danych.

5. Ujednolicić menu i komunikaty
    - Jeden przepływ dla wszystkich kolekcji, wybór pól, potwierdzenia i powrót do menu.

6. Rozszerzać CRUD na pozostałe modele
    - Najpierw czasopisma, potem gry i filmy, wykorzystując już sprawdzoną logikę.