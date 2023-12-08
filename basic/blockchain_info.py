import os
from web3 import Web3
from dotenv import load_dotenv
_ = load_dotenv()

PROVIDER = os.environ['PROVIDER']
# getLatestBlock 获取最新的区块数据
def getLatestBlock():
    w3 = Web3(Web3.HTTPProvider(PROVIDER)); 
    print(w3.eth.get_block('latest'))

def getBlockNumber():
    w3 = Web3(Web3.HTTPProvider(PROVIDER)); 
    print(w3.eth.block_number())

def main():
    # getLatestBlock()
    getBlockNumber()

if __name__ == "__main__":
    main()