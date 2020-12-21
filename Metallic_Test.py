from web3 import Web3
from ContractCreator import compile_contract
from Metallic import Metallic


w3 = Web3(Web3.EthereumTesterProvider())
w3.eth.defaultAccount = w3.eth.accounts[0]
metallic = Metallic("./Metallic.sol", "Metallic.sol", "Metallic", w3)

# message = metallic.functions.helloWorld().call()
# print(message)
metallic.addUsername("aaron000000000000000000000000000")
metallic.addUsername("aaron000000000000000000000000000")
#
# tx_hash = metallic.functions.addUsername(username).transact()
# tx_receipt = w3.eth.waitForTransactionReceipt(tx_hash)

# >>> tx_hash = greeter.functions.setGreeting('Nihao').transact()
# >>> tx_receipt = w3.eth.waitForTransactionReceipt(tx_hash)
# >>> greeter.functions.greet().call()
# 'Nihao'
