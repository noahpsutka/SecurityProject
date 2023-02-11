# This chain is a single chain blockchain model
from pyvis.network import Network
import networkx as nx
import json

#Initialized data
counter = " "
prevBlock = "0"

def buildModel():
  file = "blockchain.json"
  #Loads all data located in the blockchain.json file
  def get_data():
      with open (file, "r") as json_file:
          data = json.load(json_file)
          return data["blockchain"]

  def map_data(blockchainData, ep_color="#03DAC6", ms_color="#da03b3", edge_color="#018786", senderEdgeColor="#018786"):
      global counter, prevBlock
      g = Network()
      g = nx.MultiGraph()
      for blockchain in blockchainData:
          block = blockchain["index"]
          if int(block) > 1:
            g.add_edge(block, prevBlock, color=senderEdgeColor)

          transactions = (blockchain["transactions"])
          previous = blockchain["previous_hash"]
          g.add_node(block, color=ep_color, title="Block: " + blockchain['index'] + "\n Previous Hash: " + previous + "\n Proof: " + blockchain['proof'] + "\n Timestamp: " + blockchain['timestamp'] + " GMT")
          for transactionData in transactions:
              g.add_node(transactionData["sensor_ID"]+str(counter), color=ms_color, title="Sensor ID Number: " + transactionData["sensor_ID"])
              g.add_node(str(counter), color="#FF7311", title="Encrypted Data: " + transactionData["data"])
              g.add_edge(block, transactionData["sensor_ID"]+str(counter), color=senderEdgeColor)
              g.add_edge(transactionData["sensor_ID"]+str(counter), str(counter), color=edge_color)
              counter = counter + " "
          prevBlock = block

      nt = Network(height="1500px", width="100%", bgcolor="#222222", font_color="white",directed=True)
      nt.from_nx(g)
      nt.set_edge_smooth('dynamic')
      nt.barnes_hut()
      nt.repulsion()
      nt.show("blockchainGraphic.html")

  epp_data = get_data()
  map_data(blockchainData=epp_data)