# meta_api_python

Python Wrapper to various APIs from [Meta Platform](https://developers.facebook.com/docs/messenger-platform).

## Features

### Send API (v16.0)
 - Send text messages
 - Send Media from a remote file (image, audio, video, file)
 - Send Action 
 - Send quick replies
 - Send buttons
 - Send Generic Messages



## Prerequisite
- **Python 3.7+** installed
- You'll need to setup a [Meta App](https://developers.facebook.com/apps/), Facebook Page, get the Page Access Token and link the App to the Page.

## How to install
### From GitHub
```bash
pip install git+https://github.com/santoshdahal2016/meta-api-python.git
```
### From Pypi
Package from Pypi.org may not be the latest one, if you want the latest version of this package, install it from the GitHub repository (see above)
```bash
pip install meta-api-python
```


## Usage
### Send API
```python
from meta.api.api import Api
from meta.api.messages.text_message import TextMessage



api = Api(page_access_token=<page_access_token>)

text_message = TextMessage(text="Hi, How are you?")
response = api.send_messages(to= <recipient_id>, messages=text_message)

```
**Note**: From Facebook regarding Receipt  IDs

> These ids are page-scoped. These ids differ from those returned from Meta Login apps which are app-scoped. You must use ids retrieved from a Messenger integration for this page in order to function properly.


##### Sending a generic template message:

> [Generic Template Messages](https://developers.facebook.com/docs/messenger-platform/implementation#receive_message) allows you to add cool elements like images, text all in a single bubble.

```python
from metapython import Api

from metapython.api.consts import ButtonType
from metapython.api.messages import ElementMessage, ElementsMessage, ButtonMessage, ButtonsMessage


api = Api(page_access_token=<page_access_token>)

# Generic Message
elements = ElementsMessage()

web_link_button = ButtonMessage(button_type=ButtonType.WEB_URL, title="Visit Diyo Website")
web_link_button.set_url(<url>)

element1 = ElementMessage(
    buttons=[web_link_button],
    image_url="https://moneymitra.com/static/image/moneymitra-logo.png",
)
elements.add_element(element1)

phone_number_button = ButtonMessage(button_type=ButtonType.PHONE_NUMBER, title="Call me")
phone_number_button.set_payload("XXXXXXXXXXX")
element2 = ElementMessage(
    buttons=[phone_number_button],
    image_url=<image_url>,
)
elements.add_element(element2)

response = api.send_messages(to= <recipient_id>, messages=elements)
```
