import os
from web3 import Web3
from dotenv import load_dotenv
_ = load_dotenv()

PROVIDER = os.environ['PROVIDER']
ADDRESS = ''

def get_w3_by_network(network='mainnet'):
    w3 = Web3(Web3.HTTPProvider(PROVIDER))
    return w3


def getBalance():
    w3 = get_w3_by_network('mainnet')
    balance = w3.eth.get_balance(ADDRESS) / 1e18