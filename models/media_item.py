class MediaItem:
    id: int
    title: str
    publication_year: int
    category: str
    language: str

    @staticmethod
    def next_id(collection):
        if collection is None:
            return 1
        else:
            return max((item["id"] for item in collection), default=0) + 1