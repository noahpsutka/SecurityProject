import rsa

class RSA:

# each device has its own public and private keys
  def __init__(self, ID):
    self.ID = ID

  def generateKeys(self):
    length=1024 
    (self.publicKey, self.privateKey) = rsa.newkeys(length)
    return self.publicKey

  def encrypt(self, plaintext, key):

    plaintext = str(plaintext)
    
    # encrypt plaintext
    return rsa.encrypt(plaintext.encode('ascii'), key)

  def decrypt(self, ciphertext, key):
    try:
      return rsa.decrypt(ciphertext, key).decode('ascii')
    except:
      return False

# nodes will sign the transaction with a private key and broadcast it to the network 
  def sign(message, privatekey):
    return rsa.sign(message.encode('ascii'), privatekey, 'SHA-1')

# the trusted node verifies the signature with the source public key
  def verify(message, signature, publickey):
    try:
      return rsa.verify(message.encode('ascii'), signature, publickey) == 'SHA-1'
    except:
      return False
