from brownie import SimpleStorage, accounts, config

def read_contract():
    simple_storage = SimpleStorage[-1]
    # take the indec thats one less that the length
    # abi
    # address
    print(simple_storage.retrieve())

def main():
    read_contract()
    