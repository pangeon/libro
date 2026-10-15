from dataclasses import dataclass


@dataclass(kw_only=True)
class MediaItem:
    id: int
    title: str
    publication_year: int
    category: str
    language: str
