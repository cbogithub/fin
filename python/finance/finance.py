#!/usr/bin/env python
# -*- coding: utf-8 -*-


import system.log

financeLog = system.log.getStreamLogger('finance')

'''
abstract model
'''
class commodity:
    def __init__(self, code, symbol, precision):
        self.code      = code
        self.symbol    = symbol
        self.precision = precision
        
    def __eq__(self, another):
        return self.code == another.code
    
    def __ne__(self, another):
        return not self.__eq__(self, another)
    

'''
currency
'''
CNY = commodity('CNY', '¥', 0.01)
USD = commodity('USD', '$', 0.01)

'''
digit coin
'''
BTC = commodity('BTC', 'B', 0)
LTC = commodity('LTC', 'B', 0)
USDT = commodity('USDT', 'B', 0)





class compair:
    def __init__(self, base, quote = CNY):
        self.base  = base
        self.quote = quote

class position:
    def __init__(self, commodity, quantity):
        self.commodity = commodity
        self.quantity  = quantity

class positionExchange:
    def __init__(self, localPosition, remotePosition):
        self.local  = localPosition
        self.remote = remotePosition


'''
market component
'''
class order:
    class type:
        buy_market  = 0
        sell_market = 1
        buy_limit   = 2
        sell_limit  = 3

        name = "buy-market", "sell-market", "buy-limit", "sell-limit"

    class status:
        pre_submitted    = 0
        submitted        = 1
        partial_filled   = 2
        partial_canceled = 3
        filled           = 4
        canceled         = 5

        name = "pre-submitted", "submitted", "partial-filled", "partial-canceled", "filled", "canceled"

    def __init__(self, quantity=0, amount=0):
        pass

'''
rootaccount - plat - account (per compair) - connection
'''
class exchangeAgent:
    class method:
        def __init__(self, run=0):
            if(run == 0):
                self.__support = False
            else:
                self.__support = True
                self.__run       = run

        def run(self, *a):
            import time
            startTime = time.time()
            ret = self.__run(*a)
            endTime = time.time()
            print("method run cost %d ms" % int(round((endTime-startTime) * 1000))) 
            return ret

              
    def __init__(self, compair):
        self.pair                      = compair
        
        # getKlines (period, size)
        self.getKlines                 = self.method(self)
        
        self.historyRequest            = self.method(self)
        self.getAccountInfo            = self.method(self)
        self.getOrders                 = self.method(self)
        self.getOrderInfo              = self.method(self)
        self.buyLimit                  = self.method(self)
        self.buyMarket                 = self.method(self)
        self.sellLimit                 = self.method(self)
        self.sellMarket                = self.method(self)
        self.getNewDealOrders          = self.method(self)
        self.cancelOrder               = self.method(self)
        self.getTicker                 = self.method(self)        
        self.getDepth                  = self.method(self)


'''
    def historyRequest():
    def getAccountInfo():
    def getOrders():
    def getOrderInfo(, id):
    def buy(price, amount, tradePassword, tradeid):
    def buyMarket(price, amount, tradePassword, tradeid):
    def sell(price, amount, tradePassword, tradeid):
    def sellMarket(price, amount, tradePassword, tradeid):
    def getNewDealOrders():
    def getOrderIdByTradeId(tradeid):
    def cancelOrder(id):
    def getTicker():
    def getDepth(depth=5):
'''

class account:
    def __init__(self, exchangeConnection, measureCommodity = CNY):
        self.__exchangeConnection = exchangeConnection

        self.measure              = measureCommodity
        self.positions            = {}

    def getPosition(self, commodity):
        return self.positions[commodity] 

    def balance(self):
        return self.positions[self.measure].quantity

    def changePosition(self):
        return self.agent.orderRequest()


'''
analysis
'''
class Kmap:
    class period:
        s1   = 1
        s5   = 5*s1
        s15  = 15*s1
        s30  = 30*s1
        m1   = 60*s1
        m5   = 5*m1
        m15  = 15*m1
        m30  = 30*m1
        m60  = 60*m1
        h1   = 60*m1
        h4   = 4*h1
        D1   = 24*h1
        W1   = 5*D1
        M1   = 4*W1
        Y1   = 12*M1
        
    class Kline:
        def __init__(self):
            self.open  = 0
            self.close = 0
            self.low   = 0
            self.high  = 0 
        
class indicator:
    def __init__(self):
        pass

class tradePolicy:
    def __init__(self):
        pass





