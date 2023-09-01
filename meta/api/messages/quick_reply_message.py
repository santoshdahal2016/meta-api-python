class QuickReplies:
    """A list of QuickReply objects.

    Attributes:
        quick_replies (str , private) : A list containing the content of each QuickReply object.

    Notes:
        Use the add_quick_reply() method to add an QuickReply object's content.
        Use the asdict() method to get the content of the QuickReplies object before using it.

        The maximum of quick replies is 13 , sending more than 13 quick replies will return an error message from Facebook API's server.
    """

    def __init__(self, text):
        assert text != "", "param text must be non empty"

        self.text = text
        self.__quick_replies = []

    def add_quick_reply(self, quick_reply):
        self.__quick_replies.append(quick_reply.asdict())

    def asdict(self):
        return {"message": {"text": self.text, "quick_replies": self.__quick_replies}}


class QuickReply:
    def __init__(
        self,
        title="Quick reply",
        payload="<DEVELOPER_DEFINED_PAYLOAD>",
        image_url=None,
        type="text",
    ):
        """Represent a quick reply , used for a quick reply message.

        Args:
            title (str, optional): The title of the quick reply. Defaults to "Quick reply".
            payload (str, optional): The payload of this quick reply. Defaults to "<DEVELOPER_DEFINED_PAYLOAD>".
            image_url ([type], optional): The image url to show beside the quick reply. Defaults to None.

        Notes:
            param title must be non-empty.
            param payload must be non-empty.
            Max characters in the param payload is 1000.
            Recommended resolution for the image in param image_url is 24x24.
            Use the asdict() method to get the content of the QuickReply object before using it.
        """
        assert isinstance(
            title, str
        ), f"type of param title must be str , not {type(title)}"
        assert title != "", "param title must be non empty"
        assert isinstance(
            payload, str
        ), f"type of param payload must be str , not {type(payload)}"
        assert payload != "", "param payload must be non empty"
        assert len(str(payload)) < 1000, "max character of param payload is 1000"

        self.__title = title
        self.__payload = payload
        self.__image_url = image_url
        self.__type = type

        if len(title) > 20:
            print(
                "WARNING : max characters for param title is 20 , your title won't show entirely"
            )

    def set_title(self, title):
        assert isinstance(
            title, str
        ), f"type of param title must be str , not {type(title)}"
        assert title != "", "param title must be non empty"
        if len(title) > 20:
            print(
                "WARNING : max characters for param title is 20 , your title won't show entirely"
            )

        self.__title = title

    def set_payload(self, payload):
        assert isinstance(
            payload, str
        ), f"type of param payload must be str , not {type(payload)}"
        assert payload != "", "param payload must be non empty"
        assert len(str(payload)) < 1000, "max character of param payload is 1000"

        self.__payload = str(payload)

    def set_image_url(self, image_url):
        assert isinstance(
            image_url, str
        ), f"type of param image_url must be str , not {type(image_url)}"

        self.__image_url = image_url

    def asdict(self):
        """Return the content of the QuickReply object.

        Returns:
            dict: The content of the QuickReply object.
        """

        if self.__type == "text":
            if self.__image_url == None:
                return {
                    "content_type": "text",
                    "title": self.__title,
                    "payload": self.__payload,
                }
            return {
                "content_type": "text",
                "title": self.__title,
                "payload": self.__payload,
                "image_url": self.__image_url,
            }
        else:
            return {"content_type": self.__type}
