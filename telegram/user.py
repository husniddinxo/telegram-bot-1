class User:
    def __init__(self, id: int, is_bot: bool, first_name: str, last_name: str=None, username: str=None):
        self.id         = id
        self.is_bot     = is_bot
        self.first_name = first_name
        self.last_name  = last_name
        self.username   = username

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.username})"

    @property
    def full_name(self):
        if self.last_name is None:
            return f"{self.first_name}"
        else:
            return f"{self.first_name} {self.last_name}"
