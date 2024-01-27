from Transaction import Transaction
from Wallet import Wallet
from TransactionPool import TransactionPool
from Block import Block
import pprint
from Blockchain import Blockchain
from BlockchainUtils import BlockchainUtils

if __name__ == '__main__':
    sender = 'sender'
    recipient = 'recipient'
    amount = 100
    type = 'TRANSFER'

    wallet = Wallet()

    fruadulentWallet = Wallet()

    pool = TransactionPool()

    transaction = wallet.createTransaction(recipient, amount, type)

    if not pool.existingTransaction(transaction):
        pool.addTransaction(transaction)

    blockchain = Blockchain()
    lastHash = BlockchainUtils.hash(
        blockchain.blocks[-1].payload()).hexdigest()
    blockCount = blockchain.blocks[-1].blockCount + 1

    block = wallet.createBlock(
        pool.transactions, lastHash, wallet.publicKeyString(), blockCount)

    if not blockchain.lastBlockHashValid(block):
        print('Invalid block hash')

    elif not blockchain.blockCountValid(block):
        print('Invalid block count')
    else:
        blockchain.addBlock(block)

    pprint.pprint(blockchain.toJson())
