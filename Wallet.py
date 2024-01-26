from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5
from BlockchainUtils import BlockchainUtils
from Transaction import Transaction


class Wallet:
    """
    Wallet Class: Used to sign transactions and verify ownership
    """

    def __init__(self):
        self.keyPair = RSA.generate(2048)

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
