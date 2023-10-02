from meta.api.consts import ButtonType


class Buttons:
    """A list of Button objects.

    Attributes:
        buttons (str , private) : A list containing the content of each Button object.

    Notes:
        Use the add_button() method to add an Button object's content.
        Use the asdict() method to get the content of the Buttons object before using it in an generic message.

        The maximum of buttons is 3 (in a element), sending generic message with more than 3 buttons will return an error message from Facebook API's server.
    """

    def __init__(self, text):
        if  not text.strip():
            raise ValueError("Text must not be empty")

        self.text = text
        self.__buttons = []

    def add_button(self, element):
        self.__buttons.append(element.asdict())

    def asdict(self):
        return {
            "message": {
                "attachment": {
                    "type": "template",
                    "payload": {
                        "template_type": "button",
                        "text": self.text,
                        "buttons": self.__buttons,
                    },
                }
            }
        }


class Button:
    def __init__(self, button_type=ButtonType.POSTBACK, title="Button"):
        """Represent a button , used for generic message , persistent menu , ...

        Args:
            button_type (str, optional): The type of the button. Supported values are POSTBACK and WEB_URL. Defaults to POSTBACK.
            title (str, optional): The title of the button. Defaults to "Button".

        Notes:
            param title must be non-empty.
            If the button is a postback button , use set_payload() method to change the default value.
            If the button is a web_url button , use set_url() method to change the default value.
            Use the asdict() method to get the content of the Button object before using it.
        """
        if  button_type not  in (
            ButtonType.POSTBACK,
            ButtonType.WEB_URL,
            ButtonType.PHONE_NUMBER,
            ButtonType.BOOKING,
        ):
            raise ValueError("param type must be POSTBACK, WEB_URL, BOOKING  or PHONE_NUMBER")

        if not  isinstance(title, str):
            raise ValueError(f"type of param title must be str , not {type(title)}")

        if not title.strip():
            raise ValueError("param title must be non empty")

        self.__type = button_type
        self.__title = title

        if self.__type == ButtonType.POSTBACK:
            self.__payload = "<DEVELOPER_DEFINED_PAYLOAD>"
        elif self.__type == ButtonType.WEB_URL:
            self.__url = "<DEVELOPER_DEFINED_URL>"


    def set_payload(self, payload):
        if  self.__type not in (
            ButtonType.POSTBACK,
            ButtonType.PHONE_NUMBER,
        ):
            raise ValueError("param payload is only supported on postback and phone_number buttons")
        
        if not isinstance(
            payload, str
        ):
            raise ValueError(f"type of param payload must be str , not {type(payload)}")

        self.__payload = payload
    
    def get_payload(self):
        return self.__payload

    def set_url(self, url):
        if  self.__type != ButtonType.WEB_URL:
            raise ValueError("param url is only supported on web_url buttons")

        if not isinstance(url, str):
            raise ValueError(f"type of param url must be str , not {type(url)}")

        self.__url = url


    def get_url(self):
        return self.__url

    def get_title(self):
        return self.__title

    def asdict(self):
        """Return the content of the Button object.

        Returns:
            dict: The content of the Button object.
        """
        if self.__type == ButtonType.POSTBACK or self.__type == ButtonType.PHONE_NUMBER:
            return {
                "type": self.__type,
                "title": self.__title,
                "payload": self.__payload,
            }
        elif self.__type == ButtonType.BOOKING:
            return {"type": self.__type}
        else:
            return {"type": self.__type, "title": self.__title, "url": self.__url}
