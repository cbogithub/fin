#!/usr/bin/env python
# -*- coding: utf-8 -*-

from .huobi import util as HuobiUtils, huobiService as HuobiServices

from ...finance import *
import system.log as log

class huobiAgentApiV3(exchangeAgent):    
    def __init__(self, accessKey, secretKey, currency=CNY, commodity=BTC):
        self.__accessKey = accessKey
        self.__secretKey = secretKey
        
        market = {
            CNY.code : HuobiServices.COIN_TYPE_CNY,
            USD.code : HuobiServices.COIN_TYPE_USD
        }
        coin = {
            BTC.code : HuobiServices.HUOBI_COIN_TYPE_BTC,
            LTC.code : HuobiServices.HUOBI_COIN_TYPE_LTC
        }
        self.__market = market[currency.code]
        self.__coin = market[currency.code]

        exchangeAgent.__init__(self, compair(commodity, currency))
        self.getAccountInfo            = exchangeAgent.method(self.__getAccountInfo)
        self.getMarketDepth            = exchangeAgent.method(self.__getMarketDepth)
        self.getTicker                 = exchangeAgent.method(self.__getTicker)

    def __setAPIKeys(self):
        HuobiUtils.ACCESS_KEY = self.__accessKey
        HuobiUtils.SECRET_KEY = self.__secretKey
    
    
    def __getAccountInfo(self):
        self.__setAPIKeys()
        return HuobiServices.getAccountInfo(self.__market, HuobiUtils.ACCOUNT_INFO)

    def __getMarketDepth(self, depth=5):
        return HuobiServices.getDepth(self.__coin, self.__market, depth)
        
    def __getTicker(self): 
        return HuobiServices.getTicker(self.__coin, self.__market)
        
