from Block import Block
from BlockchainUtils import BlockchainUtils
from AccountModel import AccountModel
from ProofOfStake import ProofOfStake


class Blockchain:
    """
    Blockchain class : Blockchain is a list of blocks
    """

    def __init__(self):
        """
        Constructor
        """
        self.blocks = [Block.genesis()]
        self.accountModel = AccountModel()
        self.pos = ProofOfStake()

    def addBlock(self, block):
        """
        Adds a block to the blockchain
        """
        self.executeTransactions(block.transactions)
        self.blocks.append(block)

    def toJson(self):
        """
        Converts the blockchain to json
        """
        data = {}
        jsonBlocks = []
        for block in self.blocks:
            jsonBlocks.append(block.toJson())

        data["blocks"] = jsonBlocks
        return data

    def blockCountValid(self, block):
        """
        Checks if the block count is valid
        """

        return self.blocks[-1].blockCount == block.blockCount - 1

    def lastBlockHashValid(self, block):
        """
        Checks if the last block hash is valid
        """
        lastBlokchainBlockHash = BlockchainUtils.hash(
            self.blocks[-1].payload()).hexdigest()

        return lastBlokchainBlockHash == block.lastHash

    def getCoveredTransactionSet(self, transactions):
        """
        Returns a set of covered transactions
        """
        coveredTransactions = []
        for transaction in transactions:
            if self.transactionCovered(transaction):
                coveredTransactions.append(transaction)
            else:
                print("Transaction not covered: ")
        return coveredTransactions

    def transactionCovered(self, transaction):
        """
        Checks if the transaction is covered
        """
        if transaction.type == "REWARD" or transaction.type == "EXCHANGE":
            return True

        senderBalance = self.accountModel.getBalance(
            transaction.senderPublicKey)
        return senderBalance >= transaction.amount

    def executeTransactions(self, transactions):
        """
        Executes a list of transactions
        """
        for transaction in transactions:
            self.executeTransaction(transaction)

    def executeTransaction(self, transaction):
        """
        Executes a transaction
        """
        if transaction.type == "STAKE":
            sender = transaction.senderPublicKey
            receiver = transaction.receiverPublicKey

            if sender == receiver:
                self.pos.update(sender, transaction.amount)
                self.accountModel.updateBalance(sender, -transaction.amount)
            else:
                sender = transaction.senderPublicKey
                receiver = transaction.receiverPublicKey
                amount = transaction.amount
                self.accountModel.updateBalance(sender, -amount)
                self.accountModel.updateBalance(receiver, amount)

    def nextForger(self):
        """
        Returns the next forger
        """
        lastBlockHash = BlockchainUtils.hash(
            self.blocks[-1].payload()).hexdigest()
        nextForger = self.pos.forger(lastBlockHash)
        return nextForger

    def createBlock(self, transactionFromPool, forgerWallet):
        """
        Creates a block object
        """
        coveredTransactions = self.getCoveredTransactionSet(
            transactionFromPool)
        self.executeTransactions(coveredTransactions)
        newBlock = forgerWallet.createBlock(
            coveredTransactions, BlockchainUtils.hash(self.blocks[-1].payload()).hexdigest(), len(self.blocks))
        self.blocks.append(newBlock)
        return newBlock

    def transactionExists(self, transaction):
        """
        Checks if the transaction exists
        """
        for block in self.blocks:
            for blockTransaction in block.transactions:
                if blockTransaction.equals(transaction):
                    return True
        return False
