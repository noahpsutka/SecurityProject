import random

class Sensor:
  def __init__(self, type, ID):
    self.type = type
    self.ID = ID

  def reading(self):
    return str(round(random.random() * 200, 2))