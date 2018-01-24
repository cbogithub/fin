#!/usr/bin/python
# -*- coding: utf-8 -*-

import ccxt
import json
from system import *
from finance.trade import exchange

class ccxtExchange(exchange):
    KEY_APIKEY   = "apiKey"
    KEY_SECRET   = "secret"
    KEY_PASSWORD = "password"
    KEY_UID      = "uid"
        
    def __init__(self, exchangeId, param={}):
        # param defalt
        paramSet = {
            exchange.KEY_RATE_LIMIT      : 1,
            exchange.KEY_SYMBOLS_PROFILE : {}
        }
        
        # param update from profile
        profile = json.load(open('finance/exchangeAgent/exchangeProfile.json'))
        account = json.load(open('finance/exchangeAgent/exchangeAccount.json'))
        
        if(profile.has_key(exchangeId)):
            object.dicUpdateByKeys(paramSet, profile[exchangeId], paramSet.keys())        

        # param update from param
        object.dicUpdateByKeys(paramSet, param, paramSet.keys())  
        
        # param set
        exchange.__init__(self, exchangeId, paramSet)


        # cctx param default
        paramSet = {
            self.KEY_APIKEY   : "",
            self.KEY_SECRET   : "",
            self.KEY_PASSWORD : "",
            self.KEY_UID      : ""
        }
        
        # cctx param update form  profile
        if(account.has_key(exchangeId)):
            object.dicUpdateByKeys(paramSet, profile[exchangeId], paramSet.keys())        

        # cctx param update form param
        object.dicUpdateByKeys(paramSet, param)  
        
        # cctx param set        
        self.__exchange  = ccxtExchanges[exchangeId](param)

    # param
    def symbols(self):
        return self.__exchange.symbols
    def markets(self):
        return self.__exchange.markets
       
    # public
    def loadMarkets(self):
        return self.__exchange.loadMarkets()
    def fetchMarkets(self):
        return self.__exchange.fetchMarkets()
    def fetchTicker(self, symbol):
        return self.__exchange.fetchTicker(symbol)
    def fetchTickers(self):
        return self.__exchange.fetchTickers()
    def fetchOrderBook(self, symbol, params={}):
        return self.__exchange.fetchOrderBook(symbol, params)
    def fetchL2OrderBook(self, symbol, params={}):
        return self.__exchange.fetchL2OrderBook(symbol, params)        
    def fetchOHLCV(self):
        return self.__exchange.fetchOHLCV()
    def fetchTrades(self, symbol, since=None, limit=None, params={}):
        return self.__exchange.fetchTrades(symbol, since, limit, params)

    # private
    def fetchBalance(self):
        return self.__exchange.fetchBalance()
    def createOrder(self, symbol, type, side, amount, price=None, params={}):
        return self.__exchange.createOrder(symbol, type, side, amount, price, params)
    def createLimitBuyOrder(self, symbol, amount, price, params={}):
        return self.__exchange.createLimitBuyOrder(symbol, amount, price, params)
    def createLimitSellOrder(self, symbol, amount, price, params={}):
        return self.__exchange.createLimitSellOrder(symbol, amount, price, params)
    def createMarketBuyOrder(self, symbol, amount, params={}):
        return self.__exchange.createMarketBuyOrder(symbol, amount, params)
    def createMarketSellOrder(self, symbol, amount, params={}):
        return self.__exchange.createMarketSellOrder(symbol, amount, params)
    def cancelOrder(self, id, symbol=None, params={}):
        return self.__exchange.cancelOrder(id, symbol, params)
    def fetchOrder(self, symbol=None, params={}):
        return self.__exchange.fetchOrder(symbol, params)
    def fetchOpenOrders(self, symbol=None, params={}):
        return self.__exchange.fetchOpenOrders(symbol, params)
    def fetchClosedOrders(self, symbol=None, params={}):
        return self.__exchange.fetchClosedOrders(symbol, params)
        
ccxtExchanges={
"_1broker": ccxt._1broker,
"_1btcxe": ccxt._1btcxe,
"acx": ccxt.acx,
"allcoin": ccxt.allcoin,
"anxpro": ccxt.anxpro,
"bibox": ccxt.bibox,
"binance": ccxt.binance,
"bit2c": ccxt.bit2c,
"bitbay": ccxt.bitbay,
"bitcoincoid": ccxt.bitcoincoid,
"bitfinex": ccxt.bitfinex,
"bitfinex2": ccxt.bitfinex2,
"bitflyer": ccxt.bitflyer,
"bithumb": ccxt.bithumb,
"bitlish": ccxt.bitlish,
"bitmarket": ccxt.bitmarket,
"bitmex": ccxt.bitmex,
"bitso": ccxt.bitso,
"bitstamp": ccxt.bitstamp,
"bitstamp1": ccxt.bitstamp1,
"bittrex": ccxt.bittrex,
"bl3p": ccxt.bl3p,
"bleutrade": ccxt.bleutrade,
"braziliex": ccxt.braziliex,
"btcbox": ccxt.btcbox,
"btcchina": ccxt.btcchina,
"btcexchange": ccxt.btcexchange,
"btcmarkets": ccxt.btcmarkets,
"btctradeua": ccxt.btctradeua,
"btcturk": ccxt.btcturk,
"btcx": ccxt.btcx,
"bter": ccxt.bter,
"bxinth": ccxt.bxinth,
"ccex": ccxt.ccex,
"cex": ccxt.cex,
"chbtc": ccxt.chbtc,
"chilebit": ccxt.chilebit,
"coincheck": ccxt.coincheck,
"coinexchange": ccxt.coinexchange,
"coinfloor": ccxt.coinfloor,
"coingi": ccxt.coingi,
"coinmarketcap": ccxt.coinmarketcap,
"coinmate": ccxt.coinmate,
"coinsecure": ccxt.coinsecure,
"coinspot": ccxt.coinspot,
"cryptopia": ccxt.cryptopia,
"dsx": ccxt.dsx,
"exmo": ccxt.exmo,
"flowbtc": ccxt.flowbtc,
"foxbit": ccxt.foxbit,
"fybse": ccxt.fybse,
"fybsg": ccxt.fybsg,
"gatecoin": ccxt.gatecoin,
"gateio": ccxt.gateio,
"gdax": ccxt.gdax,
"gemini": ccxt.gemini,
"getbtc": ccxt.getbtc,
"hitbtc": ccxt.hitbtc,
"hitbtc2": ccxt.hitbtc2,
"huobi": ccxt.huobi,
"huobicny": ccxt.huobicny,
"huobipro": ccxt.huobipro,
"independentreserve": ccxt.independentreserve,
"itbit": ccxt.itbit,
"jubi": ccxt.jubi,
"kraken": ccxt.kraken,
"kucoin": ccxt.kucoin,
"kuna": ccxt.kuna,
"lakebtc": ccxt.lakebtc,
"liqui": ccxt.liqui,
"livecoin": ccxt.livecoin,
"luno": ccxt.luno,
"lykke": ccxt.lykke,
"mercado": ccxt.mercado,
"mixcoins": ccxt.mixcoins,
"nova": ccxt.nova,
"okcoincny": ccxt.okcoincny,
"okcoinusd": ccxt.okcoinusd,
"okex": ccxt.okex,
"paymium": ccxt.paymium,
"poloniex": ccxt.poloniex,
"qryptos": ccxt.qryptos,
"quadrigacx": ccxt.quadrigacx,
"quoinex": ccxt.quoinex,
"southxchange": ccxt.southxchange,
"surbitcoin": ccxt.surbitcoin,
"therock": ccxt.therock,
"tidex": ccxt.tidex,
"urdubit": ccxt.urdubit,
"vaultoro": ccxt.vaultoro,
"vbtc": ccxt.vbtc,
"virwox": ccxt.virwox,
"wex": ccxt.wex,
"xbtce": ccxt.xbtce,
"yobit": ccxt.yobit,
"yunbi": ccxt.yunbi,
"zaif": ccxt.zaif,
"zb": ccxt.zb
}
