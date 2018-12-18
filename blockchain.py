class Blockchain(object):
    def __init__(self):
        self.chain = []
        self.current_transaction = []

    def new_block(self):
        # Creates a new block and brings it into the chain.
        pass

    def new_transaction(self):
        # Makes a new transaction in the list of transactions.
        pass

    @staticmethod
    def hash(block):
        # Hash block.
        pass

    @property
    def last_block(self):
        # Returns the last block in the chain.
        pass

