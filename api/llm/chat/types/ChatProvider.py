# Base class for any provider of chat completions
import typing


@typing.Protocol
class ChatProvider:
    def __init__(self, provider_name: str):
        pass

    def get_completions(self, messages: typing.List[str]) -> typing.List[str]:
        pass
