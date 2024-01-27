import uuid
import time
import copy


class Transaction():

    def __init__(self, senderPublicKey, receiverPublicKey, amount, type):
        """
        Constructor for the Transaction class
        """
        self.senderPublicKey = senderPublicKey
        self.receiverPublicKey = receiverPublicKey
        self.amount = amount
        self.type = type
        self.id = (uuid.uuid1()).hex
        self.timestamp = time.time()
        self.signature = ''

    def toJson(self):
        """
        Returns a json representation of the transaction
        """
        return self.__dict__

    def sign(self, signature):
        """
        Signs the transaction with the given signature
        """
        self.signature = signature

    def payload(self):
        """
        Returns a json representation of the transaction without the signature
        """
        jsonRepresentation = copy.deepcopy(self.toJson())
        jsonRepresentation['signature'] = ''
        return jsonRepresentation

    def equals(self, transaction):
        """
        Returns true if the transaction is the same as the given transaction
        """
        if self.id == transaction.id:
            return True
        else:
            return False
