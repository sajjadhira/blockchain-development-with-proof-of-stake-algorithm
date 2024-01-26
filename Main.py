from Transaction import Transaction
from Wallet import Wallet
from TransactionPool import TransactionPool

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

    print(pool.transactions.__len__())
