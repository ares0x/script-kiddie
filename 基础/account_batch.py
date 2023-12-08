from eth_account import Account

# 批量生成账户
def createAccounts(quantity):
    Account.enable_unaudited_hdwallet_features()
    result = Account.create_with_mnemonic(passphrase = 'fucksec')
    mnemonic = result[1]
    wallets = []
    print(mnemonic)
    for index in range(quantity):
        localAccount = Account.from_mnemonic(mnemonic=mnemonic,
                                             account_path="m/44'/60'/0'/0/"+ str(index))
        privateKey = str.lower(bytes_to_hex(localAccount.key))
        address = localAccount.address
        wallet = {
            "id": index,
            "address": address,
            "privateKey": privateKey,
            "mnemonic": mnemonic
        }
        wallets.append(wallet.values())

    print(wallets)
    # return wallets
    
def bytes_to_hex(bs):
    return ''.join(['%02X' % b for b in bs])


def main():
    createAccounts(4)

if __name__ == "__main__":
    main()