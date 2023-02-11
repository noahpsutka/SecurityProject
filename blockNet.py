class BlockNet:

  # create blockchain network
  def __init__(self):
    self.blockchains = []

  # add blockchain to the network
  def addChain(self, blockchain):
    self.blockchains.append(blockchain)
