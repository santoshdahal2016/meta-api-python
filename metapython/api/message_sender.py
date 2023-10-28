from metapython.api.messages.message import Message

from .consts import API_URL, APIEndpoint

class MessageSender(object):
    
    def __init__(self, request_sender):
        self._request_sender = request_sender
    
    def send_message(self, to, message: Message):
        payload = self.prepare_payload(message=message, recipient=to)
        return self._request_sender.post_request(
                payload=payload, endpoint=API_URL + APIEndpoint.MESSAGES
            )

    def prepare_payload(self, message, recipient):
        payload = message.asdict()
        payload.update({"recipient": {"id": recipient}})

        return self.remove_empty_fields(payload)

    def remove_empty_fields(self, message):
        return {k: v for k, v in message.items() if v is not None}
