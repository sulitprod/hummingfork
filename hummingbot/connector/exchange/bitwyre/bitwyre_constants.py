# A single source of truth for constant variables related to the exchange
from hummingbot.core.api_throttler.data_types import LinkedLimitWeightPair, RateLimit

EXCHANGE_NAME = "bitwyre"
DEFAULT_DOMAIN = ""
BROKER_ID = "hummingbot"

URL_REST = "https://api.bitwyre.com/"
URL_WS = "wss://api.bitwyre.com/ws/"

# Public endpoints
PATH_SERVER_TIME = "public/time"
PATH_MARKETS = "public/markets"
PATH_TICKERS = "public/ticker"
PATH_ASSETS = "public/assets"
PATH_CONTRACT = "public/contract"

# Private endpoints
PATH_OPEN_ORDER = "private/orders"
PATH_CANCEL_ORDER = "private/orders/cancel"
PATH_BALANCES = "private/account/spotbalance"
PATH_ORDER_STATUS = "private/orders/info/{order_id}"
PATH_OPEN_ORDERS = "private/orders/open/all"
PATH_HISTORY_ORDERS = "private/orders/histories"
PATH_MY_TRADES = "private/trades"
