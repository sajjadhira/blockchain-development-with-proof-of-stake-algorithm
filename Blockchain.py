from Block import Block
from BlockchainUtils import BlockchainUtils
from AccountModel import AccountModel


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

    def addBlock(self, block):
        """
        Adds a block to the blockchain
        """
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
