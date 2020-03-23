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
account = web3.eth.account.privateKeyToAccount(privateKey)
balance = web3.eth.getBalance('0x481dE1a3d53c2D740e61CC08ed7fa8A8D294C1CC')
print(balance)


# setup contract instance
contract_addr = '0x60cB88a60E2B5A14D7E59c97f3bCEc2C7eb3b20B'
contract = web3.eth.contract(abi=abi, address=contract_addr)


# build transaction for bid (example)
nonce = web3.eth.getTransactionCount('0x481dE1a3d53c2D740e61CC08ed7fa8A8D294C1CC')
bid_Hash = contract.functions.bid("0x481dE1a3d53c2D740e61CC08ed7fa8A8D294C1CC","now","sell",[20],[20]).buildTransaction(
  {
    "from":"0x481dE1a3d53c2D740e61CC08ed7fa8A8D294C1CC",
    "nonce": nonce,
    'gas': 5000000,
    'gasPrice': web3.toWei('1', 'gwei')
  }
)
print(bid_Hash)


# sign transaction with account
signed = web3.eth.account.signTransaction(bid_Hash,privateKey)
print(signed)


# send transaction to testnet
ropten_tx = web3.toHex(web3.eth.sendRawTransaction(signed.rawTransaction)))
print(ropten_tx)


# get receipt of transaction when block is ready
receipt = web3.eth.waitForTransactionReceipt('0xd4d285e2bf9a28edf7f17b607ed4082815ff5140601f98a240aba6e79cc2feda')

# let contract abi help parsing with tx receipt
result = contract.events.bid_log().processReceipt(receipt)
_user = result[0]['args']['_user']
_bid_type = result[0]['args']['_bid_type']
_bid_type = result[0]['args']['_bid_type']
_volumn = result[0]['args']['_volumn']
_price = result[0]['args']['_price']