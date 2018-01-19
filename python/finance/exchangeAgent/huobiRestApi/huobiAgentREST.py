#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
if(sys.version_info.major == 2):
    from .APIPython2_7 import HuobiUtil as HuobiUtils, HuobiService as HuobiServices
else:
    from .APIPython3 import Utils as HuobiUtils, HuobiServices as HuobiServices

from ...finance import *
import system.log as log

class huobiAgentREST(exchangeAgent):       
    def __init__(self, accessKey, secretKey, currency=CNY, commodity=BTC):
        self.__accessKey = accessKey
        self.__secretKey = secretKey
        self.__accountId = ''
        
        
        exchangeAgent.__init__(self, compair(commodity, currency))
        
        symbols = {
            CNY.code  : "cny",
            BTC.code  : "btc",
            LTC.code  : "ltc",
            USDT.code : "usdt"
        }        
        self.__compairSymbol = symbols[self.pair.base.code]+symbols[self.pair.quote.code]
        
       
        self.getKlines                 = exchangeAgent.method(self.__getKlines)
        self.getMarketDepth            = exchangeAgent.method(self.__getMarketDepth)
        self.getSymbols                = exchangeAgent.method(HuobiServices.get_symbols)
        self.getAccounts               = exchangeAgent.method(self.__getAccounts)

    def __setAPIKey(self):
        HuobiUtils.ACCESS_KEY = self.__accessKey
        HuobiUtils.SECRET_KEY = self.__secretKey
        HuobiUtils.ACCOUNT_ID = self.__accountId
    

    def __getKlines(self, period, size=150):
        periodKey = {
            Kmap.period.m1 : "1min",
            Kmap.period.m5 : "5min",
            Kmap.period.m15: "15min",
            Kmap.period.m30: "30min",
            Kmap.period.m60: "60min",
            Kmap.period.D1 : "1day",
            Kmap.period.W1 : "1week",
            Kmap.period.M1 : "1month",
            Kmap.period.Y1 : "1year"                                                                                                
        }
        return HuobiServices.get_kline(self.__compairSymbol, periodKey[period], size)
        
    def __getMarketDepth(self, depth):
        return HuobiServices.get_depth(self.__compairSymbol, "step"+str(depth))
    
    def __getAccounts(self):
        self.__setAPIKey()
        return HuobiServices.get_accounts()
        
