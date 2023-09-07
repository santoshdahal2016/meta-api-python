from meta.api.messages.button_message import Buttons, Button, ButtonType
import pytest


BUTTONS_TEXT = "Please select below options" 
BUTTON_TITLE = "Button 1"
BUTTON_PAYLOAD = "Payload"
BUTTON_URL = "https://"

def test_buttons_creation():
    buttons_message = Buttons(text=BUTTONS_TEXT)
    assert buttons_message.text == BUTTONS_TEXT



def test_buttons_creation_fails():
    with pytest.raises(ValueError,match="Text must not be empty"):
        Buttons("")



def test_button_creation():
    button_message = Button(title=BUTTON_TITLE)
    assert button_message.title == BUTTON_TITLE


def test_button_creation_fails():

    with pytest.raises(ValueError,match="param type must be POSTBACK, WEB_URL, BOOKING  or PHONE_NUMBER"):
        Button(button_type="unknown")

    with pytest.raises(ValueError,match=f"type of param title must be str , not {type(1)}"):
        Button(title=1)

    with pytest.raises(ValueError,match="param title must be non empty"):
        Button(title="")

def test_set_payload_button():
    button_message = Button()
    button_message.set_payload(BUTTON_PAYLOAD)

    assert button_message.get_payload() == BUTTON_PAYLOAD

def test_set_payload_button_invalid_type():
    button_message = Button(button_type=ButtonType.BOOKING)


    with pytest.raises(ValueError, match="param payload is only supported on postback and phone_number buttons"):
        button_message.set_payload(BUTTON_PAYLOAD)


    with pytest.raises(ValueError, match=f"type of param payload must be str , not {type(1)}"):
        button_message = Button(button_type=ButtonType.POSTBACK)
        button_message.set_payload(1)


def test_set_url_button():
    button_message = Button(button_type=ButtonType.WEB_URL)
    button_message.set_url(BUTTON_PAYLOAD)

    assert button_message.get_url() == BUTTON_PAYLOAD


def test_set_url_button_fails():
    button_message = Button(button_type=ButtonType.WEB_URL)
    with pytest.raises(ValueError,match=f"type of param url must be str , not {type(1)}"):
        button_message.set_url(1)


def test_set_url_button_invalid_type():
    button_message = Button()


    with pytest.raises(ValueError, match="param url is only supported on web_url buttons"):
        button_message.set_url(BUTTON_PAYLOAD)



def test_button_asdict():

    message_dict = dict(
		type=ButtonType.POSTBACK,
		title=BUTTON_TITLE,
		payload=BUTTON_PAYLOAD
	)


    button_message = Button(title=BUTTON_TITLE)


    button_message.set_payload(BUTTON_PAYLOAD)

    assert message_dict == button_message.asdict()



    message_booking_dict = dict(
		type=ButtonType.BOOKING
	)


    button_booking_message = Button(button_type=ButtonType.BOOKING)

    assert message_booking_dict == button_booking_message.asdict()


    message_booking_dict = dict(
		type=ButtonType.BOOKING
	)


    button_booking_message = Button(button_type=ButtonType.BOOKING)

    assert message_booking_dict == button_booking_message.asdict()


    message_link_dict = dict(
		type=ButtonType.WEB_URL,
        title=BUTTON_TITLE,
        url=BUTTON_URL
	)


    button_url_message = Button(button_type=ButtonType.WEB_URL,title=BUTTON_TITLE)

    button_url_message.set_url(BUTTON_URL)



    assert message_link_dict == button_url_message.asdict()