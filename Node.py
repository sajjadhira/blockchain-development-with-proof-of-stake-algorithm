from Blockchain import Blockchain
from TransactionPool import TransactionPool
from Wallet import Wallet
from SocketCommunication import SocketCommunication
from NodeAPI import NodeAPI
from Message import Message
from BlockchainUtils import BlockchainUtils


class Node():

    def __init__(self, ip, port):
        self.p2p = None
        self.ip = ip
        self.port = port
        self.blockchain = Blockchain()
        self.transactionPool = TransactionPool()
        self.wallet = Wallet()

    def startP2P(self):
        self.p2p = SocketCommunication(self.ip, self.port)
        self.p2p.startSocketCommunication(self)

    def startAPI(self, apiPort):
        self.api = NodeAPI()
        self.api.injectNode(self)
        self.api.start(apiPort)

    def handleTransaction(self, transaction):
        data = transaction.payload()
        signature = transaction.signature
        signerPublicKey = transaction.senderPublicKey
        signatureValid = Wallet.signatureValid(
            data, signature, signerPublicKey)
        transactionExists = self.transactionPool.transactionExists(transaction)
        if not transactionExists and signatureValid:
            self.transactionPool.addTransaction(transaction)
            message = Message(self.p2p.socketConnector,
                              'TRANSACTION', transaction)
            encodedMessage = BlockchainUtils.encode(message)
            self.p2p.broadcast(encodedMessage)
