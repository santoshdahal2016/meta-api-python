from meta.api.messages.generic_message import Element, Elements
from meta.api.messages.button_message import Button, ButtonType
import pytest




ELEMENT_TITLE = "Element Title"
ELEMENT_IMAGE_URL = "https://"
ELEMENT_SUB_TITLE = "This is subtitle"


BUTTON_TITLE = "Visit  Website"
BUTTON_URL = "https://"


web_link_button = Button(button_type=ButtonType.WEB_URL, title=BUTTON_TITLE)
web_link_button.set_url(BUTTON_URL)  

def element_asdict():


    element_dict = dict(
		subtitle="text",
        image_url="",
		title=ELEMENT_TITLE,
        buttons=[dict(
            title= BUTTON_TITLE,
            type= ButtonType.WEB_URL,
            url =BUTTON_URL
        )]
	)


    element = Element(
        buttons=[web_link_button],
        image_url=ELEMENT_IMAGE_URL,
        title=ELEMENT_TITLE,
        subtitle=ELEMENT_SUB_TITLE
    )


    assert element_dict == element.asdict()

