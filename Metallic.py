from ContractCreator import compile_contract
from Utilities import stringToBytes

class Metallic():
    def __init__(self, filePath: str, fileName: str, contractName: str, w3):
        self.contract = compile_contract(filePath, fileName, contractName, w3)
        self.w3 = w3

    def addUsername(self, username: str):
        tx_hash = self.contract.functions.addUsername(stringToBytes(username, 32)).transact()
        tx_receipt = self.w3.eth.waitForTransactionReceipt(tx_hash)
