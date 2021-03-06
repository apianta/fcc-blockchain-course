from webbrowser import get
from brownie import accounts, config, SimpleStorage, network


def deploy_simple_storage():
    account = getAccount()
    simple_storage = SimpleStorage.deploy({"from": account})
    # print(simple_storage)
    stored_value = simple_storage.retrieve()
    print(stored_value)
    transaction = simple_storage.store(15, {"from": account})
    transaction.wait(1)
    updated_stored_value = simple_storage.retrieve()
    print(updated_stored_value)

def getAccount():
    if network.show_active() == "development":
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])

# 0x66aB6D9362d4F35596279692F0251Db635165871
def main():
    deploy_simple_storage()
