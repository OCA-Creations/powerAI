import datetime


class ChatMessage:
    def __init__(self, message, author, timestamp: datetime.datetime):
        self.message = message
        self.author = author
        self.timestamp = timestamp

    def to_dict(self):
        return {
            "message": self.message,
            "author": self.author,
            "timestamp": self.timestamp.strftime("%Y-%m-%d %H:%M:%S"),
        }
    toJSON = to_dict