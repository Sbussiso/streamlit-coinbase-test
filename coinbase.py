# This is a summary of all the code for this tutorial
from coinbase.rest import RESTClient
from json import dumps
import math


api_key = "organizations/{org_id}/apiKeys/{key_id}"
api_secret = "-----BEGIN EC PRIVATE KEY-----\nYOUR PRIVATE KEY\n-----END EC PRIVATE KEY-----\n"

client = RESTClient(api_key=api_key, api_secret=api_secret)



product = client.get_product("BTC-USD")
btc_usd_price = float(product["price"])
adjusted_btc_usd_price = str(math.floor(btc_usd_price - (btc_usd_price * 0.05)))

order = client.limit_order_gtc_buy(
    client_order_id="00000002",
    product_id="BTC-USD",
    base_size="0.0002",
    limit_price=adjusted_btc_usd_price
)

if order['success']:
    order_id = order['success_response']['order_id']
    client.cancel_orders(order_ids=[order_id])
else:
    error_response = order['error_response']
    print(error_response)


