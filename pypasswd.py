#!/usr/bin/env python

from Crypto.Cipher import AES
import base64
import os

### Encryption Stuff
# the block size for the cipher object; must be 16, 24, or 32 for AES
BLOCK_SIZE = 32

# the character used for padding--with a block cipher such as AES, the value
# you encrypt must be a multiple of BLOCK_SIZE in length.  This character is
# used to ensure that your value is always a multiple of BLOCK_SIZE
PADDING = '{'

# one-liner to sufficiently pad the text to be encrypted
pad = lambda s: s + (BLOCK_SIZE - len(s) % BLOCK_SIZE) * PADDING

# one-liners to encrypt/encode and decrypt/decode a string
# encrypt with AES, encode with base64
EncodeAES = lambda c, s: base64.b64encode(c.encrypt(pad(s)))
#EncodeAES = lambda c, s: c.encrypt(pad(s))
DecodeAES = lambda c, e: c.decrypt(base64.b64decode(e)).rstrip(PADDING)
#DecodeAES = lambda c, e: c.decrypt(e).rstrip(PADDING)

# generate a random secret key
secret = os.urandom(BLOCK_SIZE)

# create a cipher object using the random secret
cipher = AES.new(secret)
#### Encryption Stuff

class Node:
  """Account data container"""
  def __init__(self):
    self.system = ''
    self.url = ''
    self.UserName = ''
    self.password = ''
    self.note = ''
  def __str__(self):
    message = "System: " + self.system + "\n"
    message = message + "URL: " + self.url + "\n"
    message = message + "UserName: " + self.UserName + "\n"
    message = message + "Password: " + self.password + "\n"
    message = message + "Note: " + self.note
    return message

class Tree:
  def __init__(self):
    self.nodes = {}

# Enter the string to encode
data = raw_input('Enter string to be encoded: ')


# encode a string
encoded = EncodeAES(cipher, data)
print 'Encrypted string:', encoded

# decode the encoded string
decoded = DecodeAES(cipher, encoded)
print 'Decrypted string:', decoded

#print "Enter data to be encrypted"
