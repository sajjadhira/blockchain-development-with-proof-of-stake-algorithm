import uuid
import time


class Transaction:
    """
    Transaction class: is used to create a transaction object
    """

    def __init__(self, senderPublicKey, recipientPublicKey, amount, type):
        self.senderPublicKey = senderPublicKey
        self.recipientPublicKey = recipientPublicKey
        self.amount = amount
        self.type = type
        self.id = uuid.uuid1().hex
        self.timestamp = time.time()
        self.signature = ''

    # method to convert the transaction object to a dictionary
    def toJson(self):
        return self.__dict__

    def sign(self, signature):
        self.signature = signature,
