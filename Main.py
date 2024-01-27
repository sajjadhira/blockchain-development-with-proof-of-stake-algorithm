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
    exchange = Wallet()
    forger = Wallet()

    exchangeTransaction = exchange.createTransaction(
        alice.publicKeyString(), 100, 'EXCHANGE')

    if not pool.transactionExists(exchangeTransaction):
        pool.addTransaction(exchangeTransaction)

    coveredTransactions = blockchain.getCoveredTransactionSet(
        pool.transactions)
    lastHash = BlockchainUtils.hash(
        blockchain.blocks[-1].payload()).hexdigest()
    blockCount = blockchain.blocks[-1].blockCount + 1
    blockOne = Block(coveredTransactions, lastHash,
                     forger.publicKeyString(), blockCount)
    blockchain.addBlock(blockOne)

    ''' Alice wants to send 5 Token to Bob '''
    transaction = alice.createTransaction(bob.publicKeyString(), 5, 'TRANSFER')

    if not pool.transactionExists(transaction):
        pool.addTransaction(transaction)

    coveredTransactions = blockchain.getCoveredTransactionSet(
        pool.transactions)
    lastHash = BlockchainUtils.hash(
        blockchain.blocks[-1].payload()).hexdigest()
    blockCount = blockchain.blocks[-1].blockCount + 1
    blockTwo = Block(coveredTransactions, lastHash,
                     forger.publicKeyString(), blockCount)
    blockchain.addBlock(blockTwo)

    pprint.pprint(blockchain.toJson())
