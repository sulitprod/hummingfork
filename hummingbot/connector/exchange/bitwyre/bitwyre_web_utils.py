from typing import Callable, Optional

from dateutil.parser import parse as dateparse

import hummingbot.connector.exchange.bitwyre.bitwyre_constants as CONSTANTS
from hummingbot.connector.time_synchronizer import TimeSynchronizer
from hummingbot.connector.utils import TimeSynchronizerRESTPreProcessor
from hummingbot.core.api_throttler.async_throttler import AsyncThrottler
from hummingbot.core.web_assistant.auth import AuthBase
from hummingbot.core.web_assistant.connections.data_types import RESTMethod
from hummingbot.core.web_assistant.web_assistants_factory import WebAssistantsFactory


def full_url(path_url: str, is_public: bool) -> str:
    """
    Create a URL for provided public REST endpoint

    :param path_url: a public REST endpoint
    :param is_public: a access endpoint type

    :return: the full URL to the endpoint
    """

    access_type = 'public' if is_public else 'private'

    return CONSTANTS.URL_REST + access_type + '/' + path_url


def public_rest_url(path_url: str) -> str:
    return full_url(path_url)


def private_rest_url(path_url: str) -> str:
    return full_url(path_url, False)


def get_path_from_url(url: str) -> str:
    return url.replace(CONSTANTS.URL_REST, '')


def build_api_factory(
    throttler: Optional[AsyncThrottler] = None,
    time_synchronizer: Optional[TimeSynchronizer] = None,
    time_provider: Optional[Callable] = None,
    auth: Optional[AuthBase] = None
) -> WebAssistantsFactory:
    throttler = throttler or create_throttler()
    time_synchronizer = time_synchronizer or TimeSynchronizer()
    time_provider = time_provider or (lambda: get_current_server_time(throttler=throttler))

    api_factory = WebAssistantsFactory(
        throttler=throttler,
        auth=auth,
        rest_pre_processors=[
            TimeSynchronizerRESTPreProcessor(synchronizer=time_synchronizer, time_provider=time_provider),
        ])

    return api_factory


def build_api_factory_without_time_synchronizer_pre_processor(throttler: AsyncThrottler) -> WebAssistantsFactory:
    api_factory = WebAssistantsFactory(throttler=throttler)

    return api_factory


def create_throttler() -> AsyncThrottler:
    return AsyncThrottler(CONSTANTS.RATE_LIMITS)


async def get_current_server_time(
        throttler: Optional[AsyncThrottler] = None,
) -> float:
    throttler = throttler or create_throttler()
    api_factory = build_api_factory_without_time_synchronizer_pre_processor(throttler=throttler)
    rest_assistant = await api_factory.get_rest_assistant()
    response = await rest_assistant.execute_request(
        url=public_rest_url(path_url=CONSTANTS.PATH_SERVER_TIME),
        method=RESTMethod.GET,
        throttler_limit_id=CONSTANTS.PATH_SERVER_TIME,
    )
    server_time = float(dateparse(response["result"]["unixtime"]).timestamp())

    return server_time * 1e3
