from meta.api.messages.message import Message
from abc import abstractmethod
from dataclasses import dataclass, asdict


@dataclass
class MediaMessage(Message):
    """Represet media message i.e image, video, audio, file

    Args:
        media_type (str): The type of media. Supported values are image, video, audio, file
        media_url   (str): The url of media.
        is_resuable (str, optional): If set true, this enable the asset to be used in multiple message.

    """

    media_type: str = ""
    media_url: str = ""
    is_reusable: str = "false"

    def __post_init__(self):
        self.validate_media_type(self.media_type)
        self.validate_media_url(self.media_url)

    def validate_media_type(self, media_type):
        if not media_type.strip():
            raise ValueError("Media Type must not be empty")
        assert media_type in (
            "image",
            "video",
            "audio",
            "file",
        ), 'value of param media_type must be "image","video","audio" or "file"'

    def validate_media_url(self, media_url):
        if not media_url.strip():
            raise ValueError("Media Url must not be empty")

    def asdict(self):
        parent_dict = super().asdict()
        parent_dict.update(
            {
                "message": {
                    "attachment": {
                        "type": self.media_type,
                        "payload": {
                            "url": self.media_url,
                            "is_reusable": self.is_reusable,
                        },
                    }
                }
            }
        )
        return parent_dict
