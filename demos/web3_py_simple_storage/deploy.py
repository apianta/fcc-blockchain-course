from solcx import compile_standard, install_solc
import json
from web3 import Web3

with open("./SimpleStorage.sol", "r") as file:
    simple_storage_file = file.read()

# compile solidity
install_solc("0.6.0")
compiled_sol = compile_standard(
    {
        "language": "Solidity",
        "sources": {"SimpleStorage.sol": {"content": simple_storage_file}},
        "settings": {
            "outputSelection": {
                "*": {"*": ["abi", "metadata", "evm.bytecode", "evm.sourceMap"]}
            },
        },
    },
    solc_version="0.6.0",
)
with open("compiled_code.json", "w") as file:
    json.dump(compiled_sol, file)

# deploying
# get bytecode
bytecode = compiled_sol["contracts"]["SimpleStorage.sol"]["SimpleStorage"]["evm"][
    "bytecode"
]["object"]

# get abi
abi = compiled_sol["contracts"]["SimpleStorage.sol"]["SimpleStorage"]["abi"]

# connecting to Ganache
w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:7545"))
chain_id = 1337
my_address = "0xB2E9526ECc7343260c9E2B5bdF5c7DAe1193C257"
# make sure to always include the "0x" in the front
private_key = "0x6ec079b0396acfacebeb75452788e7ec995ec4c06ff8d8f26438a00f141e2f16"

# create the contract in puthon
SimpleStorage = w3.eth.contract(abi=abi, bytecode=bytecode)

# get latest transaction

nonce = w3.eth.getTransactionCount(my_address)

# 1.build transaction
# 2. sign the transaction
# 3. send the transaction
transaction = SimpleStorage.constructor().buildTransaction(
    {"chainId": chain_id, "from": my_address, "nonce": nonce}
)
print(transaction)
