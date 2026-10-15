from dataclasses import dataclass, field
from datetime import datetime

from .media_item import MediaItem


@dataclass(kw_only=True)
class Magazine(MediaItem):
    issn: str
    publisher: str
    series: str
    pages: int | None = None
    format: str | None = None
    description: str | None = None
    condition: str | None = None
    finished_date: datetime | None = None
    tags: list[str] = field(default_factory=list)
