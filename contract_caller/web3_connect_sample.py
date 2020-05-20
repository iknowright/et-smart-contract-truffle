import os
import json

# ABI file
with open('ABI.json') as json_file:
    abi = json.load(json_file)

# Get wallet secret
with open('.secret') as keyfile:
    privateKey = keyfile.read()

from web3 import Web3


# infura node setup
infura_project_id = os.environ["WEB3_INFURA_PROJECT_ID"]
infura_url = f"https://ropsten.infura.io/v3/{infura_project_id}"


# setup provider
web3 = Web3(Web3.HTTPProvider(infura_url))
# check connection and last mined block on ropsten testnet
print(web3.isConnected())
print(web3.eth.blockNumber)


# setup owner account
creator_addr = os.environ['CREATOR_ADDRESS']
account = web3.eth.account.privateKeyToAccount(privateKey)
balance = web3.eth.getBalance(creator_addr)
print(balance)


# # setup contract instance
# contract_addr = os.environ['DEPLOYED_CONTRACT_ADDRESS']
# contract = web3.eth.contract(abi=abi, address=contract_addr)


# # build transaction for bid (example)
# nonce = web3.eth.getTransactionCount(creator_addr)
# bid_Hash = contract.functions.bid(creator_addr,"now","sell",[20],[20]).buildTransaction(
#   {
#     "from": creator_addr,
#     "nonce": nonce,
#     'gas': 5000000,
#     'gasPrice': web3.toWei('1', 'gwei')
#   }
# )
# print(bid_Hash)


# # sign transaction with account
# signed = web3.eth.account.signTransaction(bid_Hash,privateKey)
# print(signed)


# # send transaction to testnet
# ropten_tx = web3.toHex(web3.eth.sendRawTransaction(signed.rawTransaction)))
# print(ropten_tx)


# # get receipt of transaction when block is ready
# receipt = web3.eth.waitForTransactionReceipt(ropten_tx)

# # let contract abi help parsing with tx receipt
# result = contract.events.bid_log().processReceipt(receipt)
