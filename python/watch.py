#!/usr/bin/env python
# -*- coding: utf-8 -*-

from finance import *


watchProfile={
    "symbols"            : ['BTC/USDT','ETH/BTC','ETH/USDT','LTC/BTC','LTC/USDT', 'BCH/USDT','ETC/USDT','BTC/EUR','BTC/USD','ETH/USD','LTC/USD','BCH/BTC','BCH/ETH','BCH/USD','ETC/BTC','ETC/USD'],
#    "exchanges"          : ["gdax", "huobipro", "binance", "bithumb", "okex", "bitfinex", "kucoin", "bittrex", "poloniex", "okcoinusd", "bitstamp"],  # all top
#    "exchanges"          : ["gdax", "huobipro", "binance", "bitfinex", "kucoin", "bittrex", "poloniex", "bitstamp"],   # usa available
    "exchanges"          : ["gdax", "huobipro", "binance", "bithumb", "okex", "bitfinex", "kucoin", "bittrex", "okcoinusd", "bitstamp"], # china available
    "loop_period"        : 10,
    "rate_limit"         : 2,
    "order_expire"       : 2,
    "markeet_trade_rate" : 0.1,
    "run_time"           : 60
}

hb = ATS.spreadTrade(watchProfile)

hb.run()

