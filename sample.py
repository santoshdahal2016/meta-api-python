from meta.api.api import Api

from meta.api.consts import MessagingType, QuickReplyType, SenderAction, MediaType
from meta.api.messages.text_message import TextMessage
from meta.api.messages.action_message import Action
from meta.api.messages.media_message import MediaMessage
from meta.api.messages.quick_reply_message import QuickReplies, QuickReply
from meta.api.messages.generic_message import Element, Elements
from meta.api.messages.button_message import Button, Buttons, ButtonType


# Initiate Api
api = Api(
    page_access_token=""
)


# Action Message
action = Action(event=SenderAction.TYPING_ON)


# Text Message
text_message = TextMessage(
    text="Hi, How are you?", messaging_type=MessagingType.RESPONSE
)


# Media Message
media = MediaMessage(
    media_type=MediaType.IMAGE,
    media_url="https://www.pngall.com/wp-content/uploads/2016/05/Python-Logo-PNG-Image-180x180.png",
)


# Button Message
buttons = Buttons(text="Please Select below options")
web_link_button = Button(button_type=ButtonType.WEB_URL, title="Visit  Website")
web_link_button.set_url("https://diyo.ai")
phone_number_button = Button(button_type=ButtonType.PHONE_NUMBER, title="Call me")
phone_number_button.set_payload("XXXXXXXXX")
buttons.add_button(web_link_button)
buttons.add_button(phone_number_button)


# Generic Message
elements = Elements()
element1 = Element(
    buttons=[web_link_button],
    image_url="https://moneymitra.com/static/image/moneymitra-logo.png",
)
elements.add_element(element1)
element2 = Element(
    buttons=[phone_number_button],
    image_url="https://moneymitra.com/static/landing4/assets/images/home/idea-course-tulke.png",
)
elements.add_element(element2)


# Quick Reply
quick_replies = QuickReplies(text="Please provide your phone number ")
quick_replies.add_quick_reply(QuickReply(type=QuickReplyType.PHONE_NUMBER))



response = api.send_messages(to="6572996466068929", messages=[action, text_message, media, buttons, elements , quick_replies])

