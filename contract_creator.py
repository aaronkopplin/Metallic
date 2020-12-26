import json
from solcx import compile_standard
from web3 import Web3


def compile_and_deploy_contract(filePath: str, fileName: str, contractName: str, w3: Web3):
    with open(filePath) as contract_file:
        contract_code = contract_file.read()
        compiled_contract = compile_standard({
            'language': 'Solidity',
            'sources': {
                fileName: {
                    'content': contract_code
                }
            },
            'settings': {
                'outputSelection': {
                    '*': {
                        '*': [
                            'metadata', 'evm.bytecode', 'evm.bytecode.sourceMap'
                        ]
                    }
                }
            }
        })
        bytecode = compiled_contract['contracts'][fileName][contractName]['evm']['bytecode']['object']
        abi = json.loads(compiled_contract['contracts'][fileName][contractName]['metadata'])['output']['abi']
        w3.eth.defaultAccount = w3.eth.accounts[0]
        w3Contract = w3.eth.contract(abi=abi, bytecode=bytecode)
        print("estimated gas to deploy contract", w3Contract.constructor().estimateGas())
        tx_hash = w3Contract.constructor().transact()
        tx_receipt = w3.eth.waitForTransactionReceipt(tx_hash)
        print("Contract", contractName, "is deployed at", tx_receipt.contractAddress)
        smart_contract = w3.eth.contract(address=tx_receipt.contractAddress, abi=abi)
        return smart_contract