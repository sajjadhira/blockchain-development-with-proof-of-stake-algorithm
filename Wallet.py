from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5
from BlockchainUtils import BlockchainUtils


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
