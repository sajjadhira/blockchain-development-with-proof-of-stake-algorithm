from Crypto.Hash import SHA256
import json
import jsonpickle


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

    @staticmethod
    def encode(objectToEncode):
        """
        Encodes object to JSON
        """
        return jsonpickle.encode(objectToEncode, unpicklable=True)

    @staticmethod
    def decode(encodedBytes):
        """
        Decodes JSON to object
        """
        return jsonpickle.decode(encodedBytes)
