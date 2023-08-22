from .message import Message


class Update:
    def __init__(
        self,
        update_id: int,
        message: Message=None,
    ):
        self.update_id = update_id
        self.message = message

    def __str__(self):
        return f"Update {self.update_id} with {self.message}"