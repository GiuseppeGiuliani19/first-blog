from web3 import Web3
import json
import redis
import ipapi
from django.http import JsonResponse
import nmap
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
# def posts_redis(request):
#     response = []
#     posts = Post.objects.filter().order_by('-created_date')
#     for post in posts:
#             response.append(
#                 {
#                     'published_date': post.created_date,
#                     'title': post.title,
#                     'text': post.text,
#                     'author': f"{post.author}",
#                     'hash': post.hash,
#                     'TxId': post.TxId
#                 }
#             )
#     key = client.set('lista_post', response)
#     print(key)
#     return JsonResponse(response, safe=False)

#key = client.set(response, )




# def ip(request):
#       search = request.POST.get('search')
#       data = ipapi.location(ip=search, output='json')
#       pipe = client.pipeline()
#       pipe.set('data', data)
#       d=pipe.execute()
    #  print(d)
      #print(d)

# def main():
#     return 'ciao'
# print(main())
# data = ipapi.location(output='json')
# print(ip(request=data))
# pipe = client.pipeline()
# pipe.set('data', data)
# pipe.set('altro_numero', 200)
# pipe.get('numero')
# pipe.get('altro_numero')
# print(pipe.execute())

# class Red:
#     def set(cache_key, data):
#         data = json.dumps(data)
#         rd.set(cache_key, data)
#
#         return True
#
#     def get(cache_key):
#         cache_data = rd.get(cache_key)
#         cache_data = json.loads(cache_data)
#
#         return cache_data



#4_write_smart_contracts.py
#Set up web3 connection with Ganache
# ganache_url = "http://127.0.0.1:7545"
# web3 = Web3(Web3.HTTPProvider(ganache_url))
#
# print(web3.isConnected())
# print(web3.eth.blockNumber)
#
# # TODO: Deploy the Greeter contract to Ganache with remix.ethereum.org
#
# # Set a default account to sign transactions - this account is unlocked with Ganache
# web3.eth.defaultAccount = web3.eth.accounts[0]
# # Greeter contract ABI
# abi = json.loads('[{"constant":false,"inputs":[{"name":"_greeting","type":"string"}],"name":"setGreeting",'
#                  '"outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},'
#                  '{"constant":true,"inputs":[],"name":"greet","outputs":[{"name":"","type":"string"}],'
#                  '"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],'
#                  '"name":"greeting","outputs":[{"name":"","type":"string"}],"payable":false,"stateMutability":"view",'
#                  '"type":"function"},{"inputs":[],"payable":false,"stateMutability":"nonpayable",'
#                  '"type":"constructor"}]')
# # Greeter contract address - convert to checksum address
# address = web3.toChecksumAddress('0x529D189F55068770a39f47024aa87DF43459242f')# FILL ME IN
# # Initialize contract
# contract = web3.eth.contract(address=address, abi=abi)
# # Read the default greeting
# print(contract.functions.greet().call())
# # Set a new greeting
# tx_hash = contract.functions.setGreeting('HEELLLLOOOOOO!!!').transact()
# # Wait for transaction to be mined
# web3.eth.waitForTransactionReceipt(tx_hash)
# # Display the new greeting value
# print('Updated contract greeting: {}'.format(
#     contract.functions.greet().call()
# ))






#3_send_transactions.py
# ganache_url = "http://127.0.0.1:7545"
# web3 = Web3(Web3.HTTPProvider(ganache_url))
#
# account_1 = '0x529D189F55068770a39f47024aa87DF43459242f' # Fill me in
# account_2 = '0x8a26A3Ed2a3f5C1D2949A784f9AAeC037E1159a4' # Fill me in
# private_key = 'add4159311b56e24eb073ee8e953de4ee2cb03f5290d44ec2ed6efecf4080c78' # Fill me in
#
# nonce = web3.eth.getTransactionCount(account_1)
#
# tx = {
#     'nonce': nonce,
#     'to': account_2,
#     'value': web3.toWei(1, 'ether'),
#     'gas': 2000000,
#     'gasPrice': web3.toWei('50', 'gwei'),
# }
#
# signed_tx = web3.eth.account.signTransaction(tx, private_key)
#
# tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)
#
# print(web3.toHex(tx_hash))



#5_deploy_smart_contracts.py
# Set up web3 connection with Ganache
# ganache_url = "http://127.0.0.1:7545"
# web3 = Web3(Web3.HTTPProvider(ganache_url))
#
# abi = json.loads('[{"constant":false,"inputs":[{"name":"_greeting","type":"string"}],"name":"setGreeting","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"greet","outputs":[{"name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"greeting","outputs":[{"name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"inputs":[],"payable":false,"stateMutability":"nonpayable","type":"constructor"}]')
# bytecode = "6060604052341561000f57600080fd5b6040805190810160405280600581526020017f48656c6c6f0000000000000000000000000000000000000000000000000000008152506000908051906020019061005a929190610060565b50610105565b828054600181600116156101000203166002900490600052602060002090601f016020900481019282601f106100a157805160ff19168380011785556100cf565b828001600101855582156100cf579182015b828111156100ce5782518255916020019190600101906100b3565b5b5090506100dc91906100e0565b5090565b61010291905b808211156100fe5760008160009055506001016100e6565b5090565b90565b61041a806101146000396000f300606060405260043610610057576000357c0100000000000000000000000000000000000000000000000000000000900463ffffffff168063a41368621461005c578063cfae3217146100b9578063ef690cc014610147575b600080fd5b341561006757600080fd5b6100b7600480803590602001908201803590602001908080601f016020809104026020016040519081016040528093929190818152602001838380828437820191505050505050919050506101d5565b005b34156100c457600080fd5b6100cc6101ef565b6040518080602001828103825283818151815260200191508051906020019080838360005b8381101561010c5780820151818401526020810190506100f1565b50505050905090810190601f1680156101395780820380516001836020036101000a031916815260200191505b509250505060405180910390f35b341561015257600080fd5b61015a610297565b6040518080602001828103825283818151815260200191508051906020019080838360005b8381101561019a57808201518184015260208101905061017f565b50505050905090810190601f1680156101c75780820380516001836020036101000a031916815260200191505b509250505060405180910390f35b80600090805190602001906101eb929190610335565b5050565b6101f76103b5565b60008054600181600116156101000203166002900480601f01602080910402602001604051908101604052809291908181526020018280546001816001161561010002031660029004801561028d5780601f106102625761010080835404028352916020019161028d565b820191906000526020600020905b81548152906001019060200180831161027057829003601f168201915b5050505050905090565b60008054600181600116156101000203166002900480601f01602080910402602001604051908101604052809291908181526020018280546001816001161561010002031660029004801561032d5780601f106103025761010080835404028352916020019161032d565b820191906000526020600020905b81548152906001019060200180831161031057829003601f168201915b505050505081565b828054600181600116156101000203166002900490600052602060002090601f016020900481019282601f1061037657805160ff19168380011785556103a4565b828001600101855582156103a4579182015b828111156103a3578251825591602001919060010190610388565b5b5090506103b191906103c9565b5090565b602060405190810160405280600081525090565b6103eb91905b808211156103e75760008160009055506001016103cf565b5090565b905600a165627a7a7230582006f39b9b9b558a328403f9c048af30519c79e6536660d7660e8002af27f240930029"
#
# # # set pre-funded account as sender
# web3.eth.defaultAccount = web3.eth.accounts[0]
#
# # # Instantiate and deploy contract
# Greeter = web3.eth.contract(abi=abi, bytecode=bytecode)
#
# # # Submit the transaction that deploys the contract
# tx_hash = Greeter.constructor().transact()
#
# # # Wait for the transaction to be mined, and get the transaction receipt
# tx_receipt = web3.eth.waitForTransactionReceipt(tx_hash)
#
# # # Create the contract instance with the newly-deployed address
# contract = web3.eth.contract(
#     address=tx_receipt.contractAddress,
#     abi=abi,
# )
#
# print(tx_receipt.contractAddress)
#
# # # # Display the default greeting from the contract
# print('Default contract greeting: {}'.format(
#     contract.functions.greet().call()
# ))
#
# # # update the greeting
# tx_hash = contract.functions.setGreeting('HELLOOOO!!!!').transact()
#
# # # Wait for transaction to be mined...
# web3.eth.waitForTransactionReceipt(tx_hash)
#
# # # Display the new greeting value
# print('Updated contract greeting: {}'.format(
#     contract.functions.greet().call()
# ))

# infura_url = 'https://ropsten.infura.io/v3/5ce9ad5357d449778730d2fbad3d6de9'
# web3 = Web3(Web3.HTTPProvider(infura_url))
#
# # get latest block number
# print(web3.eth.blockNumber)
#
# # get latest block
# print(web3.eth.getBlock('latest'))
#
# # get latest 10 blocks
# latest = web3.eth.blockNumber
# for i in range(0, 10):
#   print(web3.eth.getBlock(latest - i))

# get transaction from specific block
#hash = '0x66b3fd79a49dafe44507763e9b6739aa0810de2c15590ac22b5e2f0a3f502073'
#print(web3.eth.getTransactionByBlock(hash, 2))