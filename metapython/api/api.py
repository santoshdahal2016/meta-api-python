from dataclasses import dataclass



import requests
from metapython.api.message_sender import MessageSender
from metapython.api.api_request_sender import ApiRequestSender


@dataclass
class Api(object):
    """This is the main interface to call Meta Graph api


    Args:
        page_access_token (str): The pageaccess token generated using graph api explorer

    NOTES: Steps for interecting with graph api
    - Create API object with page access token 
    - Create desired message from facebook.api.messages
    - Call send_message with desired recepient_id

    """
    page_access_token: str
    request_sender: ApiRequestSender = None
    message_sender: MessageSender = None

    def __post_init__(self):
        if self.request_sender is None:
            self.request_sender = ApiRequestSender(self.page_access_token)
        if self.message_sender is None:
            self.message_sender = MessageSender(request_sender=self.request_sender)

    def send_messages(self, to, messages):
        """This function is used 

        Args:
            to (str): The recepient_id from the conversation on the respective page, This is not the facebook user id , Every page has different recepient_id for users.
            messages (Message): This is the object of classes from facebook.api.messages

        Returns:
            array : list of responses to be sent
        """
        if not isinstance(messages, list):
            messages = [messages]

        sent_messages_responses = []


        for message in messages:
            response = self.message_sender.send_message(to=to, message=message)
            sent_messages_responses.append(response)
        
        return sent_messages_responses
  


