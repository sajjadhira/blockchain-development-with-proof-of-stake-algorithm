from Transaction import Transaction
from Wallet import Wallet
from TransactionPool import TransactionPool
from Block import Block
import pprint
from Blockchain import Blockchain
from BlockchainUtils import BlockchainUtils
from AccountModel import AccountModel
from Node import Node

if __name__ == '__main__':
    node = Node()
    print(node.blockchain)
    print(node.wallet)
    print(node.transactionPool)
