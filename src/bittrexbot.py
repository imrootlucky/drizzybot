#from bittrex import bittrex
import actions
import time
api = bittrex('3b3bf8540d8f4104bb6f9883e1fb4f92', 'c0ef1bc3ea5a4dcd893c9a406127697b')


# from when using the other api
# def setapi(key, secret):
    # api = bittrex(key, secret)
    # return api

def getcurprice():
    summary = api.getmarketsummary(market)
    price = summary[0]['Last']
    print('got ', price, 'as price')
    print('--------------------------------------------')
    return price

def setsloss(boughtp):
    stloss = boughtp * ((100 - losslimit) / 100)
    return stloss

def setsell(boughtp):
    stsell = boughtp *((100 + gain) / 100)
    return stsell
    
    


# def buyit():
    # amount = tradelimit / cprice
    # print ('Buying {0} {1} for {2:.8f} {3}.'.format(amount, currency, cprice, trade))
    # api.buylimit(market, amount, cprice)
    # return amount

# def sellit(amount):
    # bal = api.getbalance(currency)
    # # amount = bal['Available']
    # print ('Selling {0} {1} for {2:.8f} {3}.'.format(amount, currency, cprice, trade))
    # api.selllimit(market, amount, cprice)

done = 0
bought = 0
round = 1





trade = input('Base market symbol?')
currency = input('Trade coin symbol?')
market = '{0}-{1}'.format(trade, currency)
csummary = api.getmarketsummary(market)
cprice = getcurprice()
mbalance = api.getbalance(trade)
print ('The price for {0} is {1:.8f} {2}.'.format(currency, cprice, trade))
print ('you have ', mbalance['Available'], trade, ' available')

btarget = api.getmarketsummary(market)[0]
print ('Last price is ', btarget['Last'], trade)
uselast = input('use last price for buy?(y/n) [default yes]')

if uselast == 'y' or uselast == 'Y':
    btarget = btarget['Last']
elif uselast == 'n':
    btarget = input('enter target price: ')
else:
    btarget = btarget['Last']
tradeavail = float(mbalance['Available'])
print(str(tradeavail) + trade + "availble for trading")
tradelimit = float(input('trade limit: '))
starget = float(btarget)
losslimit = float(input("stoploss percentage?: "))
gain = float(input('gain percentage to sell?: '))
takeprofit = starget

keepgoing = input('keep it up?(lower case y/n): ')

startingbalance = tradeavail


def startbot(btarget, round, trade, market):
    done = 0
    bought = 0
    while done == 0:
        print('round =', round)
        time.sleep(1)
        cprice = getcurprice()
        print('got price:', cprice)
        if cprice <= btarget and bought == 0:
            numberbought = buyit()
            boughtp  = cprice
            bought = 1
            sellprice = setsell(boughtp)
            stplss = setsloss(boughtp)
            round += 1
        elif cprice >= btarget and bought == 0:
            print('price is too high:', cprice)
    
        if cprice >= sellprice and bought == 1:
            sellit(numberbought)
            print ('PROFIT MET: selling for ', cprice)
            if keepgoing == 'n':
                done = 1
    
        if cprice <= stplss and bought == 1:
            sellit(numberbought)
            print ('STOPLOSS MET: selling for ', cprice)
            round += 1
            if keepgoing == 'n':
                done = 1

        else:
            #print('price is ', cprice)
            print('nothing')
            round += 1

startbot(cprice, round, trade, market)