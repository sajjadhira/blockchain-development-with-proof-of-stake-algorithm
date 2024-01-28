from Blockchain import Blockchain
from TransactionPool import TransactionPool
from Wallet import Wallet
from SocketCommunication import SocketCommunication
from NodeAPI import NodeAPI


class Node:

    def __init__(self, ip, port):
        self.p2p = None
        self.ip = ip
        self.port = port
        self.blockchain = Blockchain()
        self.transactionPool = TransactionPool()
        self.wallet = Wallet()

    def startP2P(self):
        self.p2p = SocketCommunication(self.ip, self.port)
        self.p2p.startSocketCommunication()

    def startAPI(self):
        self.api = NodeAPI()
        self.api.start()
