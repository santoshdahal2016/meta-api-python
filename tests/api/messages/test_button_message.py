from meta.api.messages.button_message import Buttons, Button, ButtonType
import pytest


BUTTONS_TEXT = "Please select below options" 
BUTTON_TITLE = "Button 1"
BUTTON_PAYLOAD = "Payload"

def test_buttons_creation():
    buttons_message = Buttons(text=BUTTONS_TEXT)
    assert buttons_message.text == BUTTONS_TEXT



def test_button_creation():
    button_message = Button(title=BUTTON_TITLE)
    assert button_message.title == BUTTON_TITLE


def test_set_payload_button():
    button_message = Button()
    button_message.set_payload(BUTTON_PAYLOAD)

    assert button_message.get_payload() == BUTTON_PAYLOAD

def test_set_payload_button_invalid_type():
    button_message = Button(button_type=ButtonType.BOOKING)


    with pytest.raises(ValueError, match="param payload is only supported on postback and phone_number buttons"):
        button_message.set_payload(BUTTON_PAYLOAD)


def test_set_url_button():
    button_message = Button(button_type=ButtonType.WEB_URL)
    button_message.set_url(BUTTON_PAYLOAD)

    assert button_message.get_url() == BUTTON_PAYLOAD

def test_set_url_button_invalid_type():
    button_message = Button()


    with pytest.raises(ValueError, match="param url is only supported on web_url buttons"):
        button_message.set_url(BUTTON_PAYLOAD)

