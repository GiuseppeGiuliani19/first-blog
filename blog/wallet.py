from web3 import Web3

w3 = Web3(Web3.HTTPProvider('https://ropsten.infura.io/v3/5ce9ad5357d449778730d2fbad3d6de9'))
account = w3.eth.account.create()
privateKey = account.privateKey.hex()
address = account.address
print(f'Your address:{address} \n Your Key: {privateKey}')
# address = ''
# privateKey = ''
# nonce = w3.eth.getTransactionCount(address)
# gasPrice = w3.eth.gasPrice
# value = w3.towei(0, 'ether')
# signedTx = w3.eth.account.signTransaction(dict(
#     nonce=nonce,
#     gasPrice=gasPrice,
#     gas=100000,
#     to='0x0000000000000000000000000000000000000000',
#     value=value,
#     data=message.encode('utf-8')
# ), privateKey)