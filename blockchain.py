import hashlib
import json

from time import time
from uuid import uuid4


class Blockchain(object):
    def __init__(self):
        self.current_transaction = []
        self.chain = []

        # Creating a genesis block
        self.new_block(previous_hash=1, proof=100)

    def new_block(self, proof, previous_hash=None):
        """Creates a new block and brings it into the chain

        :param proof: <int>
        :param previous_hash:
        :return: <dict>
        """

        block = {
            'index': len(self.chain) + 1,
            'timestamp': time(),
            'transaction': self.current_transaction,
            'proof': proof,
            'previous_hash': previous_hash or self.hash(self.chain[-1]),
        }

        # Reload current transaction list
        self.current_transaction = []

        self.chain.append(block)
        return block

    def new_transaction(self):
        """Makes a new transaction in the list of transactions

        :param sender: <str>
        :param recipient: <str>
        :param amount: <int>
        :return: <int>
        """

        self.current_transaction.append({
            'sender': sender,
            'recipient': recipient,
            'amount': amount,
        })

        return self.last_block['index'] + 1

    @property
    def last_block(self):
        # Returns the last block in the chain.
        return self.chain[-1]

    @staticmethod
    def hash(block):
        """Create hash SHA-256 block

        :param block: <dict> Block
        :return: <str>
        """

        # We must make sure that the dictionary is ordered, otherwise we'll
        # have inconsistent hashes
        block_string = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

    def proof_of_work(self, last_proof):
        """
        Simple algorithm check:
        - The search for the number p`, since hash(pp`) contains 4 capital zeros,
        where p is the previous one
        - p is the previous evidence, and p` is new
        :param last_proof: <int>
        :return: <int>
        """

        proof = 0
        while self.valid_proof(last_proof, proof) is False:
            proof += 1

        return proof

    @staticmethod
    def valid_proof(last_proof, proof):
        """
        Proof of proof: Does hash(last_proof, proof) contain 4 capital zeros?

        :param last_proof: <int>
        :param proof: <int>
        :return: <bool>
        """

        guess = f'{last_proof} {proof}'.encode()
        guess_hash = hashlib.sha256(guess).hexdigest()
        return guess_hash[:4] == "0000"
