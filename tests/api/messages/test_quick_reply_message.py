from metapython.api.messages.quick_reply_message import QuickRepliesMessage, QuickReplyMessage , QuickReplyType
import pytest


QUICK_REPLY_TEXT = "Please select below options" 
QUICK_REPLY_TITLE = "Quick Reply 1"
QUICK_REPLY_PAYLOAD = "Payload"
QUICK_REPLY_IMAGE_URL = "https://"

def test_quick_replies_creation():
    quick_replies_message = QuickRepliesMessage(text=QUICK_REPLY_TEXT)
    assert quick_replies_message.text == QUICK_REPLY_TEXT




def test_quick_replies_creation_fails():
    with pytest.raises(ValueError,match="Text must not be empty"):
        QuickRepliesMessage("")



def test_quick_reply_creation():
    quick_reply_message = QuickReplyMessage(title=QUICK_REPLY_TITLE)
    assert quick_reply_message.get_title() == QUICK_REPLY_TITLE
    assert quick_reply_message.get_type() == QuickReplyType.TEXT


def test_quick_reply_creation_fails():

    with pytest.raises(ValueError,match="param type must be TEXT, PHONE_NUMBER, EMAIL"):
        QuickReplyMessage(quick_reply_type="unknown")

    with pytest.raises(ValueError,match=f"type of param title must be str , not {type(1)}"):
        QuickReplyMessage(title=1)

    with pytest.raises(ValueError,match="param title must be non empty"):
        QuickReplyMessage(title="")

    with pytest.raises(ValueError,match=f"type of param payload must be str , not {type(1)}"):
        QuickReplyMessage(payload=1)

    with pytest.raises(ValueError,match="param payload must be non empty"):
        QuickReplyMessage(payload="")

    with pytest.raises(ValueError,match="max character of param payload is 1000"):
        QuickReplyMessage(payload=" as da sd as d as d as d as d asd a sd as d as da sd a sd as d as d asd a sd as d as d asd a sd as d sad as d as d as das d as d as das d sa d asd as d as d asd as d as d as das d as d asd a sd as d asd as d as d asd as d asd as d as d asd as d as da sd as d as da sd as d asd as d as d asd  asd as d asd as d asd a sd as  asd as da sd as d as dsa,ndksjdnkjasdlkjasdljasldjlkasjdlkjasdlkjasldnas,mdnas,jnd,amsd as,md als d, asdl asld saljd klsa dl sadl aslkdj kasj dkas dk asdk ask dask d sd as d as da sd a sd as d as d asd a sd as d as d asd a sd as d sad as d as d as das d as d as das d sa d asd as d as d asd as d as d as das d as d asd a sd as d asd as d as d asd as d asd as d as d asd as d as da sd as d as da sd as d asd as d as d asd  asd as d asd as d asd a sd as  asd as da sd as d as dsa,ndksjdnkjasdlkjasdljasldjlkasjdlkjasdlkjasldnas,mdnas,jnd,amsd as,md als d, asdl asld sal sd as d as da sd a sd as d as d asd a sd as d as d asd a sd as d sad as d as d as das d as d as das d sa d asd as d as d asd as d as d as das d as d asd a sd as d asd as d as d asd as d asd as d as d asd as d as da sd as d as da sd as d asd as d as d asd  asd as d asd as d asd a sd as  asd as da sd as d as dsa,ndksjdnkjasdlkjasdljasldjlkasjdlkjasdlkjasldnas,mdnas,jnd,amsd as,md als d, asdl asld sal")

    with pytest.raises(ValueError,match=f"type of param payload must be str , not {type(1)}"):
        QuickReplyMessage(image_url=1)



def test_quick_reply_set_title():
    quick_reply_message = QuickReplyMessage(title=QUICK_REPLY_TITLE)

    quick_reply_message.set_title("change")
    assert quick_reply_message.get_title() == "change"


def test_quick_reply_set_image():
    quick_reply_message = QuickReplyMessage(title=QUICK_REPLY_TITLE)

    quick_reply_message.set_image_url(QUICK_REPLY_IMAGE_URL)
    assert quick_reply_message.get_image_url() ==  QUICK_REPLY_IMAGE_URL


def test_quick_reply_set_payload():
    quick_reply_message = QuickReplyMessage(title=QUICK_REPLY_TITLE)

    quick_reply_message.set_payload(QUICK_REPLY_PAYLOAD)
    assert quick_reply_message.get_payload() == QUICK_REPLY_PAYLOAD



def test_quick_reply_asdict():


    text_dict = dict(
		content_type="text",
		title=QUICK_REPLY_TITLE,
		payload=QUICK_REPLY_PAYLOAD
	)


    quick_reply_text_message = QuickReplyMessage(title=QUICK_REPLY_TITLE,payload=QUICK_REPLY_PAYLOAD)



    assert text_dict == quick_reply_text_message.asdict()



    text_with_image_dict = dict(
		content_type="text",
		title=QUICK_REPLY_TITLE,
		payload=QUICK_REPLY_PAYLOAD,
        image_url = QUICK_REPLY_IMAGE_URL
	)


    quick_reply_text_with_image_message = QuickReplyMessage(title=QUICK_REPLY_TITLE,payload=QUICK_REPLY_PAYLOAD, image_url=QUICK_REPLY_IMAGE_URL)



    assert text_with_image_dict == quick_reply_text_with_image_message.asdict()   


    phone_number_dict = dict(
		content_type = QuickReplyType.PHONE_NUMBER
	)


    quick_reply_phone_message = QuickReplyMessage(quick_reply_type=QuickReplyType.PHONE_NUMBER)



    assert phone_number_dict == quick_reply_phone_message.asdict()   




def test_quick_replies_asdict():
    quick_replies_message = QuickRepliesMessage(text=QUICK_REPLY_TEXT)

    message_dict = dict(
        message = dict(
                text = QUICK_REPLY_TEXT,
                quick_replies =  [
                    dict(
                        content_type="text",
                        title=QUICK_REPLY_TITLE,
                        payload=QUICK_REPLY_PAYLOAD
                    )
                ]
        )
	)


    quick_reply_text_message = QuickReplyMessage(title=QUICK_REPLY_TITLE,payload=QUICK_REPLY_PAYLOAD)


    quick_replies_message.add_quick_reply(quick_reply_text_message)


    assert message_dict == quick_replies_message.asdict()