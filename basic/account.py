from web3 import Web3
from eth_account import Account

# 生成 ETH 地址
def createAccount():
    w3 = Web3(); 
    # create 中的参数extra_entropy 可以删除，也可以替换成任意字符 
    acc = w3.eth.account.create(extra_entropy='ares0xff')
    # 将生成的 eth 地址导入 metamask 等软件即可
    print(f'privateKey:{w3.to_hex(acc.key)}, account:{acc.address}')
    # 判断地址是否符合格式要求
    print(w3.is_address(acc.address))

# createAccountWithMnemonic 生成带有助记词的 ETH 地址
def createAccountWithMnemonic():
    w3 = Web3(); 
    Account.enable_unaudited_hdwallet_features()
    result = Account.create_with_mnemonic(passphrase = 'ares0xff')
    mnemonic = result[1]
    account = w3.eth.account.from_mnemonic(mnemonic, account_path="m/44'/60'/0'/0/0")
    privateKey = str.lower(bytes_to_hex(account.key))
    address = account.address
    wallet = {
        "address": address,
        "privateKey": privateKey,
        "mnemonic": mnemonic
    }
    print(wallet)

def bytes_to_hex(bs):
    return ''.join(['%02X' % b for b in bs])

def main():
    # createAccount()
    createAccountWithMnemonic()


if __name__ == "__main__":
    main()