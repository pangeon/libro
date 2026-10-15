# Architecture

1) User Interface
    - Display, forms, user actions

2) Application Logic Layer
    - Adding, editing, deleting, validating

3) Entities and Repositories
    - Object Model + Data Access Interface

4) JSON Files
    - Reading, writing, updating, and deleting data

# File and directory tree

```
libro/
├── models/
│   ├── media_item.py
│   ├── book.py
│   ├── magazine.py
│   ├── boxed_game.py
│   ├── digital_game.py
│   └── movie.py
├── repositories/
│   └── ...
├── services/
│   └── ...
├── data/
│   ├── books.json
│   ├── magazines.json
│   ├── boxed_games.json
│   ├── digital_games.json
│   └── movies.json
└── main.py
```

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
    - aditional_authors (LIST(STR))
    - translator (STR)
    - pages (INT)
    - format (STR)
    - series (STR)
    - description (STR)
    - condition (STR)
    - rating (FLOAT)
    - finished_date (DATETIME)
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
    - finished_date (DATETIME)
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
    - aditional_authors (LIST(STR))
    - EAN/UPC (STR)
    - requirements (STR)
    - description (STR)
    - condition (STR)
    - rating (FLOAT)
    - finished_date (DATETIME)
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
    - aditional_authors (LIST(STR))
    - requirements (STR)
    - description (STR)
    - rating (FLOAT)
    - finished_date (DATETIME)
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
    - finished_date (DATETIME)
    - tags (LIST(STR))
---