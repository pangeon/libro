# Architecture

1) Command-line interface and application flow (`main.py`)
    - Menus, user input, and catalog operations
    - All catalogs support show, add, edit, and delete operations

2) Domain models (`models/`)
    - Data classes for books, magazines, boxed and digital games, and movies

3) Collection operations (`service/`)
    - `CollectionService` provides in-memory collection lookup and CRUD methods

4) Utilities (`utils/`)
    - JSON file access and record formatting

5) JSON data and backups (`data/`)
    - Catalog records stored in JSON files
    - A copy of the relevant data file is created in `data/copy/` before changes are saved

# File and directory tree

```
libro/
|
├── data/
│   ├── copy/
│   ├── books.json
│   ├── boxed_games.json
│   ├── digital_games.json
│   ├── magazines.json
│   └── movies.json
├── models/
│   ├── __init__.py
│   ├── book.py
│   ├── boxed_game.py
│   ├── digital_game.py
│   ├── magazine.py
│   ├── media_item.py
│   └── movie.py
├── service/
│   ├── __init__.py
│   └── collection_service.py
├── utils/
│   ├── __init__.py
│   ├── data_formatter.py
│   └── file_manager.py
├── main.py
├── start.sh
├── test.py
└── README.MD
```

# Running and tests

Run the application from the project directory:

```bash
python3 main.py
```

Run the unit tests with:

```bash
python3 test.py
```

The application implements full CRUD operations for books, magazines, boxed
games, digital games, and movies.

# Data model

## Data entities
```
[pl-name]        [entity]
------------------------------------
- Książki       - books
- Magazyny      - magazines
- Gry pudełkowe - boxed games
- Gry cyfrowe   - digital games
- Filmy         - movies
```

### Books

- **REQUIRED**:
    - id (INT)
    - isbn (STR)
    - title (STR)
    - author (STR)
    - publisher (STR)
    - publication_year (INT)
    - edition (INT)
    - category (STR)
    - language (STR)
    

- **OPTIONAL**:
    - additional_authors (LIST(STR))
    - translator (STR)
    - pages (INT)
    - format (STR)
    - series (STR)
    - description (STR)
    - condition (STR)
    - rating (FLOAT)
    - finished_date (DATETIME; stored as an ISO 8601 string in JSON)
    - tags (LIST(STR))
---
### Magazines

- **REQUIRED**:
    - id (INT)
    - issn (STR)
    - title (STR)
    - publisher (STR)
    - publication_year (INT)
    - category (STR)
    - series (STR)
    - language (STR)

- **OPTIONAL**:
    - pages (INT)
    - format (STR)
    - description (STR)
    - condition (STR)
    - finished_date (DATETIME; stored as an ISO 8601 string in JSON)
    - tags (LIST(STR))
---
### Boxed games

- **REQUIRED**:
    - id (INT)
    - title (STR)
    - producer (STR)
    - publisher (STR)
    - publication_year (INT)
    - platform (STR)
    - category (STR)
    - language (STR)
    - series (STR)
    
- **OPTIONAL**:
    - translation (STR) ex. SUBTITLES[PL, ENG, ...], DUBBING[PL, ENG]
    - additional_authors (LIST(STR))
    - ean_upc (STR)
    - requirements (STR)
    - description (STR)
    - condition (STR)
    - rating (FLOAT)
    - finished_date (DATETIME; stored as an ISO 8601 string in JSON)
    - tags (LIST(STR))
---
### Digital games

- **REQUIRED**:
    - id (INT)
    - title (STR)
    - store (STR)
    - producer (STR)
    - publisher (STR)
    - publication_year (INT)
    - platform (STR)
    - category (STR)
    - language (STR)
    - series (STR)
    
- **OPTIONAL**:
    - translation (STR) ex. SUBTITLES[PL, ENG, ...], DUBBING[PL, ENG]
    - additional_authors (LIST(STR))
    - requirements (STR)
    - description (STR)
    - rating (FLOAT)
    - finished_date (DATETIME; stored as an ISO 8601 string in JSON)
    - tags (LIST(STR))
---
### Movies

- **REQUIRED**:
    - id (INT)
    - title (STR)
    - publication_year (INT)
    - category (STR)
    - language (STR)
    - format (STR)
    - director (STR)

- **OPTIONAL**:
    - translation (STR) ex. SUBTITLES[PL, ENG, ...], DUBBING[PL, ENG]
    - codec (STR)
    - producer (STR)
    - description (STR)
    - rating (FLOAT)
    - finished_date (DATETIME; stored as an ISO 8601 string in JSON)
    - tags (LIST(STR))
---
