# A single source of truth for constant variables related to the exchange
from hummingbot.core.api_throttler.data_types import LinkedLimitWeightPair, RateLimit

EXCHANGE_NAME = "bitwyre"
DEFAULT_DOMAIN = ""
BROKER_ID = "hummingbot"

URL_REST = "https://api.bitwyre.com/"
URL_WS = "wss://api.bitwyre.com/ws/"

# Public endpoints
PATH_SERVER_TIME = "time"
PATH_MARKETS = "markets"
PATH_TICKERS = "ticker"
PATH_ASSETS = "assets"
PATH_CONTRACT = "contract"

# Private endpoints
PATH_OPEN_ORDER = "orders"
PATH_CANCEL_ORDER = "orders/cancel"
PATH_BALANCES = "account/spotbalance"
PATH_ORDER_STATUS = "orders/info/{order_id}"
PATH_OPEN_ORDERS = "orders/open/all"
PATH_HISTORY_ORDERS = "orders/histories"
PATH_MY_TRADES = "trades"

# TODO: add limits && timeouts && intervals

