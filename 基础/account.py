from web3 import Web3
from eth_account import Account

# 生成 ETH 地址
def createAccount():
    w3 = Web3(); 
    # create 中的参数extra_entropy 也可以删除 
    acc = w3.eth.account.create(extra_entropy='ares0xff')
    # 将生成的 eth 地址导入 metamask 等软件即可
    print(f'privateKey:{w3.to_hex(acc.key)}, account:{acc.address}')


# 生成账户


# 校验账户

def main():
    createAccount()


if __name__ == "__main__":
    main()