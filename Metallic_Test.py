from web3 import Web3
from Metallic import Metallic
import pprint

w3 = Web3(Web3.EthereumTesterProvider())
w3.eth.defaultAccount = w3.eth.accounts[0]
metallic = Metallic("./Metallic.sol", "Metallic.sol", "Metallic", w3)

tx = metallic.addUsername("aaron")
pprint.pprint(dict(tx))
address = metallic.getAddressFromUsername("aaron")
print(address)
username = metallic.getUsernameFromAddress(address)
print(username)
print(metallic.getCurrentUsersUsername())
# metallic.addUsername("")
