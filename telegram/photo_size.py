from .file import File


class PhotoSize(File):
    def __init__(
        self,
        file_id: str,
        file_unique_id: str,
        width: int,
        height: int,
        file_size: int = None
    ):
        super().__init__(file_id, file_unique_id)
        self.width = width
        self.height = height
        self.file_size = file_size

    def __str__(self):
        return f"{self.file_id} ({self.width}x{self.height})"