from .file import File


class Document(File):
    def __init__(
        self,
        file_id: str,
        file_unique_id: str,
        file_name: str,
    ):
        super().__init__(file_id, file_unique_id)
        self.file_name = file_name

    def __str__(self):
        return f"{self.file_id} ({self.file_name})"