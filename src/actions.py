import ccxt
import time
import sqlite3
import os, sys

#import cgi, cgitb
#cgitb.enable()

#define the database if using one, exchange, and pairs
#database = 'pingypong.db'
#exchange = 'bittrex'
pairtable = 'pairs'
pairindex = 0

#figure what to do
# form = cgi.FieldStorage()
# action = form.getfirst('action')
# price = float(form.getfirst('price'))
# perctg = float(form.getfirst('percentage'))
# trade = form.getfirst('trade').upper
# base = form.getfirst('base').upper
# market = trade + '/' + base

#args = sys.argv

#stealing args for tests
# action = args[0]
# price = float(args[1])
# perctg = float(args[2])
# trade = args[3].upper()
# base = args[4].upper()
# market = trade + '/' + base

# Connecting to the database file
# conn = sqlite3.connect(database)
# c = conn.cursor()

# #testing stuff I can't remember at all
# worker = []
# acct_limits = []
# acct_reserve = []

#get all the cryptopia accounts for the old pumpty program
# def getexinfo(connection, curs, exchange):
    # #pulls trade limits, api keys
    # curs.execute('SELECT * FROM ' + exchange)
    # exinfo = curs.fetchall()
    # return exinfo
    


#set up api coinbase

#set up api 



#set up api for ccxt 
def setapi(exchange, apikey, apisec):
    #pull api 
    
    
    
    if exchange == 'binance': #instantiate api
        worker = ccxt.binance({
        "apiKey": apikey,
        "secret": apisec,
        "enableRateLimit": True,
        })
        return worker
    
    
def setcbapi():
    return
    
def getcurprice(market, exchg):
    #print(exchg.fetchMarkets)
    price = exchg.fetch_ticker(market)
    # print('got ', price, 'as price')
    # print('--------------------------------------------')
    #print(price)
    return float(price['ask'])


    
def buyit(api, mkt, limit, reserve, cprice):
    base = mkt.split('/')[0]
    bal = float(api.fetchBalance()[base]['free'])
    test = bal - limit
    if test <= reserve:
        amount = 0
        print ("funds less than limit")
        return
    else:
        amount = (limit / cprice) #math for percentage buy over time removed.
        #print ('Buying {0} {1} for {2:.8f} {3}.'.format(amount, currency, cprice, trade))
        api.createMarketBuyOrder(mkt, amount)
        result = [amount, cprice]
        return result


#sells,  returns    
def sellit(api, mkt, amount):
    trade = mkt.split('/')[1]
    bal = float(api.fetchBalance()[trade]['free'])
    amount = bal * (percentage * 0.01)
    #print ('Selling {0} {1} for {2:.8f} {3}.'.format(amount, currency, cprice, trade))
    api.createMarketSellOrder(mkt, amount)
    result = [amount, cprice]
    return result
    
def setsloss(boughtp, losslimit):
    stloss = boughtp * ((100 - losslimit) / 100)
    return stloss

def setsell(boughtp, gain):
    stsell = boughtp *((100 + gain) / 100)
    return stsell
    
    
    
#set damn api)