#!/usr/bin/env python
# -*- coding: utf-8 -*-

from finance import *



watchProfile={
    "symbols"            : ["ETH/BTC"],
    "exchanges"          : ["huobipro", "bitfinex"],
    "loop_period"        : 30,
    "rate_limit"         : 2,
    "order_expire"       : 2,
    "markeet_trade_rate" : 0.1
}

hb = ATS.spreadTrade(watchProfile)

hb.run()

