#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
if(sys.version_info.major == 2):
    from .APIPython2_7 import HuobiUtil as HuobiUtils, HuobiService as HuobiServices
else:
    from .APIPython3 import Utils as HuobiUtils, HuobiServices as HuobiServices

from ...finance import *
#import ...finance
import system.log as log

class huobiAgentREST(exchangeAgent):       
    def __init__(self, accessKey, secretKey):
        exchangeAgent.__init__(self, accessKey, secretKey)
        
        self.__accountId = ''
                
        self.availableCommodities      = []
        self.exchangeMinQuantity       = {}
        self.exchangeMaxQuantity       = {}
        self.exchangeFrequency         = 10
        
        self.getAccounts               = object.callback(self.__getAccounts)
        self.getBalance                = object.callback(self.__getBalance)

        self.getKlines                 = object.callback(self.__getKlines)
        self.getMarketDepth            = object.callback(self.__getMarketDepth)
        self.getSymbols                = object.callback(HuobiServices.get_symbols)



    def __commodityPairSymbol(self, commodityPair):
        symbols = {
            CNY.code  : "cny",
            BTC.code  : "btc",
            LTC.code  : "ltc",
            USDT.code : "usdt"
        }        
        return symbols[commodityPair.base.code]+symbols[commodityPair.quote.code]

    def __setAPIKey(self):
        HuobiUtils.ACCESS_KEY = self._username
        HuobiUtils.SECRET_KEY = self._password
        HuobiUtils.ACCOUNT_ID = self.__accountId        
           
    
    def __getAccounts(self):
        self.__setAPIKey()
        return HuobiServices.get_accounts()
    
    def __getBalance(self):
        self.__setAPIKey()
        return HuobiServices.get_balance()
        
    def __getKlines(self, commodityPair, period, size=150):
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
        return HuobiServices.get_kline(self.__commodityPairSymbol(commodityPair), periodKey[period], size)
        
    def __getMarketDepth(self, commodityPair, depth):
        return HuobiServices.get_depth(self.__commodityPairSymbol(commodityPair), "step"+str(depth))

        
