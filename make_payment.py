from web3 import Web3


def create_ganache_w3():
    ganache = "HTTP://127.0.0.1:7545"  # current ganache address and port
    return Web3(Web3.HTTPProvider(ganache))


def transfer(from_public: str, from_private: str, to_public: str, amount: int, w3: Web3):
    if w3.isConnected():
        nonce = w3.eth.getTransactionCount(from_public)
        tx = {
            'nonce': nonce,
            'to': to_public,
            'value': Web3.toWei(amount, 'ether'),
            'gas': 2000000,
            'gasPrice': Web3.toWei('50', 'gwei'),
        }

        signed_tx = w3.eth.account.signTransaction(tx, from_private)
        tx_hash = w3.eth.sendRawTransaction(signed_tx.rawTransaction)
        print(Web3.toHex(tx_hash))
    else:
        raise Exception("Not Connected to ganache")