from metapython.api.messages.generic_message import ElementMessage, ElementsMessage
from metapython.api.messages.button_message import ButtonMessage, ButtonType

import pytest

ELEMENT_TITLE = "Element Title"
ELEMENT_IMAGE_URL = "https://"
ELEMENT_SUB_TITLE = "This is subtitle"
BUTTON_TITLE = "Visit  Website"
BUTTON_URL = "https://"


web_link_button = ButtonMessage(button_type=ButtonType.WEB_URL, title=BUTTON_TITLE)
web_link_button.set_url(BUTTON_URL)  


element = ElementMessage(
    buttons=[web_link_button],
    image_url=ELEMENT_IMAGE_URL,
    title=ELEMENT_TITLE,
    subtitle=ELEMENT_SUB_TITLE
)


def test_generic_element_asdict():

    element_dict = dict(
		subtitle=ELEMENT_SUB_TITLE,
        image_url=ELEMENT_IMAGE_URL,
		title=ELEMENT_TITLE,
        buttons=[dict(
            title= BUTTON_TITLE,
            type= ButtonType.WEB_URL,
            url =BUTTON_URL
        )]
	)




    assert element_dict == element.asdict()



def test_generic_element_set_title():
    with pytest.raises(ValueError, match="param title must be non empty"):
        element.set_title(" ")

    with pytest.raises(ValueError, match=f"type of param title must be str , not {type(1)}"):
        element.set_title(1)


def test_generic_element_set_subtitle():

    with pytest.raises(ValueError, match=f"type of param subtitle must be str , not {type(1)}"):
        element.set_subtitle(1)


def test_generic_element_set_image_url():
    with pytest.raises(ValueError, match="param image_url must be non empty"):
        element.set_image_url(" ")

    with pytest.raises(ValueError, match=f"type of param image_url must be str , not {type(1)}"):
        element.set_image_url(1)


def test_generic_elements_asdict():

    element_dict = dict(
        message = dict(
            attachment = dict(
                type ="template",
                payload = dict(
                    template_type = "generic",
                    elements = [
                        dict(
                            subtitle=ELEMENT_SUB_TITLE,
                            image_url=ELEMENT_IMAGE_URL,
                            title=ELEMENT_TITLE,
                            buttons=[dict(
                                title= BUTTON_TITLE,
                                type= ButtonType.WEB_URL,
                                url =BUTTON_URL
                            )])
                    ]

                )
                
            )
            
        )
		
	)

    elements = ElementsMessage(elements=[element])




    assert element_dict == elements.asdict()