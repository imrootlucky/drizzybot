import actionscoinbase

key = '38862b81fe15448a1242279edcb13180'
sec = 'I3rTOMLIcqNFrdGn/8HT2aVnHJH/n3bqu2F2aTJeUaiRUqoS7uf0YB8DJ20owVbXWE6n4l7tPJFTBrqJUQe57Q=='

api = actionscoinbase.setapi(key, sec, 'Hu0ch3!@#')

test = actionscoinbase.sellit('BTC-USD', .001, api)

print(test)