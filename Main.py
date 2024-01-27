from Transaction import Transaction
from Wallet import Wallet
from TransactionPool import TransactionPool
from Block import Block
import pprint
from Blockchain import Blockchain

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

    if not pool.existingTransaction(transaction):
        pool.addTransaction(transaction)

    block = wallet.createBlock(pool.transactions, 'lastHash', 'forger', 1)

    signatureValid = wallet.signatureValid(
        block.payload(), block.signature, wallet.publicKeyString())

    singnatureInvalid = wallet.signatureValid(
        block.payload(), block.signature, fruadulentWallet.publicKeyString())

    blockchain = Blockchain()

    blockchain.addBlock(block)

    pprint.pprint(blockchain.toJson())
