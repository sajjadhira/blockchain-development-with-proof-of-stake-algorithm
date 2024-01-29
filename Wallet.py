from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5
from BlockchainUtils import BlockchainUtils
from Transaction import Transaction
from Block import Block


class Wallet:
    """
    Wallet Class: Used to sign transactions and verify ownership
    """

    def __init__(self):
        self.keyPair = RSA.generate(2048)

    def fromKey(self, file):
        key = ''
        with open(file, 'r') as keyfile:
            key = RSA.importKey(keyfile.read())
        self.keyPair = key

    def sign(self, data):
        """
        Signs data using the private key
        """
        dataHash = BlockchainUtils.hash(data)
        signatureSchemeObject = PKCS1_v1_5.new(self.keyPair)
        signature = signatureSchemeObject.sign(dataHash)
        return signature.hex()

    @staticmethod
    def signatureValid(data, signature, publicKeyString):
        """
        Verifies the signature of the data using the public key
        """
        signature = bytes.fromhex(signature)
        dataHash = BlockchainUtils.hash(data)
        publicKey = RSA.importKey(publicKeyString)
        signatureSchemeObject = PKCS1_v1_5.new(publicKey)
        singnatureValid = signatureSchemeObject.verify(dataHash, signature)
        return singnatureValid

    def publicKeyString(self):
        """
        Returns the public key as a string
        """
        publicKeyString = self.keyPair.publickey().exportKey('PEM').decode('utf-8')
        return publicKeyString

    def createTransaction(self, receiver, amount, type):
        """
        Creates a transaction object
        """
        transaction = Transaction(
            self.publicKeyString(), receiver, amount, type)
        signature = self.sign(transaction.payload())
        transaction.sign(signature)
        return transaction

    def createBlock(self, transactions, lastHash, blockCount):
        """
        Creates a block object
        """
        block = Block(transactions, lastHash,
                      self.publicKeyString(), blockCount)
        signature = self.sign(block.payload())
        block.sign(signature)
        return block
