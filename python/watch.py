#!/usr/bin/env python
# -*- coding: utf-8 -*-

from finance import *


watchProfile={
#    "symbols"            : ["ETH/BTC"],
    "symbols"            : ['BTC/USDT','ETH/BTC','ETH/USDT','LTC/BTC','LTC/USDT', 'BCH/USDT','ETC/USDT','BTC/EUR','BTC/USD','ETH/USD','LTC/USD','BCH/BTC','BCH/ETH','BCH/USD','ETC/BTC','ETC/USD'],
    "exchanges"          : ["huobipro", "bitfinex", "binance","okex"],
    "loop_period"        : 30,
    "rate_limit"         : 2,
    "order_expire"       : 2,
    "markeet_trade_rate" : 0.1
}

hb = ATS.spreadTrade(watchProfile)

hb.run()

