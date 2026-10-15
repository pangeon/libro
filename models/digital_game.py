from dataclasses import dataclass, field
from datetime import datetime

from .media_item import MediaItem

@dataclass(kw_only=True) 
class DigitalGame(MediaItem):
    store: str
    producer: str
    publisher: str
    platform: str
    series: str
    translation: str | None = None
    
    additional_authors: list[str] = field(default_factory=list)
    requirements: str | None = None
    description: str | None = None
    rating: float | None = None
    finished_date: datetime | None = None
    tags: list[str] = field(default_factory=list)
