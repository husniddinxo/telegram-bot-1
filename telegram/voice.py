from .file import File


class Voice(File):
    def __init__(
        self,
        file_id: str,
        file_unique_id: str,
        duration: int
    ):
        super().__init__(file_id, file_unique_id)
        self.duration = duration

    def __str__(self):
        return f"{self.file_id} ({self.duration})"
