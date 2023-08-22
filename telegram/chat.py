class Chat:
    def __init__(
        self, 
        id: int,
        type: str,
        title: str=None,
        username: str=None,
        first_name: str=None,
        last_name: str=None
    ):
        self.id         = id
        self.type       = type
        self.title      = title
        self.username   = username
        self.first_name = first_name
        self.last_name  = last_name

    def __str__(self):
        if self.type == "private":
            return f"{self.first_name} {self.last_name} ({self.username})"
        else:
            return f"{self.title} ({self.username})"

    @property
    def full_name(self):
        if self.type == "private":
            if self.last_name is None:
                return f"{self.first_name}"
            else:
                return f"{self.first_name} {self.last_name}"
        else:
            return f"{self.title}"
        