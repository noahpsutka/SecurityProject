import hashlib
import json
import RSA
from datetime import datetime
# hashlib is used for encryption
# json is used to format the blocks
# datetime will provide the timestamp for the block

class Blockchain(object):
    def __init__(self):
        self.chain = []
        self.waiting_transaction = []

        self.new_block(previous_hash=" ", proof=100)

# Create a new block listing key/value pairs of block information in a JSON object. Reset the list of waiting transactions & append the newest block to the chain.

  # len = block index #
  # proof = block object # that was passed in creation: ex: blockchain.new_block(6789) -> proof = 6789
    def new_block(self, proof, previous_hash=None):
        current = datetime.now()
        block = {
            'index': str(len(self.chain) + 1), 
            'timestamp': current.strftime("%m/%d/%Y %H:%M:%S"),
            'transactions': self.waiting_transaction,
            'proof': str(proof),
            'previous_hash': previous_hash or self.hash(self.chain[-1]),
        }
        self.waiting_transaction = []
        self.chain.append(block)

        return block

#Search the blockchain for the most recent block.

    @property
    def last_block(self):
 
        return self.chain[-1]

# Add a transaction with relevant info to the 'blockpool' - list of pending transactions's. 

    def new_transaction(self, ID, data):
        encrypted_data = self.receiveData(data)
        transaction = {
            # 'sender': sender,
            # 'receiver': receiver,
            'sensor_ID': str(ID),
            'data': encrypted_data
        }
        # signature = RSA.sign(transaction, privateKey)
        self.waiting_transaction.append(transaction)
        index = int(self.last_block['index'])
        return index + 1

# receive one block. Turn it into a string, turn that into Unicode (for hashing). Hash with SHA256 encryption, then translate the Unicode into a hexidecimal string.

  # This is the default sha256 encryption that is used in the documentation for blockchain
  # We would want to implement the encryption from main into this blockchain
    def hash(self, block):
        string_object = json.dumps(block, sort_keys=True)
        block_string = string_object.encode()

        raw_hash = hashlib.sha256(block_string)
        hex_hash = raw_hash.hexdigest()

        return hex_hash

    def receiveData(self, data):
      
        return str(data)

