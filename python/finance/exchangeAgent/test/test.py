#!/usr/bin/env python
# -*- coding: utf-8 -*-

from system import *
from finance import * 

configer = config("finance/exchangeAgent/test/account.conf")
btccny=commodityPair(BTC, CNY)
btcusdt=commodityPair(BTC, USDT)
ltccny=commodityPair(LTC,CNY)


financeLog.info("============== API V3 ===============")
huobi_apiv3 = huobiAgentApiV3(configer.get("huobi","accessKey"), configer.get("huobi", "secretKey"))
financeLog.info("--------------------- getAccountInfo:")
financeLog.info(huobi_apiv3.getAccountInfo.run(CNY))

financeLog.info("--------------------- getMarketDepth:")
financeLog.info(huobi_apiv3.getMarketDepth.run(btccny))

financeLog.info("--------------------- getTicker:")
financeLog.info(huobi_apiv3.getTicker.run(btccny))

financeLog.info("============= REST API ===============")
huobiRest = huobiAgentREST(configer.get("huobi","accessKey"), configer.get("huobi", "secretKey"))
financeLog.info("--------------------- getKlines:")
financeLog.info(huobiRest.getKlines.run(btcusdt, Kmap.period.m1, 5))

financeLog.info("--------------------- getMarketDepth:")
financeLog.info(huobiRest.getMarketDepth.run(btcusdt, 4))

financeLog.info("--------------------- getSymbols")
financeLog.info(huobiRest.getSymbols.run())

financeLog.info("--------------------- getAccounts")
financeLog.info(huobiRest.getAccounts.run())

financeLog.info("--------------------- getBalance")
financeLog.info(huobiRest.getBalance.run())

