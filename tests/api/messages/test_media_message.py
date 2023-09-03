from meta.api.messages.media_message import MediaMessage

from meta.api.consts import MediaType, MessagingType, NotificationType

import pytest


MEDIA_URL = "https://images.unsplash.com"
MESSAGING_TYPE = MessagingType.RESPONSE
NOTICIFICATION_TYPE = NotificationType.REGULAR
MEDIA_TYPE = MediaType.IMAGE

def test_media_message_creation():

    media_message = MediaMessage(media_type=MediaType.IMAGE,media_url=MEDIA_URL)

    assert media_message.messaging_type == MESSAGING_TYPE
    assert media_message.notification_type == NOTICIFICATION_TYPE
    assert media_message.media_url == MEDIA_URL
    assert media_message.media_type == MEDIA_TYPE


def test_media_message_invalid():
    
    with pytest.raises(ValueError, match="Media Url must not be empty"):
        MediaMessage(media_type=MediaType.IMAGE)
    with pytest.raises(ValueError, match="value of param media_type must be 'image','video','audio' or 'file'"):
        MediaMessage(media_type="xyz",media_url=MEDIA_URL)
    with pytest.raises(ValueError, match="value of param media_type must be 'image','video','audio' or 'file'"):
        MediaMessage(media_url=MEDIA_URL)


def test_asdict():
	message_dict = dict(
		notification_type=NOTICIFICATION_TYPE,
		messaging_type=MESSAGING_TYPE,
		message=dict(attachment=dict(
            type=MediaType.IMAGE,
            payload=dict(
                url=MEDIA_URL,
                is_reusable="false"
            )
        ))
	)

	media_message_dict = MediaMessage(media_type=MediaType.IMAGE,media_url=MEDIA_URL).asdict()

	assert message_dict == media_message_dict
