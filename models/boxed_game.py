from dataclasses import dataclass, field
from datetime import datetime

from .media_item import MediaItem


@dataclass(kw_only=True)
class BoxedGame(MediaItem):
    producer: str
    publisher: str
    platform: str
    series: str
    translation: str | None = None
    additional_authors: list[str] = field(default_factory=list)
    ean_upc: str | None = None
    requirements: str | None = None
    description: str | None = None
    condition: str | None = None
    rating: float | None = None
    finished_date: datetime | None = None
    tags: list[str] = field(default_factory=list)
