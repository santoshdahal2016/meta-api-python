from metapython.api.messages.message import Message
from abc import abstractmethod
from dataclasses import dataclass, asdict


@dataclass
class TextMessage(Message):
    """This reprsent text message
    Args:
        text (str): The message to be send.

    """
    text: str = ""

    def __post_init__(self):
        if not self.text.strip():
            raise ValueError("Text must not be empty")


    def asdict(self):
        parent_dict = super().asdict()
        parent_dict.update({"message": {"text": self.text}})
        return parent_dict
