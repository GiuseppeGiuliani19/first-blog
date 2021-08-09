from web3 import Web3
import json
import redis

#funzione che serve ad effettuare la transazione alla ropsten di ethereum
def sendTransaction(message):
    w3 = Web3(Web3.HTTPProvider('https://ropsten.infura.io/v3/5ce9ad5357d449778730d2fbad3d6de9'))
    address = '0x14Abd6b1F5E659c715600102C2D31f27BDfAc845'
    privateKey = '0x23e4b274ebe4b8db1c50810759c4ee8279bbb558659cb52143a6276bb58511c7'
    nonce = w3.eth.getTransactionCount(address)
    gasPrice = w3.eth.gasPrice
    value = w3.toWei(0, 'ether')
    signedTx = w3.eth.account.signTransaction(dict(
        nonce=nonce,
        gasPrice=gasPrice,
        gas=100000,
        to='0x0000000000000000000000000000000000000000',
        value=value,
        data=message.encode('utf-8')
    ), privateKey)
    tx = w3.eth.sendRawTransaction(signedTx.rawTransaction)
    txId = w3.toHex(tx)
    return txId

client = redis.StrictRedis(port=6379, db=0)

