#!/usr/bin/env python
import json
import sys
import time
import ccxt

demo = True

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def beep():
    print "\a\a\a\a\a"

config = json.load(open('config.json'))

Base = config["Base"]
Quote= config["Quote"]
Pair = Base+'/'+Quote
	
profit_limit = config["profit_limit"]
single_trade_amount_limit_min = config["single_trade_amount_limit_min"]
single_trade_amount_limit_max = config["single_trade_amount_limit_max"]
base_amount_limit = config["base_amount_limit"]
profitmode = config["profitmode"]

def percentage(profit):
    if profit > profit_limit:
        return bcolors.OKGREEN + "%.2f" %(profit*100) + bcolors.ENDC
    else:
        return bcolors.FAIL + "%.2f" %(profit*100) + bcolors.ENDC
def f8(number):
    return "%.8f" %(number)
def n8f4(number):
    return "%8.4f" %(number)
def n10f4(number):
    return "%10.4f" %(number)
def n12f4(number):
    return "%12.4f" %(number)
def n8(number):
    return "%8d" %(number)
def adjust(amount):
    return (amount/5)*4

exchanges={
"bittrex": ccxt.bittrex,
"binance": ccxt.binance,
"huobipro": ccxt.huobipro,
"huobi": ccxt.huobi
}

#A = ccxt.bittrex(config["bittrex"])
#B = ccxt.binance(config["binance"])
ex1=config["exchange1"]
ex2=config["exchange2"]
A = exchanges[ex1](config[ex1]) 
B = exchanges[ex2](config[ex2]) 


A.load_markets()
B.load_markets()

balance_demo = {u'NEO': {'total': 0.0, 'used': 0.0, 'free': 0.0}, u'BAT': {'total': 0.0, 'used': 0.0, 'free': 0.0}, u'QASH': {'total': 0.0, 'used': 0.0, 'free': 0.0}, u'BCH': {'total': 0.0, 'used': 0.0, 'free': 0.0}, u'AIDOC': {'total': 0.0, 'used': 0.0, 'free': 0.0}, u'GNT': {'total': 0.0, 'used': 0.0, 'free': 0.0}, u'BT2': {'total': 0.0, 'used': 0.0, 'free': 0.0}, u'BCD': {'total': 0.0, 'used': 0.0, 'free': 0.0}, u'PAY': {'total': 0.0, 'used': 0.0, 'free': 0.0}, u'DTA': {'total': 0.0, 'used': 0.0, 'free': 0.0}, u'REQ': {'total': 0.0, 'used': 0.0, 'free': 0.0}, u'BIFI': {'total': 0.0, 'used': 0.0, 'free': 0.0}, u'XEM': {'total': 0.0, 'used': 0.0, 'free': 0.0}, u'EOS': {'total': 0.0, 'used': 0.0, 'free': 0.0}, u'ETC': {'total': 0.0, 'used': 0.0, 'free': 0.0}, u'RCN': {'total': 0.0, 'used': 0.0, 'free': 0.0}, 'used': {u'NEO': 0.0, u'BAT': 0.0, u'QASH': 0.0, u'BCH': 0.0, u'AIDOC': 0.0, u'GNT': 0.0, u'BT2': 0.0, u'BCD': 0.0, u'PAY': 0.0, u'GNX': 0.0, u'REQ': 0.0, u'BIFI': 0.0, u'EOS': 0.0, u'ETC': 0.0, u'RCN': 0.0, u'BCX': 0.0, u'CHAT': 0.0, u'ACT': 0.0, u'BT1': 0.0, u'ETH': 0.0, u'CMT': 0.0, u'TOPC': 0.0, u'IOST': 0.0, u'DAT': 0.0, u'DGD': 0.0, u'AST': 0.0, u'POWR': 0.0, u'QTUM': 0.0, u'XRP': 0.0, u'GAS': 0.0, u'OST': 0.0, u'CVC': 0.0, u'HSR': 0.0, u'MANA': 0.0, u'WICC': 0.0, u'BTG': 0.0, u'MDS': 0.0, u'APPC': 0.0, u'DTA': 0.0, u'TNT': 0.0, u'SMT': 0.0, u'BTC': 0.0, u'SWFTC': 0.0, u'SALT': 0.0, u'UTK': 0.0, u'ELF': 0.0, u'KNC': 0.0, u'ADX': 0.0, u'ZRX': 0.0, u'DASH': 0.0, u'STORJ': 0.0, u'ICX': 0.0, u'ETF': 0.0, u'MTL': 0.0, u'WAX': 0.0, u'VEN': 0.0, u'THETA': 0.0, u'RDN': 0.0, u'USDT': 0.0, u'PROPY': 0.0, u'MCO': 0.0, u'ZEC': 0.0, u'OMG': 0.0, u'EVX': 0.0, u'NAS': 0.0, u'XEM': 0.0, u'DBC': 0.0, u'YEE': 0.0, u'ITC': 0.0, u'LTC': 0.0, u'SBTC': 0.0, u'SNT': 0.0, u'QSP': 0.0, u'LET': 0.0, u'TNB': 0.0, u'RPX': 0.0, u'BTM': 0.0, u'LINK': 0.0, u'QUN': 0.0}, u'BCX': {'total': 0.0, 'used': 0.0, 'free': 0.0}, u'CHAT': {'total': 0.0, 'used': 0.0, 'free': 0.0}, u'ACT': {'total': 0.0, 'used': 0.0, 'free': 0.0}, u'BT1': {'total': 0.0, 'used': 0.0, 'free': 0.0}, u'ETH': {'total': 0.0, 'used': 0.0, 'free': 0.0}, u'CMT': {'total': 0.0, 'used': 0.0, 'free': 0.0}, u'TOPC': {'total': 0.0, 'used': 0.0, 'free': 0.0}, u'CVC': {'total': 0.0, 'used': 0.0, 'free': 0.0}, u'HSR': {'total': 0.0, 'used': 0.0, 'free': 0.0}, u'WAX': {'total': 0.0, 'used': 0.0, 'free': 0.0}, 'total': {u'NEO': 0.0, u'BAT': 0.0, u'QASH': 0.0, u'BCH': 0.0, u'AIDOC': 0.0, u'GNT': 0.0, u'BT2': 0.0, u'BCD': 0.0, u'PAY': 0.0, u'GNX': 0.0, u'REQ': 0.0, u'BIFI': 0.0, u'EOS': 0.0, u'ETC': 0.0, u'RCN': 0.0, u'BCX': 0.0, u'CHAT': 0.0, u'ACT': 0.0, u'BT1': 0.0, u'ETH': 0.0, u'CMT': 0.0, u'TOPC': 0.0, u'IOST': 0.0, u'DAT': 0.0, u'DGD': 0.0, u'AST': 0.0, u'POWR': 0.0, u'QTUM': 0.0, u'XRP': 0.0, u'GAS': 0.0, u'OST': 0.0, u'CVC': 0.0, u'HSR': 0.0, u'MANA': 0.0, u'WICC': 0.0, u'BTG': 0.0, u'MDS': 0.0, u'APPC': 0.0, u'DTA': 0.0, u'TNT': 0.0, u'SMT': 0.0, u'BTC': 0.0, u'SWFTC': 0.0, u'SALT': 0.0, u'UTK': 0.0, u'ELF': 0.0, u'KNC': 0.0, u'ADX': 0.0, u'ZRX': 0.0, u'DASH': 0.0, u'STORJ': 0.0, u'ICX': 0.0, u'ETF': 0.0, u'MTL': 0.0, u'WAX': 0.0, u'VEN': 0.0, u'THETA': 0.0, u'RDN': 0.0, u'USDT': 0.0, u'PROPY': 0.0, u'MCO': 0.0, u'ZEC': 0.0, u'OMG': 0.0, u'EVX': 0.0, u'NAS': 0.0, u'XEM': 0.0, u'DBC': 0.0, u'YEE': 0.0, u'ITC': 0.0, u'LTC': 0.0, u'SBTC': 0.0, u'SNT': 0.0, u'QSP': 0.0, u'LET': 0.0, u'TNB': 0.0, u'RPX': 0.0, u'BTM': 0.0, u'LINK': 0.0, u'QUN': 0.0}, u'DGD': {'total': 0.0, 'used': 0.0, 'free': 0.0}, u'AST': {'total': 0.0, 'used': 0.0, 'free': 0.0}, u'POWR': {'total': 0.0, 'used': 0.0, 'free': 0.0}, u'QTUM': {'total': 0.0, 'used': 0.0, 'free': 0.0}, u'XRP': {'total': 0.0, 'used': 0.0, 'free': 0.0}, u'GAS': {'total': 0.0, 'used': 0.0, 'free': 0.0}, u'OST': {'total': 0.0, 'used': 0.0, 'free': 0.0}, u'IOST': {'total': 0.0, 'used': 0.0, 'free': 0.0}, u'DAT': {'total': 0.0, 'used': 0.0, 'free': 0.0}, u'MANA': {'total': 0.0, 'used': 0.0, 'free': 0.0}, u'WICC': {'total': 0.0, 'used': 0.0, 'free': 0.0}, u'MDS': {'total': 0.0, 'used': 0.0, 'free': 0.0}, u'APPC': {'total': 0.0, 'used': 0.0, 'free': 0.0}, u'GNX': {'total': 0.0, 'used': 0.0, 'free': 0.0}, u'MCO': {'total': 0.0, 'used': 0.0, 'free': 0.0}, u'SMT': {'total': 0.0, 'used': 0.0, 'free': 0.0}, u'SWFTC': {'total': 0.0, 'used': 0.0, 'free': 0.0}, u'ZEC': {'total': 0.0, 'used': 0.0, 'free': 0.0}, u'UTK': {'total': 0.0, 'used': 0.0, 'free': 0.0}, u'ELF': {'total': 0.0, 'used': 0.0, 'free': 0.0}, u'KNC': {'total': 0.0, 'used': 0.0, 'free': 0.0}, u'ADX': {'total': 0.0, 'used': 0.0, 'free': 0.0}, u'ZRX': {'total': 0.0, 'used': 0.0, 'free': 0.0}, u'DASH': {'total': 0.0, 'used': 0.0, 'free': 0.0}, u'STORJ': {'total': 0.0, 'used': 0.0, 'free': 0.0}, u'ICX': {'total': 0.0, 'used': 0.0, 'free': 0.0}, 'free': {u'NEO': 0.0, u'BAT': 0.0, u'QASH': 0.0, u'BCH': 0.0, u'AIDOC': 0.0, u'GNT': 0.0, u'BT2': 0.0, u'BCD': 0.0, u'PAY': 0.0, u'GNX': 0.0, u'REQ': 0.0, u'BIFI': 0.0, u'EOS': 0.0, u'ETC': 0.0, u'RCN': 0.0, u'BCX': 0.0, u'CHAT': 0.0, u'ACT': 0.0, u'BT1': 0.0, u'ETH': 0.0, u'CMT': 0.0, u'TOPC': 0.0, u'IOST': 0.0, u'DAT': 0.0, u'DGD': 0.0, u'AST': 0.0, u'POWR': 0.0, u'QTUM': 0.0, u'XRP': 0.0, u'GAS': 0.0, u'OST': 0.0, u'CVC': 0.0, u'HSR': 0.0, u'MANA': 0.0, u'WICC': 0.0, u'BTG': 0.0, u'MDS': 0.0, u'APPC': 0.0, u'DTA': 0.0, u'TNT': 0.0, u'SMT': 0.0, u'BTC': 0.0, u'SWFTC': 0.0, u'SALT': 0.0, u'UTK': 0.0, u'ELF': 0.0, u'KNC': 0.0, u'ADX': 0.0, u'ZRX': 0.0, u'DASH': 0.0, u'STORJ': 0.0, u'ICX': 0.0, u'ETF': 0.0, u'MTL': 0.0, u'WAX': 0.0, u'VEN': 0.0, u'THETA': 0.0, u'RDN': 0.0, u'USDT': 0.0, u'PROPY': 0.0, u'MCO': 0.0, u'ZEC': 0.0, u'OMG': 0.0, u'EVX': 0.0, u'NAS': 0.0, u'XEM': 0.0, u'DBC': 0.0, u'YEE': 0.0, u'ITC': 0.0, u'LTC': 0.0, u'SBTC': 0.0, u'SNT': 0.0, u'QSP': 0.0, u'LET': 0.0, u'TNB': 0.0, u'RPX': 0.0, u'BTM': 0.0, u'LINK': 0.0, u'QUN': 0.0}, u'MTL': {'total': 0.0, 'used': 0.0, 'free': 0.0}, u'TNB': {'total': 0.0, 'used': 0.0, 'free': 0.0}, u'VEN': {'total': 0.0, 'used': 0.0, 'free': 0.0}, u'THETA': {'total': 0.0, 'used': 0.0, 'free': 0.0}, u'RDN': {'total': 0.0, 'used': 0.0, 'free': 0.0}, u'USDT': {'total': 0.0, 'used': 0.0, 'free': 0.0}, u'PROPY': {'total': 0.0, 'used': 0.0, 'free': 0.0}, 'info': {u'status': u'ok', u'data': {u'list': [{u'currency': u'act', u'balance': u'0.000000000000000000', u'type': u'trade'}, {u'currency': u'act', u'balance': u'0.000000000000000000', u'type': u'frozen'}, {u'currency': u'adx', u'balance': u'0.000000000000000000', u'type': u'trade'}, {u'currency': u'adx', u'balance': u'0.000000000000000000', u'type': u'frozen'}, {u'currency': u'aidoc', u'balance': u'0.000000000000000000', u'type': u'trade'}, {u'currency': u'aidoc', u'balance': u'0.000000000000000000', u'type': u'frozen'}, {u'currency': u'appc', u'balance': u'0.000000000000000000', u'type': u'trade'}, {u'currency': u'appc', u'balance': u'0.000000000000000000', u'type': u'frozen'}, {u'currency': u'ast', u'balance': u'0.000000000000000000', u'type': u'trade'}, {u'currency': u'ast', u'balance': u'0.000000000000000000', u'type': u'frozen'}, {u'currency': u'bat', u'balance': u'0.000000000000000000', u'type': u'trade'}, {u'currency': u'bat', u'balance': u'0.000000000000000000', u'type': u'frozen'}, {u'currency': u'bch', u'balance': u'0.000000000000000000', u'type': u'trade'}, {u'currency': u'bch', u'balance': u'0.000000000000000000', u'type': u'frozen'}, {u'currency': u'bcd', u'balance': u'0.000000000000000000', u'type': u'trade'}, {u'currency': u'bcd', u'balance': u'0.000000000000000000', u'type': u'frozen'}, {u'currency': u'bcx', u'balance': u'0.000000000000000000', u'type': u'trade'}, {u'currency': u'bcx', u'balance': u'0.000000000000000000', u'type': u'frozen'}, {u'currency': u'bifi', u'balance': u'0.000000000000000000', u'type': u'trade'}, {u'currency': u'bifi', u'balance': u'0.000000000000000000', u'type': u'frozen'}, {u'currency': u'bt1', u'balance': u'0.000000000000000000', u'type': u'trade'}, {u'currency': u'bt1', u'balance': u'0.000000000000000000', u'type': u'frozen'}, {u'currency': u'bt2', u'balance': u'0.000000000000000000', u'type': u'trade'}, {u'currency': u'bt2', u'balance': u'0.000000000000000000', u'type': u'frozen'}, {u'currency': u'btc', u'balance': u'0.000000000000000000', u'type': u'trade'}, {u'currency': u'btc', u'balance': u'0.000000000000000000', u'type': u'frozen'}, {u'currency': u'btg', u'balance': u'0.000000000000000000', u'type': u'trade'}, {u'currency': u'btg', u'balance': u'0.000000000000000000', u'type': u'frozen'}, {u'currency': u'btm', u'balance': u'0.000000000000000000', u'type': u'trade'}, {u'currency': u'btm', u'balance': u'0.000000000000000000', u'type': u'frozen'}, {u'currency': u'chat', u'balance': u'0.000000000000000000', u'type': u'trade'}, {u'currency': u'chat', u'balance': u'0.000000000000000000', u'type': u'frozen'}, {u'currency': u'cmt', u'balance': u'0.000000000000000000', u'type': u'trade'}, {u'currency': u'cmt', u'balance': u'0.000000000000000000', u'type': u'frozen'}, {u'currency': u'cvc', u'balance': u'0.000000000000000000', u'type': u'trade'}, {u'currency': u'cvc', u'balance': u'0.000000000000000000', u'type': u'frozen'}, {u'currency': u'dash', u'balance': u'0.000000000000000000', u'type': u'trade'}, {u'currency': u'dash', u'balance': u'0.000000000000000000', u'type': u'frozen'}, {u'currency': u'dat', u'balance': u'0.000000000000000000', u'type': u'trade'}, {u'currency': u'dat', u'balance': u'0.000000000000000000', u'type': u'frozen'}, {u'currency': u'dbc', u'balance': u'0.000000000000000000', u'type': u'trade'}, {u'currency': u'dbc', u'balance': u'0.000000000000000000', u'type': u'frozen'}, {u'currency': u'dgd', u'balance': u'0.000000000000000000', u'type': u'trade'}, {u'currency': u'dgd', u'balance': u'0.000000000000000000', u'type': u'frozen'}, {u'currency': u'dta', u'balance': u'0.000000000000000000', u'type': u'trade'}, {u'currency': u'dta', u'balance': u'0.000000000000000000', u'type': u'frozen'}, {u'currency': u'elf', u'balance': u'0.000000000000000000', u'type': u'trade'}, {u'currency': u'elf', u'balance': u'0.000000000000000000', u'type': u'frozen'}, {u'currency': u'eos', u'balance': u'0.000000000000000000', u'type': u'trade'}, {u'currency': u'eos', u'balance': u'0.000000000000000000', u'type': u'frozen'}, {u'currency': u'etc', u'balance': u'0.000000000000000000', u'type': u'trade'}, {u'currency': u'etc', u'balance': u'0.000000000000000000', u'type': u'frozen'}, {u'currency': u'etf', u'balance': u'0.000000000000000000', u'type': u'trade'}, {u'currency': u'etf', u'balance': u'0.000000000000000000', u'type': u'frozen'}, {u'currency': u'eth', u'balance': u'0.000000000000000000', u'type': u'trade'}, {u'currency': u'eth', u'balance': u'0.000000000000000000', u'type': u'frozen'}, {u'currency': u'evx', u'balance': u'0.000000000000000000', u'type': u'trade'}, {u'currency': u'evx', u'balance': u'0.000000000000000000', u'type': u'frozen'}, {u'currency': u'gas', u'balance': u'0.000000000000000000', u'type': u'trade'}, {u'currency': u'gas', u'balance': u'0.000000000000000000', u'type': u'frozen'}, {u'currency': u'gnt', u'balance': u'0.000000000000000000', u'type': u'trade'}, {u'currency': u'gnt', u'balance': u'0.000000000000000000', u'type': u'frozen'}, {u'currency': u'gnx', u'balance': u'0.000000000000000000', u'type': u'trade'}, {u'currency': u'gnx', u'balance': u'0.000000000000000000', u'type': u'frozen'}, {u'currency': u'hsr', u'balance': u'0.000000000000000000', u'type': u'trade'}, {u'currency': u'hsr', u'balance': u'0.000000000000000000', u'type': u'frozen'}, {u'currency': u'icx', u'balance': u'0.000000000000000000', u'type': u'trade'}, {u'currency': u'icx', u'balance': u'0.000000000000000000', u'type': u'frozen'}, {u'currency': u'iost', u'balance': u'0.000000000000000000', u'type': u'trade'}, {u'currency': u'iost', u'balance': u'0.000000000000000000', u'type': u'frozen'}, {u'currency': u'itc', u'balance': u'0.000000000000000000', u'type': u'trade'}, {u'currency': u'itc', u'balance': u'0.000000000000000000', u'type': u'frozen'}, {u'currency': u'knc', u'balance': u'0.000000000000000000', u'type': u'trade'}, {u'currency': u'knc', u'balance': u'0.000000000000000000', u'type': u'frozen'}, {u'currency': u'let', u'balance': u'0.000000000000000000', u'type': u'trade'}, {u'currency': u'let', u'balance': u'0.000000000000000000', u'type': u'frozen'}, {u'currency': u'link', u'balance': u'0.000000000000000000', u'type': u'trade'}, {u'currency': u'link', u'balance': u'0.000000000000000000', u'type': u'frozen'}, {u'currency': u'ltc', u'balance': u'0.000000000000000000', u'type': u'trade'}, {u'currency': u'ltc', u'balance': u'0.000000000000000000', u'type': u'frozen'}, {u'currency': u'mana', u'balance': u'0.000000000000000000', u'type': u'trade'}, {u'currency': u'mana', u'balance': u'0.000000000000000000', u'type': u'frozen'}, {u'currency': u'mco', u'balance': u'0.000000000000000000', u'type': u'trade'}, {u'currency': u'mco', u'balance': u'0.000000000000000000', u'type': u'frozen'}, {u'currency': u'mds', u'balance': u'0.000000000000000000', u'type': u'trade'}, {u'currency': u'mds', u'balance': u'0.000000000000000000', u'type': u'frozen'}, {u'currency': u'mtl', u'balance': u'0.000000000000000000', u'type': u'trade'}, {u'currency': u'mtl', u'balance': u'0.000000000000000000', u'type': u'frozen'}, {u'currency': u'nas', u'balance': u'0.000000000000000000', u'type': u'trade'}, {u'currency': u'nas', u'balance': u'0.000000000000000000', u'type': u'frozen'}, {u'currency': u'neo', u'balance': u'0.000000000000000000', u'type': u'trade'}, {u'currency': u'neo', u'balance': u'0.000000000000000000', u'type': u'frozen'}, {u'currency': u'omg', u'balance': u'0.000000000000000000', u'type': u'trade'}, {u'currency': u'omg', u'balance': u'0.000000000000000000', u'type': u'frozen'}, {u'currency': u'ost', u'balance': u'0.000000000000000000', u'type': u'trade'}, {u'currency': u'ost', u'balance': u'0.000000000000000000', u'type': u'frozen'}, {u'currency': u'pay', u'balance': u'0.000000000000000000', u'type': u'trade'}, {u'currency': u'pay', u'balance': u'0.000000000000000000', u'type': u'frozen'}, {u'currency': u'powr', u'balance': u'0.000000000000000000', u'type': u'trade'}, {u'currency': u'powr', u'balance': u'0.000000000000000000', u'type': u'frozen'}, {u'currency': u'propy', u'balance': u'0.000000000000000000', u'type': u'trade'}, {u'currency': u'propy', u'balance': u'0.000000000000000000', u'type': u'frozen'}, {u'currency': u'qash', u'balance': u'0.000000000000000000', u'type': u'trade'}, {u'currency': u'qash', u'balance': u'0.000000000000000000', u'type': u'frozen'}, {u'currency': u'qsp', u'balance': u'0.000000000000000000', u'type': u'trade'}, {u'currency': u'qsp', u'balance': u'0.000000000000000000', u'type': u'frozen'}, {u'currency': u'qtum', u'balance': u'0.000000000000000000', u'type': u'trade'}, {u'currency': u'qtum', u'balance': u'0.000000000000000000', u'type': u'frozen'}, {u'currency': u'qun', u'balance': u'0.000000000000000000', u'type': u'trade'}, {u'currency': u'qun', u'balance': u'0.000000000000000000', u'type': u'frozen'}, {u'currency': u'rcn', u'balance': u'0.000000000000000000', u'type': u'trade'}, {u'currency': u'rcn', u'balance': u'0.000000000000000000', u'type': u'frozen'}, {u'currency': u'rdn', u'balance': u'0.000000000000000000', u'type': u'trade'}, {u'currency': u'rdn', u'balance': u'0.000000000000000000', u'type': u'frozen'}, {u'currency': u'req', u'balance': u'0.000000000000000000', u'type': u'trade'}, {u'currency': u'req', u'balance': u'0.000000000000000000', u'type': u'frozen'}, {u'currency': u'rpx', u'balance': u'0.000000000000000000', u'type': u'trade'}, {u'currency': u'rpx', u'balance': u'0.000000000000000000', u'type': u'frozen'}, {u'currency': u'salt', u'balance': u'0.000000000000000000', u'type': u'trade'}, {u'currency': u'salt', u'balance': u'0.000000000000000000', u'type': u'frozen'}, {u'currency': u'sbtc', u'balance': u'0.000000000000000000', u'type': u'trade'}, {u'currency': u'sbtc', u'balance': u'0.000000000000000000', u'type': u'frozen'}, {u'currency': u'smt', u'balance': u'0.000000000000000000', u'type': u'trade'}, {u'currency': u'smt', u'balance': u'0.000000000000000000', u'type': u'frozen'}, {u'currency': u'snt', u'balance': u'0.000000000000000000', u'type': u'trade'}, {u'currency': u'snt', u'balance': u'0.000000000000000000', u'type': u'frozen'}, {u'currency': u'storj', u'balance': u'0.000000000000000000', u'type': u'trade'}, {u'currency': u'storj', u'balance': u'0.000000000000000000', u'type': u'frozen'}, {u'currency': u'swftc', u'balance': u'0.000000000000000000', u'type': u'trade'}, {u'currency': u'swftc', u'balance': u'0.000000000000000000', u'type': u'frozen'}, {u'currency': u'theta', u'balance': u'0.000000000000000000', u'type': u'trade'}, {u'currency': u'theta', u'balance': u'0.000000000000000000', u'type': u'frozen'}, {u'currency': u'tnb', u'balance': u'0.000000000000000000', u'type': u'trade'}, {u'currency': u'tnb', u'balance': u'0.000000000000000000', u'type': u'frozen'}, {u'currency': u'tnt', u'balance': u'0.000000000000000000', u'type': u'trade'}, {u'currency': u'tnt', u'balance': u'0.000000000000000000', u'type': u'frozen'}, {u'currency': u'topc', u'balance': u'0.000000000000000000', u'type': u'trade'}, {u'currency': u'topc', u'balance': u'0.000000000000000000', u'type': u'frozen'}, {u'currency': u'usdt', u'balance': u'0.000000000000000000', u'type': u'trade'}, {u'currency': u'usdt', u'balance': u'0.000000000000000000', u'type': u'frozen'}, {u'currency': u'utk', u'balance': u'0.000000000000000000', u'type': u'trade'}, {u'currency': u'utk', u'balance': u'0.000000000000000000', u'type': u'frozen'}, {u'currency': u'ven', u'balance': u'0.000000000000000000', u'type': u'trade'}, {u'currency': u'ven', u'balance': u'0.000000000000000000', u'type': u'frozen'}, {u'currency': u'wax', u'balance': u'0.000000000000000000', u'type': u'trade'}, {u'currency': u'wax', u'balance': u'0.000000000000000000', u'type': u'frozen'}, {u'currency': u'wicc', u'balance': u'0.000000000000000000', u'type': u'trade'}, {u'currency': u'wicc', u'balance': u'0.000000000000000000', u'type': u'frozen'}, {u'currency': u'xem', u'balance': u'0.000000000000000000', u'type': u'trade'}, {u'currency': u'xem', u'balance': u'0.000000000000000000', u'type': u'frozen'}, {u'currency': u'xrp', u'balance': u'0.000000000000000000', u'type': u'trade'}, {u'currency': u'xrp', u'balance': u'0.000000000000000000', u'type': u'frozen'}, {u'currency': u'yee', u'balance': u'0.000000000000000000', u'type': u'trade'}, {u'currency': u'yee', u'balance': u'0.000000000000000000', u'type': u'frozen'}, {u'currency': u'zec', u'balance': u'0.000000000000000000', u'type': u'trade'}, {u'currency': u'zec', u'balance': u'0.000000000000000000', u'type': u'frozen'}, {u'currency': u'zrx', u'balance': u'0.000000000000000000', u'type': u'trade'}, {u'currency': u'zrx', u'balance': u'0.000000000000000000', u'type': u'frozen'}], u'state': u'working', u'type': u'spot', u'id': 1351771}}, u'EVX': {'total': 0.0, 'used': 0.0, 'free': 0.0}, u'TNT': {'total': 0.0, 'used': 0.0, 'free': 0.0}, u'OMG': {'total': 0.0, 'used': 0.0, 'free': 0.0}, u'SNT': {'total': 0.0, 'used': 0.0, 'free': 0.0}, u'NAS': {'total': 0.0, 'used': 0.0, 'free': 0.0}, u'SALT': {'total': 0.0, 'used': 0.0, 'free': 0.0}, u'DBC': {'total': 0.0, 'used': 0.0, 'free': 0.0}, u'YEE': {'total': 0.0, 'used': 0.0, 'free': 0.0}, u'ITC': {'total': 0.0, 'used': 0.0, 'free': 0.0}, u'LINK': {'total': 0.0, 'used': 0.0, 'free': 0.0}, u'LTC': {'total': 0.0, 'used': 0.0, 'free': 0.0}, u'SBTC': {'total': 0.0, 'used': 0.0, 'free': 0.0}, u'BTG': {'total': 0.0, 'used': 0.0, 'free': 0.0}, u'QSP': {'total': 0.0, 'used': 0.0, 'free': 0.0}, u'LET': {'total': 0.0, 'used': 0.0, 'free': 0.0}, u'BTC': {'total': 0.0, 'used': 0.0, 'free': 0.0}, u'RPX': {'total': 0.0, 'used': 0.0, 'free': 0.0}, u'BTM': {'total': 0.0, 'used': 0.0, 'free': 0.0}, u'ETF': {'total': 0.0, 'used': 0.0, 'free': 0.0}, u'QUN': {'total': 0.0, 'used': 0.0, 'free': 0.0}}

if(demo):
    balance_A = balance_demo 
else:
    balance_A = A.fetchBalance()

print A.id, Quote, n12f4(balance_A[Quote]['free'])
print A.id, Base,  n12f4(balance_A[Base]['free'])

if(demo):
    balance_B = balance_demo 
else:
    balance_B = B.fetchBalance()
print B.id, Quote, n12f4(balance_B[Quote]['free'])
print B.id, Base,  n12f4(balance_B[Base]['free'])

balance_start = balance_B[Quote]['total'] + balance_A[Quote]['total']
balance_quote_mark = balance_start
balance_base_amount = balance_B[Base]['total'] + balance_A[Base]['total']

retry = 0
hit = 0
restart = 0
delay = 1 # seconds
while True:
    print ""
    print('------------------------------------------------------------')
    retry = retry + 1
    time.sleep(delay) # rate limit
    print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), "Retry", retry, "Hitted", hit,
          "Restart", restart, "Profit", balance_quote_mark - balance_start)
    if balance_base_amount > base_amount_limit:
        print Base, "buy too much", balance_base_amount
        continue
    try:
        order_book_A = A.fetch_order_book(Pair)
        bid0_price_A = order_book_A['bids'][0][0]
        bid0_amount_A = order_book_A['bids'][0][1]
        if bid0_amount_A < single_trade_amount_limit_min:
            bid0_price_A = order_book_A['bids'][1][0]
            bid0_amount_A = order_book_A['bids'][1][1]
        ask0_price_A = order_book_A['asks'][0][0]
        ask0_amount_A = order_book_A['asks'][0][1]
        if ask0_amount_A < single_trade_amount_limit_min:
            ask0_price_A = order_book_A['asks'][1][0]
            ask0_amount_A = order_book_A['asks'][1][1]
        print A.id, "bid: ", f8(bid0_price_A), " amount: ", n12f4(bid0_amount_A)
        print A.id, "ask: ", f8(ask0_price_A), " amount: ", n12f4(ask0_amount_A)


        print "----- 1"
        order_book_B = B.fetch_order_book(Pair)
        
        print "----- 1.1"
        bid0_price_B = order_book_B['bids'][0][0]
        bid0_amount_B = order_book_B['bids'][0][1]
        if bid0_amount_B < single_trade_amount_limit_min:
            bid0_price_B = order_book_B['bids'][1][0]
            bid0_amount_B = order_book_B['bids'][1][1]
        ask0_price_B = order_book_B['asks'][0][0]
        ask0_amount_B = order_book_B['asks'][0][1]
        if ask0_amount_B < single_trade_amount_limit_min:
            ask0_price_B = order_book_B['asks'][1][0]
            ask0_amount_B = order_book_B['asks'][1][1]

        print B.id, "bid: ", f8(bid0_price_B), " amount: ", n12f4(bid0_amount_B)
        print B.id, "ask: ", f8(ask0_price_B), " amount: ", n12f4(ask0_amount_B)

        bid_available_A = balance_A[Quote]['free']/ask0_price_A
        ask_available_A = balance_A[Base]['free']
        bid_available_B = balance_B[Quote]['free']/ask0_price_B
        ask_available_B = balance_B[Base]['free']

        AbidBask_amount = int(min(ask0_amount_A, bid0_amount_B, bid_available_A, ask_available_B, single_trade_amount_limit_max))
        AbidBask_amount = adjust(AbidBask_amount)
        AaskBbid_amount = int(min(bid0_amount_A, ask0_amount_B, ask_available_A, bid_available_B, single_trade_amount_limit_max))
        AaskBbid_amount = adjust(AaskBbid_amount)
        AbidBask_profit = (bid0_price_B - ask0_price_A)/ask0_price_A
        AaskBbid_profit = (bid0_price_A - ask0_price_B)/ask0_price_B

        print "========================================================="
        print A.id, "to", B.id, "profit: ", percentage(AbidBask_profit)
        print B.id, "to", A.id, "profit: ", percentage(AaskBbid_profit)
        if profitmode != 1:
            continue
        if AbidBask_profit > profit_limit and AbidBask_amount > single_trade_amount_limit_min:
            hit = hit + 1
            beep()
            print "!!!!!! exchange amount: ", AbidBask_amount
            if(not demo):
                Abid = A.createLimitBuyOrder(Pair, AbidBask_amount, ask0_price_A)
                Bask = B.createLimitSellOrder(Pair, AbidBask_amount, bid0_price_B)
            print hit, "times", A.id, "bid", B.id, "ask", " amount:", AbidBask_amount

        if AaskBbid_profit > profit_limit and AaskBbid_amount > single_trade_amount_limit_min:
            hit = hit + 1
            beep()
            print "!!!!!! exchange amount: ", AaskBbid_amount
            if(not demo):
                Bbid = B.createLimitBuyOrder(Pair, AaskBbid_amount, ask0_price_B)
                Aask = A.createLimitSellOrder(Pair, AaskBbid_amount, bid0_price_A)
            print hit, "times", A.id, "ask", B.id, "bid", " amount:", AaskBbid_amount
            print Bbid

        if(not demo):
            balance_A = A.fetchBalance()
            balance_B = B.fetchBalance()
        print "========================================================="
        print A.id, "open order: "
        if(not demo):
            for i in A.fetchOpenOrders(symbol=Pair):
                print "Remaing: ", n12f4(i['remaining']), "Limit: ", f8(i['price'])
            print B.id, "open order: "
            for i in B.fetchOpenOrders(symbol=Pair):
                print "Remaing: ", n12f4(i['remaining']), "Limit: ", f8(i['price'])
        print "========================================================="
        print ex1, Quote, "free: ", n8f4(balance_A[Quote]['free']), "used: ", n8f4(balance_A[Quote]['used'])
        print ex2, Quote, "free: ", n8f4(balance_B[Quote]['free']), "used: ", n8f4(balance_B[Quote]['used'])
        print "Total:            ", n8f4(balance_B[Quote]['total'] + balance_A[Quote]['total'])
        print "========================================================="
        print ex1, Base, "free: ", n8(balance_A[Base]['free']), "used: ", n8(balance_A[Base]['used'])
        print ex2, Base, "free: ", n8(balance_B[Base]['free']), "used: ", n8(balance_B[Base]['used'])
        print "Total:            ", n8(balance_B[Base]['total'] + balance_A[Base]['total'])
        print "========================================================="
        balance_quote_mark = balance_B[Quote]['total'] + balance_A[Quote]['total']
        balance_base_amount = balance_B[Base]['total'] + balance_A[Base]['total']

    except:
        print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), "oops... restarting")

        restart = restart + 1
        ex1=config["exchange1"]
        ex2=config["exchange2"]
        A = exchanges[ex1](config[ex1])
        B = exchanges[ex2](config[ex2])

        #A = ccxt.bittrex(config["bittrex"])
        #B = ccxt.binance(config["binance"])

        A.load_markets()
        B.load_markets()

        if(demo):
            balance_A = balance_demo
            balance_B = balance_demo
        else:
            balance_A = A.fetchBalance()
            balance_B = B.fetchBalance()

        pass




