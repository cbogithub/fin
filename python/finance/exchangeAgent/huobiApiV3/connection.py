#!/usr/bin/env python
# -*- coding: utf-8 -*-

#import hashlib
import time
import urllib
#import urllib.parse
#import urllib.request

import system.pythonLib as pythonLib


class connectionOld:
    class cmd:
        ACCOUNT_INFO = "get_account_info"
        GET_ORDERS = "get_orders"
        ORDER_INFO = "order_info"
        BUY = "buy"
        BUY_MARKET = "buy_market"
        SELL = "sell"
        SELL_MARKET = "sell_market"        
        CANCEL_ORDER = "cancel_order"
        NEW_DEAL_ORDERS = "get_new_deal_orders"
        ORDER_ID_BY_TRADE_ID = "get_order_id_by_trade_id"


    class currency:
        CNY = 'cny'
        USD = 'usd'
        
    class commodity:
        BTC = 1
        LTC = 2

    marketUrl = {
        currency.CNY :
        {
            commodity.BTC :
            {
                "ticker" : "http://api.huobi.com/staticmarket/ticker_btc_json.js",
                "depth"  : "http://api.huobi.com/staticmarket/depth_btc_",
            },
            commodity.LTC :
            {
                "ticker" : "http://api.huobi.com/staticmarket/ticker_ltc_json.js",
                "depth"  : "http://api.huobi.com/staticmarket/depth_ltc_",
            }
        },
        currency.USD :
        {
            commodity.BTC :
            {
                "ticker" : "http://api.huobi.com/usdmarket/ticker_btc_json.js",
                "depth"  : "http://api.huobi.com/usdmarket/depth_btc_",
            }
        }
    }        

                
    def __init__(self, serviceApi="https://api.huobi.com/apiv3", accessKey='', secretKey=''):
        self.__serviceApi = serviceApi
        self.__accessKey  = accessKey
        self.__secretkey  = secretKey

        
    def send2api(self, pParams, extra):
        pParams['access_key'] = self.__accessKey
        pParams['created'] = int(time.time())
        pParams['sign'] = self.__createSign(pParams)
        if (extra):
            for k in extra:
                v = extra.get(k)
                if (v != None):
                    pParams[k] = v
                    # pParams.update(extra)
        return self.__httpRequest(self.__serviceApi, pParams)


    def __createSign(self, params):
        params['secret_key'] = self.__secretkey;
        params = sorted(params.items(), key=lambda d: d[0], reverse=False)
        return pythonLib.createSign(params)


    def __httpRequest(self, url, params):
#        return pythonLib.httpPost(url,params);
        return pythonLib.browserPost(url,params);
