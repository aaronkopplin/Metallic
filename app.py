from web3 import Web3
from metallic import Metallic
from website import run_website
import sys


# connect to ganache blockchain
ganache = sys.argv[1]
w3 = Web3(Web3.HTTPProvider(ganache))

# deploy the contract to ganache
metallic = Metallic("./metallic.sol", 'metallic.sol', "Metallic", w3)

run_website(metallic)

