#!/usr/bin/env python


from Crypto.Cipher import AES
import base64
import os

# ENTRY_ATTRIBS is a list of tupples.
# each tupple contains the attribute name and it's description
ENTRY_ATTRIBS = [('name', 'Name'), ('url', 'URL'), 
    ('UserName', 'User Name'), ('password','Password'),
    ('note','Note'), ('test','Test')]

### Encryption Stuff
# the block size for the cipher object; must be 16, 24, or 32 for AES
BLOCK_SIZE = 32

# the character used for padding--with a block cipher such as AES, the value
# you encrypt must be a multiple of BLOCK_SIZE in length.    This character is
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

class Entry:
    """Account data container"""
    def __init__(self,name):
        for i in range(len(ENTRY_ATTRIBS)):
            setattr(self, ENTRY_ATTRIBS[i][0], '')
        # Populate the name with the real value
        self.name = name
    def __str__(self):
        message = ''
        for i in range(len(ENTRY_ATTRIBS)):
            (attrib,desc,value) = self.fetch_attr(i)
            message += attrib + ": " + value + "\n"
        return message
    def fetch_attr(self,i):
        attrib = ENTRY_ATTRIBS[i][0]
        desc = ENTRY_ATTRIBS[i][1]
        value = getattr(self, attrib)
        return (attrib,desc,value)
    def edit_entry(self):
        print "Editing: " + self.name + "\n"
        for i in range(len(ENTRY_ATTRIBS)):
            (attrib,desc,value) = self.fetch_attr(i)
            print str(i) + " " + desc + ": " + value
        choice = input("Enter number to edit: ")
        setattr(self, ENTRY_ATTRIBS[choice][0],
            raw_input(ENTRY_ATTRIBS[choice][1] + ": "))
class Folder:
    def __init__(self,name):
        self.name = name
        self.nodes = {}  # Can be Entry or Folder
    def __str__(self):
        message = "Branch Name: " + self.name + "\n" \
            "Nodes: "
        for node in self.nodes:
            message += node.name + ","
        return message




# Enter the string to encode
#data = raw_input('Enter string to be encoded: ')


# encode a string
#encoded = EncodeAES(cipher, data)
#print 'Encrypted string:', encoded

# decode the encoded string
#decoded = DecodeAES(cipher, encoded)
#print 'Decrypted string:', decoded

#print "Enter data to be encrypted"
