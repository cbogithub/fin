#!/usr/bin/env python
# -*- coding: utf-8 -*-

from .huobi import util as HuobiUtils, huobiService as HuobiServices

from ...finance import *
import system.log as log

class huobiAgentApiV3(exchangeAgent):    
    def __init__(self, accessKey, secretKey):
        exchangeAgent.__init__(self, accessKey, secretKey)
                
        self.getAccountInfo            = object.callback(self.__getAccountInfo)
        self.getMarketDepth            = object.callback(self.__getMarketDepth)
        self.getTicker                 = object.callback(self.__getTicker)

    def __getMarketType(self, currency):
        market = {
            CNY.code : HuobiServices.COIN_TYPE_CNY,
            USD.code : HuobiServices.COIN_TYPE_USD
        }
        return market[currency.code]

    def __getCoinType(self, coin):
        coinType = {
            BTC.code : HuobiServices.HUOBI_COIN_TYPE_BTC,
            LTC.code : HuobiServices.HUOBI_COIN_TYPE_LTC
        }
        return coinType[coin.code]
        
    def __setAPIKeys(self):
        HuobiUtils.ACCESS_KEY = self._username
        HuobiUtils.SECRET_KEY = self._password
    
    
    def __getAccountInfo(self, currency=CNY):
        self.__setAPIKeys()
        return HuobiServices.getAccountInfo(self.__getMarketType(currency), HuobiUtils.ACCOUNT_INFO)

    def __getMarketDepth(self, commodityPair, depth=5):
        return HuobiServices.getDepth(self.__getCoinType(commodityPair.base), self.__getMarketType(commodityPair.quote), depth)
        
    def __getTicker(self, commodityPair): 
        return HuobiServices.getTicker(self.__getCoinType(commodityPair.base), self.__getMarketType(commodityPair.quote))
        
