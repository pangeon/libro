from dataclasses import dataclass, field
from datetime import datetime

from .media_item import MediaItem


@dataclass(kw_only=False)
class Movie(MediaItem):
    id: int
    title: str
    publication_year: int
    category: str
    language: str
    format: str
    director: str
    translation: str | None = None
    codec: str | None = None
    producer: str | None = None
    description: str | None = None
    rating: float | None = None
    finished_date: datetime | None = None
    tags: list[str] = field(default_factory=list)
