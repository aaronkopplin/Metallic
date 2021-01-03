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

    # create and sign the transaction with the created account information
    def addAccountPayWithSameAccount(self, username: str, public_address: str, currency: str, creationDate: str, private_key: str):
        estimated_gas = self.estimateGasToAddAccount(username, public_address, currency, creationDate)
        nonce = self.w3.eth.getTransactionCount(public_address)
        transaction = self.contract.functions.addAccount(username, 
                                                        public_address, 
                                                        currency, 
                                                        creationDate
            ).buildTransaction({
                'chainId' : 1,
                'gas' : estimated_gas,
                'gasPrice' : auto.w3.toWei('47', 'gwei'),
                'nonce' : nonce
            })

        signed_txn = self.w3.eth.account.sign_transaction(transaction, private_key)
        self.w3.eth.sendRawTransaction(signed_txn.rawTransaction)

    def addAccount(self, username: str, public_address: str, currency: str, creationDate: str):
        estimated_gas = self.estimateGasToAddAccount(username, public_address, currency, creationDate)
        nonce = self.w3.eth.getTransactionCount(self.receive_account._address)
        transaction = self.contract.functions.addAccount(username, 
                                                        public_address, 
                                                        currency, 
                                                        creationDate
            ).buildTransaction({
                'chainId' : 1,
                'gas' : estimated_gas,
                'gasPrice' : auto.w3.toWei('47', 'gwei'),
                'nonce' : nonce
            })

        signed_txn = self.w3.eth.account.sign_transaction(transaction, self.receive_account._private_key)
        self.w3.eth.sendRawTransaction(signed_txn.rawTransaction)

    def estimateGasToAddAccount(self, username: str, public_address: str, currency: str, creationDate: str):
        return self.contract.functions.addAccount(username, public_address, currency, creationDate).estimateGas()

    def convertGasToEth(self, gas: int):
        return Web3.fromWei(gas, "ether")

    def getAddress(self, username):
        return self.contract.functions.getAddress(username).call()

    def username_exists(self, username: str):
        return self.contract.functions.usernameExists(username).call()

    def getAccounts(self):
        # returns a list of tuples [("username", "address", "currency"), (...), (...), ...]
        return self.contract.functions.getAccounts().call()

    def getStructuredAccounts(self):
        def byDateCreated(account):
            return account['dateCreated']

        accounts = []
        raw_accounts = self.getAccounts()
        for account in raw_accounts:
            accounts.append({
                'username' : account[0],
                'address' : account[1],
                'currency' : account[2],
                'dateCreated' : account[3]
            })
            
        accounts.sort(key=byDateCreated)
        return accounts



