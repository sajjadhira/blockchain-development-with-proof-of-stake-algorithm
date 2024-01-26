from Crypto.Hash import SHA256
import json


class BlockchainUtils:
    """
    Building Utility Class for Blockchain
    """
    @staticmethod
    def hash(data):
        """
        Hashes data using SHA256
        """
        dataString = json.dumps(data)
        dataBytes = dataString.encode('utf-8')
        dataHash = SHA256.new(dataBytes)
        return dataHash
