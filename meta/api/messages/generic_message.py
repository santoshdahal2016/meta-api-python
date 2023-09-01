class Elements:
    """A list of Element objects.

    Attributes:
        elements (str , private) : A list containing the content of each Element object.

    Notes:
        Use the add_element() method to add an Element object's content.
        Use the asdict() method to get the content of the Elements object before using it in an generic message.

        The maximum of elements is 10 , sending generic message with more than 10 elements will return an error message from Facebook API's server.
    """

    def __init__(self, image_aspect_ratio: str = "horizontal"):
        self.__elements = []
        self.__image_aspect_ratio = image_aspect_ratio

    def add_element(self, element):
        self.__elements.append(element.asdict())

    def asdict(self):
        return {
            "message": {
                "attachment": {
                    "type": "template",
                    "payload": {
                        "template_type": "generic",
                        "image_aspect_ratio": self.__image_aspect_ratio,
                        "elements": self.__elements,
                    },
                }
            }
        }


class Element:
    def __init__(
        self,
        title="An element of a generic message.",
        subtitle=None,
        image_url=None,
        buttons=None,
    ):
        """Represent one element (block , card) of a generic message

        Args:
            title (str, optional): The title of the element , use set_title() method to change its default value. Defaults to "An element of a generic message.".
            subtitle (str, optional): The subtitle of the element , use set_subtitle() method to change its default value. Defaults to None.
            image_url (str, optional): The url of the image to show in the element , use set_image_url() method to change its default value. Defaults to None.
            buttons (list, optional): List of the buttons in the element , max supported is 3(?). Defaults to an empty list.

        Notes:
            param image_url and buttons must be non-empty.
            Use the asdict() method to get the content of the Element object before using it in an generic message or an Elements object.
        """
        assert isinstance(
            title, str
        ), f"type of param title must be str , not {type(title)}"
        assert title != "", "param title must be non empty"

        self.__title = title
        self.__subtitle = subtitle
        self.__image_url = image_url
        self.__buttons = (
            [item.asdict() for item in buttons] if buttons is not None else []
        )

        if self.__image_url == None or len(self.__buttons) == 0:
            print("WARNING : param image_url and buttons must be non-empty.")

    def set_title(self, title):
        assert isinstance(
            title, str
        ), f"type of param title must be str , not {type(title)}"
        assert title != "", "param title must be non empty"

        self.__title = title

    def set_subtitle(self, subtitle):
        assert isinstance(
            subtitle, str
        ), f"type of param subtitle must be str , not {type(subtitle)}"
        self.__subtitle = subtitle

    def set_image_url(self, image_url):
        assert isinstance(
            image_url, str
        ), f"type of param image_url must be str , not {type(image_url)}"

        self.__image_url = image_url

    def add_button(self, button):
        self.__buttons.append(button.asdict())

    def asdict(self):
        """Return the content of the Element object.

        Returns:
            dict: The content of the Element object.
        """
        if self.__subtitle == None:
            return {
                "title": self.__title,
                "image_url": self.__image_url,
                "buttons": self.__buttons,
            }
        return {
            "title": self.__title,
            "subtitle": self.__subtitle,
            "image_url": self.__image_url,
            "buttons": self.__buttons,
        }
