import cbpro



def getcurprice(market):
    pub_client=cbpro.PublicClient()
    price = pub_client.get_product_ticker(product_id=market)
    print(price['price'])
    return price['price']
    
def setapi(key, secret, passp):
    auth_client = cbpro.AuthenticatedClient(key, secret, passp, api_url="https://api-public.sandbox.pro.coinbase.com")
    return auth_client
    
def buyit(market, amt, api):
    result = api.place_market_order(product_id=market,
                            side='buy',
                            funds=amt)
    
    print(result)
    return result               
                            
def sellit(market, amt, api):
    selling = api.place_market_order(product_id=market,
                            side='sell',
                            funds=amt)
    
    