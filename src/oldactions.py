import ccxt
import time
import sqlite3
import os, sys

#import cgi, cgitb
#cgitb.enable()

#define the database if using one, exchange, and pairs
database = 'pingypong.db'
exchange = 'bittrex'
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

args = sys.argv

#stealing args for tests
action = args[0]
price = float(args[1])
perctg = float(args[2])
trade = args[3].upper()
base = args[4].upper()
market = trade + '/' + base

# Connecting to the database file
conn = sqlite3.connect(database)
c = conn.cursor()

# set up exchange api
exchg = setapi(conn, c)

#testing stuff I can't remember at all
worker = []
acct_limits = []
acct_reserve = []

#get all the cryptopia accounts for the old pumpty program
def getexinfo(connection, curs):
    #pulls trade limits, api keys
    curs.execute('SELECT * FROM ' + exchange)
    exinfo = curs.fetchall()
    return exinfo
    


#set up api
def setapi(connection, curs, exchange):
    #pull api 
    curs.execute('SELECT * FROM ' + exchange) #
    exinfo = curs.fetchall()
    dex = 0
    
    #make a list of accounts
    for account in exinfo:
        apikey = str(exinfo[dex][2])
        
        apisec =  str(exinfo[dex][3])
        
        #instantiate api
        worker.append(ccxt.cryptopia({
        "apiKey": apikey,
        "secret": apisec,
        "enableRateLimit": True,
        }))
        global acct_limits.append(float(exinfo[dex][1]))
        global acct_reserve.append(float(exinfo[dex][0]))
        dex += 1
    return worker
    
    
    
    
def getcurprice():

    price = exchg.fetch_ticker(market[pindex])['info']['Last']
    print('got ', price, 'as price')
    print('--------------------------------------------')
    return float(price)


    
def buyit(api, mkt, limit, reserve, cprice):
    bal = float(api.fetchBalance()[base]['free'])
    test = bal - limit
    if test <= reserve:
        amount = 0
        print ("funds less than limit")
        return
    else:
        amount = (limit / cprice) #math for percentage buy over time removed.
        #print ('Buying {0} {1} for {2:.8f} {3}.'.format(amount, currency, cprice, trade))
        api.createLimitBuyOrder(mkt, amount, cprice)
        return amount

def sellit(api, mkt, trade, amount, cprice):
    bal = float(api.fetchBalance()[trade]['free'])
    amount = bal * (percentage * 0.01)
    #print ('Selling {0} {1} for {2:.8f} {3}.'.format(amount, currency, cprice, trade))
    api.createLimitSellOrder(mkt, amount, cprice)
    
    
#when I ran the program here instead of as a strategy
# if action == 'buy':
    # dex = 0
    # for account in exchg:
        # buyit(account, market, acct_limits[dex], acct_reserve[dex], price)
    
# if action == 'sell':
    # for account in exchg:
        # sellit(account, market, trade, perctg, price)
