#!/usr/bin/env python
# -*- coding: utf-8 -*-

from system import *
from finance import * 

configer = config("finance/exchangeAgent/test/account.conf")
huobi_cny_btc = huobiAgentApiV3(configer.get("huobi","accessKey"), configer.get("huobi", "secretKey"), CNY, BTC)
huobi_cny_btc2 = huobiAgentREST(configer.get("huobi","accessKey"), configer.get("huobi", "secretKey"), USDT, BTC)
huobi_cny_ltc2 = huobiAgentREST(configer.get("huobi","accessKey"), configer.get("huobi", "secretKey"), CNY, LTC)


loger.info("============== API V3 ===============")
loger.info("--------------------- getAccountInfo:")
loger.info(huobi_cny_btc.getAccountInfo.run())

loger.info("--------------------- getMarketDepth:")
loger.info(huobi_cny_btc.getMarketDepth.run())

loger.info("--------------------- getTicker:")
loger.info(huobi_cny_btc.getTicker.run())

loger.info("============= REST API ===============")
loger.info("--------------------- getKlines:")
loger.info(huobi_cny_btc2.getKlines.run(Kmap.period.m1, 5))

loger.info("--------------------- getMarketDepth:")
loger.info(huobi_cny_btc2.getMarketDepth.run(4))

loger.info("--------------------- getSymbols")
loger.info(huobi_cny_btc2.getSymbols.run())

loger.info("--------------------- getAccounts")
loger.info(huobi_cny_btc2.getAccounts.run())




