from contract_creator import compile_and_deploy_contract

class Metallic:
    def __init__(self, filePath: str, fileName: str, contractName: str, w3):
        self.contract = compile_and_deploy_contract(filePath, fileName, contractName, w3)
        self.w3 = w3

    def helloWorld(self):
        return self.contract.functions.helloWorld().call()

    def addAccount(self, username: str, public_address: str, currency: str):
        tx_hash = self.contract.functions.addAccount(username, public_address, currency).transact()
        tx_receipt = self.w3.eth.waitForTransactionReceipt(tx_hash)
        return tx_receipt

    def getAddress(self, username):
        return self.contract.functions.getAddress(username).call()

    def username_exists(self, username: str):
        return self.contract.functions.usernameExists(username).call()
    #
    # def getCurrentUsersUsername(self):
    #     return self.contract.functions.getCurrentUsersUsername().call()

