from brownie import network, config, interface
from scripts.helpful_scripts import get_account
from scripts.get_weth import get_weth


def main():
    account = get_account()
    erc20_addrss = config["networks"][network.show_active()]["weth_token"]
    # Address:
    if network.show_active() in ["mainnet-fork"]:
        get_weth()
        # ABI:
    lending_pool = get_lending_pool()


def get_lending_pool():
    lending_pool_addresses_provider = interface.ILendingPoolAddressesProvider(
        config["networks"][network.show_active()]["lending_pool_addresses_provider"]
    )
    lending_pool_address = lending_pool_addresses_provider.getLendingPool()
    # ABI:
    
