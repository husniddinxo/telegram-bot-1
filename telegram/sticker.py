from .file import File


class Sticker(File):
    def __init__(
        slef,
        file_id: str,
        file_unique_id: str,
        type: str,
        width: int,
        height: int
    ):
        super().__init__(file_id, file_unique_id)
        self.type = type
        self.width = width
        self.height = height

    def __str__(self):
        return f"{self.file_id} ({self.width}x{self.height})"