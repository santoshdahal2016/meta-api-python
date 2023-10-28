from metapython.api.messages.text_message import TextMessage
from metapython.api.consts import MessagingType, NotificationType

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


def test_asdict():
	message_dict = dict(
		notification_type=NOTICIFICATION_TYPE,
		messaging_type=MESSAGING_TYPE,
		message=dict(text=TEXT_MESSAGE)
	)

	text_message_dict = TextMessage(text=TEXT_MESSAGE).asdict()

	assert message_dict == text_message_dict
