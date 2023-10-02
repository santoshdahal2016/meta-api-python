from meta.api.messages.quick_reply_message import QuickReplies, QuickReply , QuickReplyType
import pytest


QUICK_REPLY_TEXT = "Please select below options" 
QUICK_REPLY_TITLE = "Quick Reply 1"
QUICK_REPLY_PAYLOAD = "Payload"
QUICK_REPLY_IMAGE_URL = "https://"

def test_quick_replies_creation():
    quick_replies_message = QuickReplies(text=QUICK_REPLY_TEXT)
    assert quick_replies_message.text == QUICK_REPLY_TEXT



def test_quick_replies_creation_fails():
    with pytest.raises(ValueError,match="Text must not be empty"):
        QuickReplies("")



def test_quick_reply_creation():
    quick_reply_message = QuickReply(title=QUICK_REPLY_TITLE)
    assert quick_reply_message.get_title() == QUICK_REPLY_TITLE


def test_quick_reply_creation_fails():

    with pytest.raises(ValueError,match="param type must be TEXT, PHONE_NUMBER, EMAIL"):
        QuickReply(quick_reply_type="unknown")

    with pytest.raises(ValueError,match=f"type of param title must be str , not {type(1)}"):
        QuickReply(title=1)

    with pytest.raises(ValueError,match="param title must be non empty"):
        QuickReply(title="")

    with pytest.raises(ValueError,match=f"type of param payload must be str , not {type(1)}"):
        QuickReply(payload=1)

    with pytest.raises(ValueError,match="param payload must be non empty"):
        QuickReply(payload="")