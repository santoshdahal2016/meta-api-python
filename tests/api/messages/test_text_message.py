from meta.api.messages.text_message import TextMessage
from meta.api.consts import MessagingType, NotificationType

import pytest

TEXT_MESSAGE = "Hi"
MESSAGING_TYPE = MessagingType.RESPONSE
NOTICIFICATION_TYPE = NotificationType.REGULAR

def test_creation():
    text_message = TextMessage(text=TEXT_MESSAGE)

    assert text_message.text == TEXT_MESSAGE
    assert text_message.messaging_type == MESSAGING_TYPE
    assert text_message.notification_type == NOTICIFICATION_TYPE


def test_creation_text_empty():

    with pytest.raises(ValueError, match="Text must not be empty"):
        TextMessage(text=" ")

    with pytest.raises(ValueError, match="Text must not be empty"):
        TextMessage(text="\t\n  \t")