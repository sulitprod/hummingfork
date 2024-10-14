import hashlib
import hmac
import json

from typing import Dict

from hummingbot.connector.time_synchronizer import TimeSynchronizer
from hummingbot.core.web_assistant.auth import AuthBase
from hummingbot.core.web_assistant.connections.data_types import RESTRequest, WSRequest
from hummingbot.core.utils.tracking_nonce import NonceCreator

class BitwyreAuth(AuthBase):
    def __init__(self, api_key: str, secret_key: str, time_provider: TimeSynchronizer):
        self.api_key = api_key
        self.secret_key = secret_key
        self.time_provider = time_provider

    async def rest_authenticate(self, request: RESTRequest) -> RESTRequest:
        headers = {}

        if request.headers is not None:
            headers.update(request.headers)

        headers.update(self._get_rest_headers(request))
        request.headers = headers

        return request
    
    async def ws_authenticate(self, request: WSRequest) -> WSRequest:
        request.headers = self._get_ws_headers(request)

        return request
    
    def _get_ws_headers(self):
        sign = hmac.new(
            self.secret_key.encode("utf-8"), "".encode("utf-8"), hashlib.sha512
        ).hexdigest()

        data = {
            "api_key": self.api_key, 
            "api_sign": sign
        }
        json_data = json.dumps(data)

        headers = {
            "API-Data": json_data
        }

        return headers

    def _get_rest_headers(self, request: RESTRequest) -> Dict[str, str]:
        sign = self._generate_sign(request)

        headers = {
            "API-Key": self.api_key,
            "API-Sign": sign,
            "Content-type": "application/json",
        }

        return headers
    
    def _generate_sign(self, request: RESTRequest) -> str:
        nonce = NonceCreator.for_microseconds()
        payload = json.dumps(request.payload)
        checksum = hashlib.sha256(str(payload).encode("utf-8")).hexdigest()
        nonce_checksum = hashlib.sha256(
            str(nonce).encode("utf-8") + str(checksum).encode("utf-8")
        ).hexdigest()
        message = request.url.encode("utf-8") + nonce_checksum.encode("utf-8")
        api_sign = hmac.new(
            self.secret_key.encode('utf-8'), 
            message, 
            hashlib.sha512
        ).hexdigest()

        return api_sign