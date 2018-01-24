#!/usr/bin/env python
# -*- coding: utf-8 -*-


from system import object, log

financeLog = log.getStreamLogger('finance')

'''
abstract model
'''
class commodity:
    CNY = 'CNY'
    USD = 'USD'
    
    BTC = 'BTC'
    LTC = 'LTC'
    USDT = 'USDT'




class commodityPair:
    def __init__(self, base, quote):
        self.__base  = base
        self.__quote = quote

    def base():
        return self.__base
    
    def quote():
        return self.__quote

    def id(self):
        return self.__base.lower() + self.__quote.lower() 

    def symbol(self):
        return self.__base + "/" + self.__quote 


class position:
    def __init__(self, commodity, quantity):
        self.commodity = commodity
        self.quantity  = quantity

class positionExchange:
    def __init__(self, localPosition, remotePosition):
        self.local  = localPosition
        self.remote = remotePosition

class restrictDecimal:
    def __init__(self, precision=None, min=None, max=None):
        self.__precision  = precision
        self.__min        = min
        self.__max        = max
    
    def restrict(decimal):
        if(self.min and decima < self.min):
            decimal = self.min
        if(self.max and decimal > self.max):
            decimal = self.max
        if(self.precision):
            decimal = downRound(decimal, self.precision)
        return decimal

    def inRange(decimal):
        if(self.min and decimal < self.min):
            return False
        if(self.max and decial > self.max):
            return False
        return True
    
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
{
    'id':     'btcusd',   // string literal for referencing within an exchange
    'symbol': 'BTC/USD',  // uppercase string literal of a pair of currencies
    'base':   'BTC',      // uppercase string, base currency, 3 or more letters
    'quote':  'USD',      // uppercase string, quote currency, 3 or more letters
    'active': true,       // boolean, market status
    'precision': {        // number of decimal digits "after the dot"
        'price': 8,       // integer
        'amount': 8,      // integer
        'cost': 8,        // integer
    },
    'limits': {           // value limits when placing orders on this market
        'amount': {
            'min': 0.01,  // order amount should be > min
            'max': 1000,  // order amount should be < max
        },
        'price': { ... }, // same min/max limits for the price of the order
        'cost':  { ... }, // same limits for order cost = price * amount
    }
    'info':      { ... }, // the original unparsed market info from the exchange
}
'''
class market:
    def __init__(self, base, quote):
        self.__pair  = commodityPair(base, quote)
                
        self.price  = restrictDecimal()
        self.amount = restrictDecimal()
        self.cost   = restrictDecimal()

    def pair():
        return self.__pair
    
    def base():
        return self.__pair.base()
        
    def quote():
        return self.__pair.quote()

    def id(self):
        return self.__pair.id()

    def symbol(self):
        return self.__pair.symbol()

        
'''
{
    'id':   'exchange'                  // lowercase string exchange id
    'name': 'Exchange'                  // human-readable string
    'countries': [ 'US', 'CN', 'EU' ],  // string or array of ISO country codes
    'urls': {
        'api': 'https://api.example.com/data',  // string or dictionary of base API URLs
        'www': 'https://www.example.com'        // string website URL
        'doc': 'https://docs.example.com/api',  // string URL or array of URLs
    },
    'version':         'v1',            // string ending with digits
    'api':             { ... },         // dictionary of api endpoints
    'hasFetchTickers':  true,           // true if the exchange implements fetchTickers ()
    'hasFetchOHLCV':    false,          // true if the exchange implements fetchOHLCV ()
    'timeframes': {                     // empty if the exchange !hasFetchOHLCV
        '1m': '1minute',
        '1h': '1hour',
        '1d': '1day',
        '1M': '1month',
        '1y': '1year',
    },
    'timeout':          10000,          // number in milliseconds
    'rateLimit':        2000,           // number in milliseconds
    'userAgent':       'ccxt/1.1.1 ...' // string, HTTP User-Agent header
    'verbose':          false,          // boolean, output error details
    'markets':         { ... }          // dictionary of markets/pairs by symbol
    'symbols':         [ ... ]          // sorted list of string symbols (traded pairs)
    'currencies':      { ... }          // dictionary of currencies by currency code
    'markets_by_id':   { ... },         // dictionary of dictionaries (markets) by id
    'proxy': 'https://crossorigin.me/', // string URL
    'apiKey':   '92560ffae9b8a0421...', // string public apiKey (ASCII, hex, Base64, ...)
    'secret':   '9aHjPmW+EtRRKN/Oi...'  // string private secret key
    'password': '6kszf4aci8r',          // string password
    'uid':      '123456',               // string user id
}
'''
class exchange:
    KEY_RATE_LIMIT               = "rate_limit"
    KEY_SYMBOLS_PROFILE          = "symbols_profile"
    KEY_SYMBOLS_PRICE_PRECISION  = "price_precision"
    KEY_SYMBOLS_AMOUNT_PRECISION = "amount_precision"
    KEY_SYMBOLS_AMOUNT_MIN       = "amount_min"
    KEY_SYMBOLS_AMOUNT_MAX       = "amount_max"
    KEY_SYMBOLS_TRADE_COST_RATE  = "trade_cost_rate"
    
    def __init__(self, exchangeId="", param={}):
        self.__exchangeId = exchangeId

        # default config
        paramSet = {
            self.KEY_RATE_LIMIT      : 1,
            self.KEY_SYMBOLS_PROFILE : {}
        }

        # update
        object.dicUpdateByKeys(paramSet, param, paramSet.keys())        

        # set
        self.rateLimit      = paramSet[self.KEY_RATE_LIMIT]
        self.symbolsProfile = paramSet[self.KEY_SYMBOLS_PROFILE]

    # param
    def id(self):
        return self.__exchangeId
    def symbols(self):
        return None
    def markets(self):
        return None
       
    # public
    def loadMarkets(self):
        return None
    def fetchMarkets(self):
        return None
    def fetchTicker(self, symbol):
        return None
    def fetchTickers(self):
        return None
    def fetchOrderBook(self, symbol, params={}):
        return None
    def fetchL2OrderBook(self, symbol, params={}):
        return None        
    def fetchOHLCV(self):
        return None
    def fetchTrades(self, symbol, since=None, limit=None, params={}):
        return None

    # private
    def fetchBalance(self):
        return None
    def createOrder(self, symbol, type, side, amount, price=None, params={}):
        return None
    def createLimitBuyOrder(self, symbol, amount, price, params={}):
        return None
    def createLimitSellOrder(self, symbol, amount, price, params={}):
        return None
    def createMarketBuyOrder(self, symbol, amount, params={}):
        return None
    def createMarketSellOrder(self, symbol, amount, params={}):
        return None
    def cancelOrder(self, id, symbol=None, params={}):
        return None
    def fetchOrder(self, symbol=None, params={}):
        return None
    def fetchOpenOrders(self, symbol=None, params={}):
        return None
    def fetchClosedOrders(self, symbol=None, params={}):
        return None
'''
    |       loadMarkets            .           fetchBalance       |
    |       fetchMarkets           .            createOrder       |
    |       fetchTicker            .            cancelOrder       |
    |       fetchTickers           .             fetchOrder       |
    |       fetchOrderBook         .            fetchOrders       |
    |       fetchOHLCV             .        fetchOpenOrders       |
    |       fetchTrades            .      fetchClosedOrders       |
    |                              .          fetchMyTrades       |
    |                              .                deposit       |
    |                              .               withdraw       |
'''

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
        d1   = 24*h1
        w1   = 5*d1
        M1   = 4*w1
        y1   = 12*M1
        
    class Kline:
        def __init__(self):
            self.open  = 0
            self.close = 0
            self.low   = 0
            self.high  = 0 
        
class indicator:
    def __init__(self):
        pass

class policy:
    def __init__(self):
        pass
    
    def signal():
        pass
    
    def run():
        pass





