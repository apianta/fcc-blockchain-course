from scripts.helpful_scripts import get_account
from brownie import interface, config, network


def main():
    get_weth()


def get_weth():
    """
    Mints WETH while depositing ETH
    """
    # ABI
    # Address
    account = get_account()
    weth = interface.Iweth(config["networks"][network.show_active()]["weth_token"])
