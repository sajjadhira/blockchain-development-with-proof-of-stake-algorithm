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
            lengOfPeers = len(self.socketCommunication.peers)
            print(f"Current Connections {lengOfPeers} :")
            for peer in self.socketCommunication.peers:
                print(peer.ip + ":" + str(peer.port))
            time.sleep(10)

    def discovery(self):
        """
        Send discovery message to all peers
        """
        while True:
            handshakeMessage = self.handleHandshake()
            self.socketCommunication.broadcast(handshakeMessage)
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

    def handleMessage(self, message):
        peerSocketConnector = message.senderConnector
        peersPeerList = message.data
        newPeer = True
        for peer in self.socketCommunication.peers:
            if peer.equals(peerSocketConnector):
                newPeer = False

        if newPeer:
            self.socketCommunication.peers.append(peerSocketConnector)

        for peersPeer in peersPeerList:
            peerKnown = False
            for peer in self.socketCommunication.peers:
                if peer.equals(peersPeer):
                    peerKnown = True
            if not peerKnown and not peersPeer.equals(self.socketCommunication.socketConnector):
                self.socketCommunication.peers.append(peersPeer)
                self.socketCommunication.connect_with_node(
                    peersPeer.ip, peersPeer.port)
