class Dice:
    def __init__(self, value: str, emoji: str):
        self.value = value
        self.emoji = emoji

    def __str__(self):
        return f"{self.value} ({self.emoji})"
        