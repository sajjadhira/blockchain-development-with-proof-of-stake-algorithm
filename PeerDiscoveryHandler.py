import threading
import time
from Message import Message
from BlockchainUtils import BlockchainUtils


class PeerDiscoveryHandler:
    def __init__(self, node):
        self.socketCommunication = node

    def start(self):
        """
        Start the PeerDiscoveryHandler
        """
        statusThread = threading.Thread(target=self.status, args=())
        statusThread.start()
        discoveryThread = threading.Thread(target=self.discovery, args=())
        discoveryThread.start()

    def status(self):
        """
        Send status message to all peers
        """
        while True:
            print("status")
            time.sleep(10)

    def discovery(self):
        """
        Send discovery message to all peers
        """
        while True:
            print("discovery")
            time.sleep(10)

    def handshake(self, connected_node):
        """
        Send handshake message to a peer
        """
        handshakeMessage = self.handleHandshake()
        self.socketCommunication.send(connected_node, handshakeMessage)

    def handleHandshake(self):
        """
        Handle a handshake message
        """
        ownConnector = self.socketCommunication.socketConnector
        ownPeers = self.socketCommunication.peers
        data = ownPeers
        messageType = 'DISCOVERY'
        message = Message(ownConnector, messageType, data)
        encodedMessage = BlockchainUtils.encode(message)
        return encodedMessage
