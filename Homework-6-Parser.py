#!/usr/bin/env python2


#######################################################################################
This is a parser written in Python to parse the fictional fpff file format for CMSC389R
#######################################################################################

import sys
import struct


# You can use this method to exit on failure conditions.
def bork(msg):
    sys.exit(msg)


# Some constants. You shouldn't need to change these.
MAGIC = 0xbefedade
VERSION = 1

word = 4
dword = 8

if len(sys.argv) < 2:
    sys.exit("Usage: python2 stub.py input_file.rcff")

# Normally we'd parse a stream to save memory, but the RCFF files in this
# assignment are relatively small.
with open(sys.argv[1], 'rb') as rcff:
    data = rcff.read()

# Hint: struct.unpack will be VERY useful.
# Hint: you might find it easier to use an index/offset variable than
# hardcoding ranges like 0:8

start = 0; 
end = 3*(word)
magic, version, timestamp = struct.unpack("<LLL", data[start:end])
# From this I found that:
# MAGIC: 0xbefedade
# VERSION: 1
# TIMESTAMP: 1056472735

start = end
end += dword #author is 8 bytes long

author, = struct.unpack("%ds" % dword, data[start:end]) 

start = end
end += word

nsects, = struct.unpack("<L", data[start:end]) 

nsects = nsects + 2 #there are 2 extra (HIDDEN!) sections 

if magic != MAGIC:
    bork("Bad magic! Got %s, expected %s" % (hex(magic), hex(MAGIC)))

if version != VERSION:
    bork("Bad version! Got %d, expected %d" % (int(version), int(VERSION)))


print("------- HEADER -------")
print("MAGIC: %s" % hex(magic))
print("VERSION: %d" % int(version))
print("TIMESTAMP: %s" % int(timestamp)) #ADDED
print("AUTHOR: %s" % author) #ADDED
print("NSECTS: %s" % int(nsects)) #ADDED

# We've parsed the magic and version out for you, but you're responsible for
# the rest of the header and the actual RCFF body. Good luck!

print("-------  BODY  -------")

#offset the rest of the header to start at the body 

section_num = 1

#Parse body here
while nsects != 0 : #if a section exists
	
	#update start and end to get to next section
	start = end
	end += word*2

	#identity the type of section
	stype,slen = struct.unpack("<LL", data[start:end]) #get the first stype and slen

	#update start and end to get the text in the section
	start = end
	end += slen
	
	#Identify the stype and parse the section#
	if stype == 1: #Section ASCII
		#print(slen)
		ascii_str = struct.unpack("%ds" % slen, data[start:end]) 
		print(str(section_num) + " [SECTION_ASCII (0x1)] ")
		print(ascii_str)
	elif stype == 2: #Section UTF8
		print(str(section_num) + " [SECTION_UTF8 (0x2) -- UTF-8-encoded text] ")
	elif stype == 3: #Section Words
		print(str(section_num) + " [SECTION_WORDS (0x3) -- Array of words] ")
		string_str = struct.unpack("<%dL" % (slen/4), data[start:end])
		print(string_str)
	elif stype == 4: #Section DWords 
		print(str(section_num) + " [SECTION_DWORDS (0x4) -- Array of dwords.] ")
		dwords_str  = struct.unpack("<%dQ" % (slen / 8) ,data[start:end])
		print(dwords_str)
	elif stype == 5: #Section Doubles
		print(str(section_num) + " [SECTION_DOUBLES (0x5) -- Array of doubles.] ")
	elif stype == 6: #Section Coord
		if slen == 16:	
			print(str(section_num) + " [SECTION_COORD (0x6) -- (Latitude, longitude) tuple of doubles.] ")
			coord_str = struct.unpack("<%dd" % (slen / 8), data[start:end])
			print(coord_str)
	elif stype == 7: #Section Reference
		if slen == 4:
			print(str(section_num) + " [SECTION_REFERENCE (0x7) -- The index of another section.] ")
			ref_str, = struct.unpack("<L", data[start:end]) 
			print(("section ref: ") + str(ref_str))
	elif stype == 8: #Section PNG
		print(str(section_num) + " [SECTION_PNG (0x8) -- Embedded PNG image.] ")
		
		#The first eight bytes of a PNG file always contain the following values:
	   	#(decimal)              137  80  78  71  13  10  26  10
  	 	#(hexadecimal)           89  50  4e  47  0d  0a  1a  0a
   		#(ASCII C notation)    \211   P   N   G  \r  \n \032 \n

		p_str = struct.unpack("%ds" % slen, data[start:end])
		png_str = (p_str[0]) #grab the string from the tuple
		p2 = "\211PNG\r\n\032\n" + p_str[0]
		#print(p_str)

		f = open('resultfile.png', 'w')
		f.write(p2)
		f.close()
		print("File Created: resultsfile.png")

	nsects = nsects - 1
	section_num = section_num + 1
	
