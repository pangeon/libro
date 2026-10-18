from dataclasses import dataclass, field
from datetime import datetime

from .media_item import MediaItem


@dataclass(kw_only=False)
class Book(MediaItem):
    id: int
    isbn: str
    title: str
    author: str
    publisher: str
    publication_year: int
    edition: int
    category: str
    language: str
    additional_authors: list[str] = field(default_factory=list)
    translator: str | None = None
    pages: int | None = None
    format: str | None = None
    series: str | None = None
    description: str | None = None
    condition: str | None = None
    rating: float | None = None
    finished_date: datetime | None = None
    tags: list[str] = field(default_factory=list)
