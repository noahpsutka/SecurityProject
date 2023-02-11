import RSA

class LightNode:
  def __init__(self, ID):
    self.ID = ID

    # create list of rsa algorithms for each sensor
    self.rsa_list = []

    # create list of sensors
    self.sensors = []

    # create list of users
    self.users = []

  def RSA(self, sensor):
    if sensor.ID in self.sensors: # verifying device using regID

      # create new RSA algorithm for each sensor/actuator
      
      newRSA = RSA.RSA(sensor.ID)

      # generate public key and private key for each device
      publicKey = newRSA.generateKeys() # generate public and private keys

      # append new RSA algorithm for sensor
      self.rsa_list.append(newRSA)

      return publicKey      
    else:
      return False

  def encrypt(self, sensor, key):
    if sensor.ID in self.sensors: # verifying device using regID

      for i in self.rsa_list:
        if i.ID == sensor.ID:
          tempRSA = i
          
      data = sensor.type + " " +  sensor.reading()
      
      # encrypt data using device RSA algorithm
      return tempRSA.encrypt(data, key)

    else:
      return False

  def registerSensor(self, sensorID):
    self.sensors.append(sensorID)

  def registerUser(self, userID):
    self.users.append(userID)

  def dataRequest(self, userID, sensorID):
    if sensorID in self.sensors and userID in self.users:

      return True
    else: 
      return False

  def getData(self, sensorID, cipher):
    for i in self.rsa_list:
      if i.ID == sensorID:
        tempRSA = i
          
    # decrypt data using device RSA algorithm
    return tempRSA.decrypt(cipher, tempRSA.privateKey)
    
  def getUsers(self):
    return self.users

  def getSensors(self):
    return self.sensors