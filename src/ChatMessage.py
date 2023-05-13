import datetime


class ChatMessage:
    def __init__(self, author: str, time: datetime, content: str):
        self.author = author
        self.time = time
        self.content = content

    def __str__(self):
        return f'{self.author if self.author else "Whatsapp"} ({self.time}): {self.content}\n'
