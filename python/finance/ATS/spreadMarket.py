#!/usr/bin/env python
# -*- coding: utf-8 -*-


from system import config, log
from finance import finance
import time


class marketOffer:
    def __init__(self, buyPrice, sellPrice, buyQuantity=0, sellQuantity=0):
        self.buyprice     = buyPrice
        self.sellprice    = sellPrice
        self.buyquantity  = buyQuantity
        self.sellquantity = sellQuantity
                    

class spreadMarketPair:
    def __init__(self, market1, market2):
        self.market1 = market1
        self.market2 = market2
        self.diff12  = []
        self.diff21  = []
        
    def addOffer(self, market1, market2):
        self.diff12.append(market1.buyPrice - market2.sellPrice)
        self.diff21.append(market2.buyPrice - market1.sellPrice)
        
    def checkSignal():
        #signal = avgCheck(self.diff12)
        #signal = avgCheck(self.diff21)
        '''
        if(signal.action == BUY)
            market1.buy()
            market2.sell()
        elif(signal.action == SELL)
            market1.sell()
            market2.buy()
        '''
        __logger.info("check Signal")

class spreadMarket(finance.tradePolicy):
    def __init__(self, tradePair=None, markets=None):
        self.__logger = log.getFileLogger("spreadMarket", "log/spreadMarket.log")
        self.__logger = log.getStreamLogger('f.spreadMarket')

        self.__tradepaire        = tradePair

        configer = config("finance/ATS/conf/spreadMarket.conf")
        self.orderRatio       = configer.getfloat("policy", "orderRatio")
        self.__loopPeriod     = configer.getfloat("policy", "loopPeriod")  # 每次循环结束之后睡眠的时间, 单位：秒
        self.orderWaitingTime = configer.get("policy", "orderWaitingTime")    # 每次等待订单执行的最长时间

      
        #self.coinMarketType   = configer.get("account", "coinMarket")
                

        # okcoin 的比特币最小市价买单下单金额是：0.01BTC*比特币当时市价
        # okcoin 的莱特币最小市价买单下单金额是：0.1LTC*莱特币当时市价
        #self.last_data_log_time = None

        # setup timeLogger               
        self.__dataLogger = log.getFileLogger("spreadMarket", "finance/ATS/data/spreadMarket.txt")

        # markets
        self.__markets = markets
        self.__marketPairs = []
        self.marketOffers  = {}

        for market1 in self.__markets:
            match = False
            for market2 in self.__markets:
                if(market1 == market2):
                    match = True
                elif(match):
                    self.__marketPairs.append(spreadMarketPair(market1, market2))

    def run(self):
        self.__logger.info(" =========================== spreadMaket start run !")

        while (True):
            self.__logger.info("wait %d s for next loop..." % self.__loopPeriod)
            time.sleep(self.__loopPeriod)

            #  get markets
            for market in self.__markets:
                depthResult = market.getMarketDepth.run(self.__tradepaire, 1)
                mo = marketOffer(depthResult["tick"]["bids"][0][0], depthResult["tick"]["asks"][0][0], depthResult["tick"]["bids"][0][1], depthResult["tick"]["asks"][0][1])
                self.marketOffers[market] = mo
            
            # generate diff map
            for pair in self.__marketPairs:
                pair.addOffer(self.marketOffers[pair.market1], self.marketOffers[market2])
                pair.checkSignal()
            

                    
            
