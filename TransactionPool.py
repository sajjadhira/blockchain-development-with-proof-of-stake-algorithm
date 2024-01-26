class TransactionPool:
    def __init__(self):
        self.transactions = []

    def addTransaction(self, transaction):
        """
        Adds a transaction to the transaction pool
        """
        self.transactions.append(transaction)

    def existingTransaction(self, transaction):
        """
        Checks if a transaction exists in the transaction pool
        """
        for transaction in self.transactions:
            if transaction.equals(transaction):
                return True
        return False
