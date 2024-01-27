from Transaction import Transaction
from Wallet import Wallet
from TransactionPool import TransactionPool
from Block import Block
import pprint
from Blockchain import Blockchain
from BlockchainUtils import BlockchainUtils
from AccountModel import AccountModel

if __name__ == '__main__':

    blockchain = Blockchain()
    pool = TransactionPool()

    alice = Wallet()
    bob = Wallet()

    #  alice wants to send 5 token to bob

    transaction = alice.createTransaction(bob.publicKeyString(), 5, "TRANSFER")

    if not pool.existingTransaction(transaction):
        pool.addTransaction(transaction)

    coveredTransactions = blockchain.getCoveredTransactionSet(
        pool.transactions)

    pprint.pprint(coveredTransactions)
