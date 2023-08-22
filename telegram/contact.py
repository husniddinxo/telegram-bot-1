class Contact:
    def __init__(
        self,
        phone_number: str,
        first_name: str,
        last_name: str=None,
    ):

        self.phone_number = phone_number
        self.first_name   = first_name
        self.last_name    = last_name

    def __str__(self):
        if self.last_name is None:
            return f"{self.first_name} ({self.phone_number})"
        else:
            return f"{self.first_name} {self.last_name} ({self.phone_number})"
    