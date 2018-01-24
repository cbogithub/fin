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

digits = ATS.dataStat()

digits.add(1.111)
digits.add(2.222)
digits.add(3.333)

print(digits.upHit(),digits.downHit(),digits.cnt(),digits.average())


