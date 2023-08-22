class File:
    def __init__(
        self, 
        file_id: str,
        file_unique_id: str
    ):

        self.file_id = file_id
        self.file_unique_id = file_unique_id
    
    def __str__(self):
        return f"{self.file_id}"