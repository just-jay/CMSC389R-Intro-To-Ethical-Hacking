#!/usr/bin/env python
#-*- coding:utf-8 -*-

# importing useful libraries -- feel free to add any others you find necessary
import socket
import hashlib
import re

host = "129.2.94.135"   # IP address of irc.csec.umiacs.umd.edu
port = 4444    # port give

# use these to connect to the service
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))

for i in range(0,3):
	data = s.recv(1024) #get the data
	sub_data = re.findall(r'\d+ [-+]? \d+', data) #regex to grab the equation part of the string
	print data #print the data
	sum = eval(sub_data[0]) #compute the arithmetic
	h = hashlib.sha256((str(sum)).rstrip()).hexdigest() + '\n' #compute the hash
	s.send(h) #send the hash to the socket

#prompts three times, now we can get the flag
data = s.recv(1024) #get the data
print data #print the data

# close the connection
s.close()