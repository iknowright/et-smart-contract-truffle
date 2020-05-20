import os
import json
from web3 import Web3
from dotenv import load_dotenv


load_dotenv()

class ET_Contract():
    def __init__(self):
        privateKey = os.environ['SECRET']
        infura_url = f"https://ropsten.infura.io/v3/{os.environ['WEB3_INFURA_PROJECT_ID']}"

        # setup provider
        web3 = Web3(Web3.HTTPProvider(infura_url))

        # setup owner account
        self.creator_addr = os.environ.get['CREATOR_ADDRESS']
        self.account = web3.eth.account.privateKeyToAccount(privateKey)

        # contract abi
        with open('ABI.json') as json_file:
            abi = json.load(json_file)

        contract_addr = os.environ['DEPLOYED_CONTRACT_ADDRESS']
        self.contract = web3.eth.contract(abi=abi, address=contract_addr)

    def bid(self, bidder, time, bid_type, volumes, prices):
        nonce = web3.eth.getTransactionCount(creator_addr)
        bid_hash = contract.functions.bid(bidder, time, bid_type, volumes, prices).buildTransaction({
            "from": self.creator_addr,
            "nonce": nonce,
            'gas': 5000000,
            'gasPrice': web3.toWei('1', 'gwei')
        })
        # sign transaction with account
        signed = web3.eth.account.signTransaction(bid_hash, privateKey)
        # send transaction to testnet
        tx = web3.toHex(web3.eth.sendRawTransaction(signed.rawTransaction))
        # get receipt of transaction when block is ready
        receipt = web3.eth.waitForTransactionReceipt(tx)
        # let contract abi help parsing with tx receipt
        result = contract.events.bid_log().processReceipt(receipt)

    def match_bids(self, users, time):
        nonce = web3.eth.getTransactionCount(creator_addr)
        bid_hash = contract.functions.match_bids(users, time).buildTransaction({
            "from": self.creator_addr,
            "nonce": nonce,
            'gas': 5000000,
            'gasPrice': web3.toWei('1', 'gwei')
        })
