import lightNode

class User:

  # create a new user 
  def __init__(self, name, ID):
    self.name = name
    self.ID = ID

  def requestData(self, lightNodes, sensorID):
    ID = self.ID
    return lightNodes.dataRequest(ID, sensorID)
    