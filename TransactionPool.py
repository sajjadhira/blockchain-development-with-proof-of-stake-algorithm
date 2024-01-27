class TransactionPool:
    def __init__(self):
        self.transactions = []

    def addTransaction(self, transaction):
        """
        Adds a transaction to the transaction pool
        """
        self.transactions.append(transaction)

    def transactionExists(self, transaction):
        """
        Checks if a transaction exists in the transaction pool
        """
        for transaction in self.transactions:
            if transaction.equals(transaction):
                return True
        return False

    def removeTransaction(self, transactions):
        """
        Removes a transaction from the transaction pool
        """
        newPoolTransactions = []
        for poolTransaction in self.transactions:
            insert = True
            for transaction in transactions:
                if poolTransaction.equals(transaction):
                    insert = False
            if insert:
                newPoolTransactions.append(poolTransaction)
        self.transactions = newPoolTransactions
