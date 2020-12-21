import json
from solcx import compile_standard

def compile_contract(filePath: str, fileName: str, contractName: str, w3):
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
        w3Contract = w3.eth.contract(abi=abi, bytecode=bytecode)
        tx_hash = w3Contract.constructor().transact()
        tx_receipt = w3.eth.waitForTransactionReceipt(tx_hash)
        smart_contract = w3.eth.contract(address=tx_receipt.contractAddress, abi=abi)
        return smart_contract