from Transaction import Transaction
from Wallet import Wallet
from TransactionPool import TransactionPool
from Block import Block
import pprint

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

    print(signatureValid)
    print(singnatureInvalid)
