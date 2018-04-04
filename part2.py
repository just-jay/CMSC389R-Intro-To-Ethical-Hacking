#!/usr/bin/env python
#-*- coding:utf-8 -*-

# importing a useful library -- feel free to add any others you find necessary
import hashlib
from string import ascii_lowercase
wordlist = "passwords.txt" # download the wordlist and enter the ABSOLUTE path here
f = open(wordlist) #open the wordlist
hashlist = ["7e0b893f2448c8476a0dd5d34f89a88f3ffa24e70f03e47d4de98f23bbfa0a2d4c89a84ceae6e3eabc8570a0027babd726611100df19335373665ff0eb1a13e6",
			"71ed98458540dd6aff8cc2683c6450310f3a2d4bddd8c0bca7dcbe002e70614671127a59a543139fc40ed7f73ac259a3fdcb0426ff8433fe85e7adf3fa047771",
			"c7072e350fa8794e78b864d6cb3fe06281e933743d26f00c0ec55a66e7394cb8e0ee0840d7fd0aa80177bc5c7e1bfe65c6d73e7491243959bf738957c97f125a",
			"765d54e7e4cc23ea3cf9c820844d192c8cc80fc20701cd16fb7a0b9dafc5f8a8d526534ae0cea78d6b878ca4beb7a6fbdcdf012a0ec95d8067a015a6327153dd",
			"9164498b4652250420d3b3ae2a121dd58750598740f79080b3c45f3d6c25a4f5f840f506d4427453ee85c6f79c0c674f45b1c21933f3161c4fa674eebf9e2f00"]

for line in f:	
	for c in ascii_lowercase:
		h = hashlib.sha512(c + (line.rstrip())).hexdigest() #remove all end tags from the line, add the salt, and hash
		if h in hashlist:
			print "Salt:" + c + " Password:" + line 
f.close()