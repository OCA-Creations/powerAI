import typing
import datetime

from api.llm.chat.types.ChatMessage import ChatMessage


class ChatConversation:
    def __init__(self, messages: typing.List[ChatMessage]):
        """Create a ChatConversation object from a list of messages.
        :param messages: A list of ChatMessage objects
        """
        self.messages = messages

    def _add_message(self, message: ChatMessage):
        """Add a message to the conversation
        :param message: A ChatMessage object
        """
        self.messages.append(message)

    def add_message(self, role: str, message: str, timestamp: datetime.datetime = datetime.datetime.now()):
        """Add a message to the conversation
        :param role: The role of the message author
        :param message: The message content
        :param timestamp: The timestamp of the message (default: datetime.datetime.now())
        """
        self._add_message(ChatMessage(message, role, timestamp))

    def to_dict(self):
        """Convert the ChatConversation object to a dictionary, for JSON serialization or similar.
        :return: A dictionary representation of the ChatConversation object
        """
        return {
            "messages": [message.to_dict() for message in self.messages]
        }

    toJSON = to_dict
