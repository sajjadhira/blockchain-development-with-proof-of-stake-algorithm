class Blockchain:
    """
    Blockchain class : Blockchain is a list of blocks
    """

    def __init__(self):
        """
        Constructor
        """
        self.blocks = []

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
