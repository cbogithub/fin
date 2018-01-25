#!/usr/bin/env python
# -*- coding: utf-8 -*-


from system import *
from finance import *
import time

spreadTradeLogger = log.getFileLogger("spreadTrade", "log/spreadMarket.log")
spreadTradeLogger = log.getStreamLogger('spreadTrade')    
        
class orderBook:
    def __init__(self, orderbook):
        self.__orderbook = orderbook
        
    def getBuy(priceLimit=None, amountLimit=None):
        return list(self.__orderbook['bids'][0][0], self.__orderbook['bids'][0][1])
        
    def geSell(priceLimit=None, amountLimit=None):
        return list(self.__orderbook['sell'][0][0], self.__orderbook['asks'][0][1])
          
            
class marketOffer:
    def __init__(self, buyPrice, sellPrice, buyQuantity=0, sellQuantity=0):
        self.buyprice     = buyPrice
        self.sellprice    = sellPrice
        self.buyquantity  = buyQuantity
        self.sellquantity = sellQuantity
        

class dataStat:
    def __init__(self, avgPeriod=10, radii=0.005):
        self.__limit = avgPeriod + 5
        self.__data  = []
        
        self.__cnt   = 0
        self.__total = 0
        self.__min   = None
        self.__max   = None

        self.__avgPeriod = avgPeriod
        self.__radii     = radii
        self.__relation  = 0
        self.__upHit     = 0
        self.__downHit   = 0
    
    def add(self, value):
        if(self.__cnt == 0):
            self.__min = value
            self.__max = value
        else:
            if(value > self.__max):
                self.__max = value
            if(value < self.__min):
                self.__min = value
        self.__cnt   += 1
        self.__total += value
        if(self.__limit !=0 and len(self.__data) >= self.__limit):
            del self.__data[0]
        self.__data.append(value)
        
        if(len(self.__data) >= self.__avgPeriod): 
            avg = self.average(self.__avgPeriod)
            relation = 0
            if(value >= avg+self.__radii):
                relation = 1
                if(self.__relation != relation):
                    self.__upHit += 1
            if(value <= avg-self.__radii):
                relation = -1
                if(self.__relation != relation):
                    self.__downHit += 1                
            self.__relation = relation


    def min(self):
        return self.__min

    def max(self):
        return self.__max

    def cnt(self):
        return self.__cnt
        
    def total(self):
        return self.__total
        
    def upHit(self):
        return self.__upHit
    def downHit(self):
        return self.__downHit

        
    def __listTotal(self, list):
        totalval = 0
        for item in list:
            totalval += item
        return totalval
        
    def average(self, period=0):
        if(self.__cnt == 0):
            return None
        if(period == 0):
            return self.__total/self.__cnt
        if(period < len(self.__data)):
            return self.__listTotal(self.__data[(-1*period):])/period
        else:
            return self.__listTotal(self.__data)/len(self.__data)
        return None            


class spreadDiff:
    def __init__(self, exchangeId1, exchangeId2):
        self.exchange1 = exchangeId1
        self.exchange2 = exchangeId2
        self.diff12 = dataStat(10, 0.005)
        self.diff21 = dataStat(10, 0.005)

    def addOderBook(self, orderbook1, orderbook2):
        if(orderbook1['bids'][0][0]==0 or orderbook2['bids'][0][0]==0):
            return
        self.diff12.add(100*(orderbook1['bids'][0][0] - orderbook2['asks'][0][0])/orderbook1['bids'][0][0])
        self.diff21.add(100*(orderbook2['bids'][0][0] - orderbook1['asks'][0][0])/orderbook2['bids'][0][0])        
        spreadTradeLogger.debug("%s - %s : %s %%" % (self.exchange1, self.exchange2, 100*(orderbook1['bids'][0][0] - orderbook2['asks'][0][0])/orderbook1['bids'][0][0]))
        spreadTradeLogger.debug("%s - %s : %s %%" % (self.exchange2, self.exchange1, 100*(orderbook2['bids'][0][0] - orderbook1['asks'][0][0])/orderbook2['bids'][0][0]))
        
    def checkSignal(self):
        spreadTradeLogger.debug("%s - %s : [%s - %s, %s], hit[%s, %s] cnt:%s, avg:%s, " % (self.exchange1, self.exchange2, self.diff12.min(), self.diff12.max(), self.diff12.max()- self.diff12.min(), self.diff12.upHit(), self.diff12.downHit(), self.diff12.cnt(), self.diff12.average()))
        spreadTradeLogger.debug("%s - %s : [%s - %s, %s], hit[%s, %s] cnt:%s, avg:%s, " % (self.exchange2, self.exchange1, self.diff21.min(), self.diff21.max(), self.diff21.max()- self.diff21.min(), self.diff21.upHit(), self.diff21.downHit(), self.diff21.cnt(), self.diff21.average()))

    def report(self):
        spreadTradeLogger.info("%s - %s : [%s - %s, %s], hit[%s, %s] cnt:%s, avg:%s, " % (self.exchange1, self.exchange2, self.diff12.min(), self.diff12.max(), self.diff12.max()- self.diff12.min(), self.diff12.upHit(), self.diff12.downHit(), self.diff12.cnt(), self.diff12.average()))
        spreadTradeLogger.info("%s - %s : [%s - %s, %s], hit[%s, %s] cnt:%s, avg:%s, " % (self.exchange2, self.exchange1, self.diff21.min(), self.diff21.max(), self.diff21.max()- self.diff21.min(), self.diff21.upHit(), self.diff21.downHit(), self.diff21.cnt(), self.diff21.average()))


class spreadTrade(trade.policy):
    KEY_SYMBOLS           = "symbols"
    KEY_EXCHANGES         = "exchanges"
    KEY_LOOPPERIOD        = "loop_period"
    KEY_RATE_LIMIT        = "rate_limit"     
    KEY_MARKET_TRADE_RATE = "market_trade_rate"
    KEY_ORDER_EXPIRE      = "order_expire" 
    KEY_RUN_SAFE          = "run_safe"
    KEY_RUN_TIME          = "run_time"
        
    def __init__(self, params={}):
        # default
        paramSet = {
            self.KEY_SYMBOLS           : "",
            self.KEY_EXCHANGES         : "",
            self.KEY_LOOPPERIOD        : 60,
            self.KEY_RATE_LIMIT        : 2,            
            self.KEY_MARKET_TRADE_RATE : 0.5, 
            self.KEY_ORDER_EXPIRE      : 3,
            self.KEY_RUN_SAFE          : True,
            self.KEY_RUN_TIME          : 60
        }
        

        # update from param
        object.dicUpdateByKeys(paramSet, params, paramSet.keys()) 
        
        # set            
        self.__symbols          = paramSet[self.KEY_SYMBOLS]
        self.__exchangeIds      = paramSet[self.KEY_EXCHANGES]
        self.__loopPeriod       = paramSet[self.KEY_LOOPPERIOD]
        self.__rateLimit        = paramSet[self.KEY_RATE_LIMIT]        
        self.__marketTradeRate  = paramSet[self.KEY_MARKET_TRADE_RATE]
        self.__orderExpire      = paramSet[self.KEY_ORDER_EXPIRE]
        self.__safeMode         = paramSet[self.KEY_RUN_SAFE]
        self.__runTimeLen       = paramSet[self.KEY_RUN_TIME]

        self.__connectDebug    = False
        self.__startTime       = time.time()
        self.__symbolExchanges = {}
        self.__spreadDiff      = {}

        for symbol in self.__symbols:
            self.__spreadDiff[symbol] = {}

        self.init()

    def init(self, params={}):
        # setup timeLogger                    
        self.__dataLogger = log.getFileLogger("spreadMarket", "finance/ATS/data/spreadMarket.txt")

        # init exchanges
        exchanges = []
        for exId in self.__exchangeIds:
            exchanges.append(exchangeAgent.ccxtExchange(exId, params))

        
        # load markets
        failedExchanges = []
        for ex in exchanges:
            if(self.__loadMarkets(ex) == None):
                spreadTradeLogger.error(" %s loadMarkets failed!  ignore this exchange!" % ex.id())
                failedExchanges.append(ex)
        
        for ex in failedExchanges:
            exchanges.remove(ex)

        # validate pair
        for  symbol in self.__symbols:
            #self.__spreadDiff[symbol] = {} # watch mode, not clean data
            self.__symbolExchanges[symbol] = []
            for exchange in exchanges:
                if symbol in exchange.symbols():
                    self.__symbolExchanges[symbol].append(exchange)

        # init index: diff                
        for  symbol in self.__symbols:
            for ex1 in self.__symbolExchanges[symbol]:
                match = False
                for ex2 in self.__symbolExchanges[symbol]:
                    if(	ex1 == ex2):
                        match = True
                    elif(match):
                        key = ex1.id()+"/"+ex2.id()
                        if(not self.__spreadDiff[symbol].has_key(key)): # watch mode, not clean data
                            self.__spreadDiff[symbol][key] = spreadDiff(ex1.id(), ex2.id())

    def deinit(self):
        for symbol in self.__symbols:
            for key in self.__spreadDiff[symbol].keys():
                #del self.__spreadDiff[symbol][key]
                pass # watch mode, not clean data
        
        for  symbol in self.__symbols:
            for exchange in self.__symbolExchanges[symbol]:
                del exchange

    def __loadMarkets(self, exchange, retry=3, period=3):
        if(self.__connectDebug):
            return exchange.loadMarkets()
        else:
            for cnt in range(1, retry+1):
                try:
                    return exchange.loadMarkets()
                except:
                    if(cnt >= retry):
                        spreadTradeLogger.warning(" %s loadMarkets failed %s tims, ignore this exchange!" % (exchange.id(), cnt))
                        return None
                    spreadTradeLogger.warning(" %s loadMarkets failed %s tims, wait %s s to retry!" % (exchange.id(), cnt, period))
                    time.sleep(period)

    def __fetchOderbook(self, exchange, symbol, retry=2, period=1):
        if(self.__connectDebug):
            return exchange.fetchOrderBook(symbol)
        else:    
            for cnt in range(1, retry+1):
                try:
                    return exchange.fetchOrderBook(symbol)
                except:            
                    if(cnt >= retry):
                        spreadTradeLogger.warning(" %s fetchOrderBook failed %s tims, skip this fetch!" % (exchange.id(), cnt))
                        return None
                    spreadTradeLogger.warning(" %s fetchOrderBook failed %s tims, wait %s s to retry!" % (exchange.id(), cnt, period))
                    time.sleep(period)

                                                                
    def check(self):
        #  upate market
        orderBooks = {}
        for symbol in self.__symbols:
            orderBooks[symbol] = {}
            time.sleep(self.__rateLimit) 
            for exchange in self.__symbolExchanges[symbol]:
                ret = self.__fetchOderbook(exchange, symbol)
                if(ret == None):
                    spreadTradeLogger.error("%s - %s :fetch oderbook faild!" % (symbol, exchange.id()))
                    orderBooks[symbol][exchange.id()] = {'bids': [[0, 0]], 'asks': [[0,0]]} 
                elif(not ret.has_key('bids'))
                    spreadTradeLogger.error("error order response", ret)                    
                else:
                    orderBooks[symbol][exchange.id()] = ret
                    spreadTradeLogger.debug("%s - %s :  bid %s(%s), ask %s(%s)" % (symbol, exchange.id(), orderBooks[symbol][exchange.id()]['bids'][0][0], orderBooks[symbol][exchange.id()]['bids'][0][1], orderBooks[symbol][exchange.id()]['asks'][0][0], orderBooks[symbol][exchange.id()]['asks'][0][1]))
            
        # update diff
        for symbol in self.__symbols:
            spreadTradeLogger.debug("------------ check %s -----------" % symbol)
            for key in self.__spreadDiff[symbol].keys():
                self.__spreadDiff[symbol][key].addOderBook(orderBooks[symbol][key.split('/')[0]], orderBooks[symbol][key.split('/')[1]])
                self.__spreadDiff[symbol][key].checkSignal()

    def run(self):
        spreadTradeLogger.info(" =========================== spreadMaket start run !")
        checkCnt = 0
        hit = 0
        restart = 0
        
        while (True): 
            runtime = time.time() - self.__startTime
            if(runtime >= self.__runTimeLen):
                spreadTradeLogger.info("policy run %s s (>= %s), now exit...", runtime, self.__runTimeLen)
                break;     
            checkCnt += 1
          
            if(self.__safeMode):
                try:
                    self.check()
                except:
                    restart += 1
                    spreadTradeLogger.error(" oops, the %d restarting !" % restart)
                    self.deinit()
                    time.sleep(self.__rateLimit * 2)
                    self.init()
                    continue
            else:
                self.check()                      
            spreadTradeLogger.info(" finished the %d check (hit %d, restart %d), sleep %d s for next check, total run %s s" % (checkCnt, hit, restart, self.__loopPeriod, runtime))
            time.sleep(self.__loopPeriod)
            
        spreadTradeLogger.info(" ################### spreadTrade report: ##########")             
        for symbol in self.__symbols:
            spreadTradeLogger.info("------------ check %s -----------" % symbol)
            for key in self.__spreadDiff[symbol].keys():
                self.__spreadDiff[symbol][key].report()
        spreadTradeLogger.info(" spreadTrade stoped!")   