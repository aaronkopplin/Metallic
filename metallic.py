from contract_creator import compile_and_deploy_contract
import web3.auto as auto
from web3 import Web3

class Metallic:
    def __init__(self, filePath: str, fileName: str, contractName: str, w3):
        self.contract = compile_and_deploy_contract(filePath, fileName, contractName, w3)
        self.w3 = w3
        self.receive_account = self.w3.eth.account.create("test seed")

    def getReceiveAddress(self):
        return str(self.receive_account._address)

    def helloWorld(self):
        return self.contract.functions.helloWorld().call()

    def addAccount(self, username: str, public_address: str, currency: str):
        estimated_gas = self.estimateGasToAddAccount(username, public_address, currency)
        nonce = self.w3.eth.getTransactionCount(self.receive_account._address)
        transaction = self.contract.functions.addAccount(username, public_address, currency).buildTransaction({
            'chainId' : 1,
            'gas' : estimated_gas,
            'gasPrice' : auto.w3.toWei('1', 'gwei'),
            'nonce' : nonce
        })

        signed_txn = self.w3.eth.account.sign_transaction(transaction, self.receive_account._private_key)
        self.w3.eth.sendRawTransaction(signed_txn.rawTransaction)
        print("signed transaction hash", Web3.toHex(signed_txn.hash) )


        # tx_hash = self.contract.functions.addAccount(username, public_address, currency).transact()
        # tx_receipt = self.w3.eth.waitForTransactionReceipt(tx_hash)
        # return tx_receipt

    def estimateGasToAddAccount(self, username: str, public_address: str, currency: str):
        return self.contract.functions.addAccount(username, public_address, currency).estimateGas()

    def getAddress(self, username):
        return self.contract.functions.getAddress(username).call()

    def username_exists(self, username: str):
        return self.contract.functions.usernameExists(username).call()

    def getAccounts(self):
        # returns a list of tuples [("username", "address", "currency"), (...), (...), ...]
        return self.contract.functions.getAccounts().call()
    #
    # def getCurrentUsersUsername(self):
    #     return self.contract.functions.getCurrentUsersUsername().call()

