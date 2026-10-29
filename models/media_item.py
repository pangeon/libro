class MediaItem:
    id: int
    title: str
    publication_year: int
    category: str
    language: str

    @staticmethod
    def next_id(collection):
        return max((item["id"] for item in collection), default=0) + 1