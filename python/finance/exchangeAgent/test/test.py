#!/usr/bin/env python
# -*- coding: utf-8 -*-

from system import *
from finance import * 

configer = config("finance/exchangeAgent/test/account.conf")
huobi_cny_btc = huobiAgentApiV3(configer.get("huobi","accessKey"), configer.get("huobi", "secretKey"), CNY, BTC)
huobi_cny_btc2 = huobiAgentREST(configer.get("huobi","accessKey"), configer.get("huobi", "secretKey"), USDT, BTC)
huobi_cny_ltc2 = huobiAgentREST(configer.get("huobi","accessKey"), configer.get("huobi", "secretKey"), CNY, LTC)


financeLog.info("============== API V3 ===============")
financeLog.info("--------------------- getAccountInfo:")
financeLog.info(huobi_cny_btc.getAccountInfo.run())

financeLog.info("--------------------- getMarketDepth:")
financeLog.info(huobi_cny_btc.getMarketDepth.run())

financeLog.info("--------------------- getTicker:")
financeLog.info(huobi_cny_btc.getTicker.run())

financeLog.info("============= REST API ===============")
financeLog.info("--------------------- getKlines:")
financeLog.info(huobi_cny_btc2.getKlines.run(Kmap.period.m1, 5))

financeLog.info("--------------------- getMarketDepth:")
financeLog.info(huobi_cny_btc2.getMarketDepth.run(4))

financeLog.info("--------------------- getSymbols")
financeLog.info(huobi_cny_btc2.getSymbols.run())

financeLog.info("--------------------- getAccounts")
financeLog.info(huobi_cny_btc2.getAccounts.run())




