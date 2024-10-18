# A single source of truth for constant variables related to the exchange
from hummingbot.core.api_throttler.data_types import RateLimit

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

WS_PRIVATE_API = {
    "ORDER_CONTROL": "/ws/private/orders/control",
    "ORDER_STATUS": "/ws/private/orders/status"
}
WS_COMMANDS = {
    "ORDER_CREATE": "create",
    "ORDER_CANCEL": "cancel",
    "ORDER_GET": "get"
}

TIMEOUT = 5
SLEEP = 5

MID_PRICE = 30000
QTY = 0.5
PRICE_PRECISION = 2
QTY_PRECISION = 2
MIN_SPREAD = 0
MAX_SPREAD = 0.01

RATE_LIMITS = [
    RateLimit(limit_id=PATH_SERVER_TIME, limit=900, time_interval=1),
    RateLimit(limit_id=PATH_MARKETS, limit=900, time_interval=1),
    RateLimit(limit_id=PATH_TICKERS, limit=900, time_interval=1),
    RateLimit(limit_id=PATH_ASSETS, limit=900, time_interval=1),
    RateLimit(limit_id=PATH_CONTRACT, limit=900, time_interval=1),
    RateLimit(limit_id=PATH_OPEN_ORDER, limit=900, time_interval=1),
    RateLimit(limit_id=PATH_CANCEL_ORDER, limit=5_000, time_interval=1),
    RateLimit(limit_id=PATH_BALANCES, limit=900, time_interval=1),
    RateLimit(limit_id=PATH_ORDER_STATUS, limit=900, time_interval=1),
    RateLimit(limit_id=PATH_OPEN_ORDERS, limit=900, time_interval=1),
    RateLimit(limit_id=PATH_HISTORY_ORDERS, limit=900, time_interval=1),
    RateLimit(limit_id=PATH_MY_TRADES, limit=900, time_interval=1),
]

# TODO: add limits && timeouts && intervals
