from decimal import Decimal

from pydantic import Field, SecretStr

from hummingbot.client.config.config_data_types import BaseConnectorConfigMap, ClientFieldData
from hummingbot.connector.exchange.bitwyre_draft import bitwyre_constants as CONSTANTS
from hummingbot.core.data_type.trade_fee import TradeFeeSchema

CENTRALIZED = True
EXAMPLE_INSTRUMENT_PAIR = "btc_usdt_spot"
DEFAULT_FEES = TradeFeeSchema(
    maker_percent_fee_decimal=Decimal("0.002"),
    taker_percent_fee_decimal=Decimal("0.002"),
)


class BitwyreConfigMap(BaseConnectorConfigMap):
    connector: str = Field(default=CONSTANTS.EXCHANGE_NAME, client_data=None)
    bitwyre_api_key: SecretStr = Field(
        default=...,
        client_data=ClientFieldData(
            prompt=f"Enter your {CONSTANTS.EXCHANGE_NAME} API key",
            is_secure=True,
            is_connect_key=True,
            prompt_on_new=True,
        )
    )
    bitwyre_secret_key: SecretStr = Field(
        default=...,
        client_data=ClientFieldData(
            prompt=f"Enter your {CONSTANTS.EXCHANGE_NAME} secret key",
            is_secure=True,
            is_connect_key=True,
            prompt_on_new=True,
        )
    )

    class Config:
        title = CONSTANTS.EXCHANGE_NAME


KEYS = BitwyreConfigMap.construct()
