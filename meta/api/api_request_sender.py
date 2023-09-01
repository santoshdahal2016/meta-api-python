import requests
from requests import RequestException
import traceback
from meta.api.consts import API_URL, APIEndpoint
import json
from dataclasses import dataclass
import logging


@dataclass
class ApiRequestSender(object):
    page_access_token: str
    _logger = logging.getLogger("facebook.bot.api")

    def post_request(self, endpoint, payload):
        try:
            response = requests.post(
                endpoint, params={"access_token": self.page_access_token}, json=payload
            )
            response.raise_for_status()
            return json.loads(response.text)
        except RequestException as e:
            self._logger.error(
                "failed to post request to endpoint={0}, with payload={1}. error is: {2} \n".format(
                    endpoint, payload, response.content
                )
            )
            # raise e
        except Exception as ex:
            # pass
            self._logger.error(
                "unexpected Exception while trying to post request. error is: {0} \n".format(
                    traceback.format_exc()
                )
            )
            # raise ex
