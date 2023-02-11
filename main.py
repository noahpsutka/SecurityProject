import sensor
import blockchain
import lightNode
import user
import blockNet
import UImodel
import json
import matplotlib.pyplot as plt
import networkx as nx
import time
import random

# create light nodes
lightNodes = lightNode.LightNode(567)

# dynamically add and register users
while True:
  print("Would you like to add users to your network? y/n")
  answer = input()
  if answer == 'y':
    print('')
    print("Enter new user: ")
    name = input()
    print('')
    print("Enter user ID: ")
    ID = input()
    globals()[name] = user.User(name, ID)
    lightNodes.registerUser(globals()[name].ID)
    print('')
    print("New user:", globals()[name].name,"#" + globals()[name].ID)
    print("")
  elif answer == 'n':
    print("")
    break
  else:
    print("")
    print("Please enter a valid answer!")
    print("")

# create users
Ben = user.User("Ben", 4389)
Noah = user.User("Noah", 1394)
Arjit = user.User("Arjit", 1093)
Alex = user.User("Alex", 2890)
Anderson = user.User("Anderson", 8932)
Heena = user.User("Heena", 9245)

# register users
lightNodes.registerUser(Ben.ID)
lightNodes.registerUser(Noah.ID)
lightNodes.registerUser(Arjit.ID)
lightNodes.registerUser(Alex.ID)
lightNodes.registerUser(Anderson.ID)
lightNodes.registerUser(Heena.ID)

sensors = []

# dynamically add and register sensors
while True:
  print("Would you like to add sensors to your network? y/n")
  answer = input()
  if answer == 'y':
    print('')
    print("Enter sensor name: ")
    name = input()
    print('')
    print("Enter sensor type: ")
    type = input()
    print('')
    print("Enter sensor ID: ")
    ID = input()
    globals()[name] = sensor.Sensor(type, ID)
    sensors.append(globals()[name])
    lightNodes.registerSensor(globals()[name].ID)
    print('')
    print("New sensor:", name, globals()[name].type,"#" + globals()[name].ID)
    print("")
  elif answer == 'n':
    print("")
    break
  else:
    print('')
    print("Please enter a valid answer!")
    print("")

# create sensors
sensor1 = sensor.Sensor("temperature", 345)
sensors.append(sensor1)
sensor2 = sensor.Sensor("pressure", 146)
sensors.append(sensor2)
sensor3 = sensor.Sensor("weight", 903)
sensors.append(sensor3)
sensor4 = sensor.Sensor("temperature", 713)
sensors.append(sensor4)

# register new sensors
lightNodes.registerSensor(sensor1.ID)
lightNodes.registerSensor(sensor2.ID)
lightNodes.registerSensor(sensor3.ID)
lightNodes.registerSensor(sensor4.ID)

# create blockchain network
blocknet = blockNet.BlockNet()

# create blockchain
blockchain = blockchain.Blockchain()

# add blockchain to the network
blocknet.addChain(blockchain)

keys = []

for i, snsr in enumerate(sensors[0:len(sensors) - 4]):
  key_name = "pubKey" + str(i)
  globals()[key_name] = lightNodes.RSA(snsr)
  keys.append(globals()[key_name])
  
# create new RSA algorithm for each sensor
publicKey1 = lightNodes.RSA(sensor1)
publicKey2 = lightNodes.RSA(sensor2)
publicKey3 = lightNodes.RSA(sensor3)
publicKey4 = lightNodes.RSA(sensor4)

keys.append(publicKey1)
keys.append(publicKey2)
keys.append(publicKey3)
keys.append(publicKey4)

# signature = RSA.sign(transaction, privateKey)
encrypted_data = lightNodes.encrypt(sensor4, publicKey4)

# This is the creation of each event on a block
# transaction(%sender, %receiver, %what is being sent)
t1 = blockchain.new_transaction(sensor4.ID,
                                encrypted_data)  # sending encrypted data to

encrypted_data = lightNodes.encrypt(sensor2, publicKey2)
t2 = blockchain.new_transaction(sensor2.ID, encrypted_data)

encrypted_data = lightNodes.encrypt(sensor3, publicKey3)
t3 = blockchain.new_transaction(sensor3.ID, encrypted_data)
blockchain.new_block(12345)

# This is the creation of a new block
encrypted_data = lightNodes.encrypt(sensor4, publicKey4)
t4 = blockchain.new_transaction(sensor4.ID, encrypted_data)

encrypted_data = lightNodes.encrypt(sensor2, publicKey2)
t5 = blockchain.new_transaction(sensor2.ID, encrypted_data)

encrypted_data = lightNodes.encrypt(sensor1, publicKey1)
t6 = blockchain.new_transaction(sensor1.ID, encrypted_data)
blockchain.new_block(6789)

print("Reading sensor data, encrypting, and adding to blockchain network...")
print("Press 'ctrl C' to stop", "\n")
time.sleep(3)

# here we are reading data from a random sensor every second and outputting the  data
num = 0
try:
  while True:
    temp_sensor = int(random.random() * len(sensors))
    encrypted_data = lightNodes.encrypt(sensors[temp_sensor], keys[temp_sensor])
    blockchain.new_transaction(sensors[temp_sensor].ID, encrypted_data)
    num += 1
    if num == 3:
      blockchain.new_block(int(random.random() * 9000))
      num = 0
    time.sleep(1)
    print(encrypted_data)
except KeyboardInterrupt:
  pass

print("\n", "#######################################", '\n')

time.sleep(5)
print('Printing entire blockchain...')
time.sleep(3)
print('')

print("New Blockchain:")
# The chain is a python list of blocks, where each block contains all of the transactions inside it
for blocks in blockchain.chain:
  print(blocks)

print("\n", "#######################################", '\n')

time.sleep(3)

print("Data requested for sensor #2 by Ben")
time.sleep(3)
print('')
print("Verifying user and sensor...")
time.sleep(3)
print('')
print("User and sensor verified by nodes")
time.sleep(3)
print('')
print("Decrypting data...")
time.sleep(3)
print('')

# data acquisition by user and verification of user
if Ben.requestData(lightNodes, sensor2.ID) is True:
  flag = 0
  for block in blockchain.chain:
    for key in block:
      if key == 'timestamp':
        timestamp = block[key]
      if key == 'transactions':
        for allData in block[key]:
          for key, value in allData.items():
            if flag == 1:
              print(timestamp, " ", lightNodes.getData(sensor2.ID, eval(value)))
              flag = 0
            if key == "sensor_ID":
              if value == str(sensor2.ID):
                flag = 1
                
#Blocks are added to a list and converted to a JSON format.
#Previous block data located in blockchain.py was converted to a string format for JSON
jsonStr = []
for blocks in blockchain.chain:
  jsonStr.append(blocks)

  res_dict = {"blockchain": jsonStr}

with open('blockchain.json', 'w') as out_file:
  json.dump(res_dict, out_file, sort_keys=True, indent=4, ensure_ascii=False)

UImodel.buildModel()

G = nx.Graph()

#G.add_node(1)
#G.add_node(2)
#G.add_node(3)
#G.add_node(4)

#4389, 1394, 1093, 2890, 8932, 9245
# Hard coded some connections/transactions between nodes
# Might want to add "weight" to each transaction,
# i.e. how many times the same edge is created ^
G.add_edge(4389, 1394)
G.add_edge(1394, 1093)
G.add_edge(1394, 8932)
G.add_edge(1093, 2890)
G.add_edge(1093, 4389)
G.add_edge(2890, 8932)
G.add_edge(8932, 9245)
userList = lightNodes.getUsers()
G.add_nodes_from(userList)

# G.add_edges_from(#transaction list)
# example ---> G.add_edges_from([(4,2),(2,3),(3,4),(4,2),(2,1)])
### How to create more plots from same nodes / edges
# for loop for each user? create new graph for each maybe?
subax1 = plt.subplot(121)
nx.draw(G, with_labels=True, font_weight='bold')
plt.show()  # may not need this line

#####################################################################