# do `curl http://starship.python.net/~gherman/programs/md5py/md5py.py > md5.py`
# if you do not have it from the git repo
import md5py
import socket
import re

host = "159.89.236.106"
port = 5678    # port give

# use these to connect to the service
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))

#####################################
### STEP 1: Calculate forged hash ###
#####################################

message = 'Howdy'    # original message here
legit = '' # a legit hash of secret + message goes here, obtained from signing a message

#chose option 1
data = s.recv(1024) 
s.send("1" + '\n') 

#send the message
data = s.recv(1024)
s.send(message + '\n') 

#get the has
data = s.recv(1024) 
my_hash = data[39:].strip()
print(my_hash)

#continue to main 'menu'
data = s.recv(1024) 
legit = my_hash

# initialize hash object with state of a vulnerable hash
fake_hash = md5py.new('A' * 64)
fake_hash.A, fake_hash.B, fake_hash.C, fake_hash.D = md5py._bytelist2long(legit.decode('hex'))

malicious = 'Hack'  # put your malicious message here
# update legit hash with malicious message
fake_hash.update(malicious)

# test is the correct hash for md5(secret + message + padding + malicious)
test = fake_hash.hexdigest()

#############################
### STEP 2: Craft payload ###
#############################

# TODO: calculate proper padding based on secret + message
# secret is 6 bytes long (48 bits)
# each block in MD5 is 512 bits long
# secret + message is followed by bit 1 then bit 0's (i.e. \x80\x00\x00...)
# after the 0's is a bye with message length in bits, little endian style
# (i.e. 20 char msg = 160 bits = 0xa0 = '\xa0\x00\x00\x00\x00\x00\x00\x00\x00')
# craft padding to align the block as MD5 would do it
# (i.e. len(secret + message + padding) = 64 bytes = 512 bits

#make the padding

# 11 bytes of secret data (message+secret)
# 45 bytes of padding
# 8 bytes of endian data

#length of message: 15 bytes

padding = '\x80' #start with the x80 
for i in range(0,44): # add all the x00s
	padding += '\x00'
padding += '\x58\x00\x00\x00\x00\x00\x00\x00' #endian field (8 bytes)

# payload is the message that corresponds to the hash in `test`
# server will calculate md5(secret + payload)
#                     = md5(secret + message + padding + malicious)
#                     = test
payload = message + padding + malicious
#send option 2
s.send("2" + '\n')
data = s.recv(1024)

#send the fake test
s.send(test + '\n')
data = s.recv(1024)

#send the payload
s.send(payload + '\n')
data = s.recv(1024)

#return the results
data = s.recv(1024)

print(data)

s.close()	
# send `test` and `payload` to server (manually or with sockets)
# REMEMBER: every time you sign new data, you will regenerate a new secret!