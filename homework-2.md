This is the submission I made for my homework 2 assignment. The assignment was essentially that we were given just a username, and we had to reserach as much as we could about that person, and eventually that led us to a server which we then were able to hack into.

Homework 2 – Briong70
I pledge on my honor that I have not given or received any unauthorized assistance on this assignment. -Jacob Elspas

Part 1 – The Briong Server
1)	After googling ‘Briong70’, I found a link to their github page, and one of their commits was labeled “whoops! Shouldn’t have pushed that.” I thought this suspicious, so I looked at the commit and found an IP address embedded in the code, 129.2.94.135.
2)	 I was using a TCP Port Scan from pentest-tools.com and it gave me the option to find the operating system. I did so and it told me that the system was running Ubuntu Linux.
3)	I did a whois search on the IP address to find out that the server is located at Office of Information Technology Patuxent Building on the University of Maryland campus.
4)	Mark N Thompson owns this server. I found his name on the github repository and matched it with a post he’d made on twitter.
5)	Twitter account: https://twitter.com/mnthomp22 - via googling mnthomp22
Gina Thompson, Briong70 developer: https://www.facebook.com/ginathompsonlolz - via googling briong70
Mark’s Facebook: https://www.facebook.com/profile.php?id=100024289025573	 - Mark is a friend of Gina’s
Both of them went to the University of Maryland
Possible email: mnthomp22@tuta.io -from the website at 129.2.94.135
Possible phone number: 555-555-5555 – from the website at 129.2.94.135
Possible Address: 1234 Secure Road, New York, New York – from the website at 129.2.94.135
6)	I found 2 open ports by using pentest-tools.com’s port scan with nmap results, Ports 22 and 80. I also suspected port 1337 because I found a pastebin associated with mnthomp22 that mentioned that port, so I checked if that port was open, and it was (https://pastebin.com/Db44Ujg2). 
7)	 I went to shodan.io and typed in the IP address that I had found. It then returned irc.cse.umd.edu, which linked back to the IP. 
8)	 Via Shodan I found that HTTP is being run on port 80. Via pentest-tools.com I found that port 22 was running ssh. Port 1337 is open but I’m not sure what it’s running, the only information I could find about said that it was ‘garbage’.
9)	One of the hidden files I discovered on the website was a folder called ‘secret’. I found it because I checked http://129.2.94.135/robots.txt to see if any files had been hidden. 
I used inspect element, and based off of the comments left in the HTML I went to the flag.txt file, where I got the following message: Good – nice find! CMSC389R-{r0b0ts_t00k_m3_h3r3}.
10)	An SSH Fingerprint is a hash of the server’s public key. It is used to help authenticate users and allow them access to the server.  I tried SSHing into the server using ssh root@129.2.94.135. I got denied because I don’t have permission, but it still outputted the SSH Fingerprint : SHA256:TLK7NktVYm7saUoLLejccSd3AAqrMWJGEYuwHKWFatU
Part 2
I first logged into Kali and got the python script into a text editor, along with the file for all the potential passwords. I then guessed that the username was mnthomp22, because it had been the username for other accounts. Then I added a bit more python code that would go though the file, testing each password in the file with the username on port 1337 of the server until it passed. 
Eventually, the password blink182 passed. I then logged into the server with that password, and after exploring the directory I found that there was a flag.txt file in the home directory. I opened flag.txt and is read “Good! Here’s your flag: CMSC389R-{vu1n_sc4n_t0_pwn}”
 
 

Part 3
Pastebin is a service wherein someone can send a chunk of text (i.e. code) to someone else by copying it into a textbox on the site, that then generates a link that the user can send to their friend, thereby giving them access to their text. The issue with this is that the default setting for generating a URL that gives someone access to your code is public, and if a user isn’t careful they could copy sensitive data like a list of usernames and passwords and then make it public to the whole internet, while they assume that it is private. Someone could then use OSINT to find your paste online, perhaps by googling specific phrases they suspect would be in the document, and you would never know. 
A very simple OPSEC technique to this is to just be mindful when you are making your link and if there is anything sensitive that you make it private instead of public. Alternatively, you could use a BYOD policy (Bring Your Own Device) and only share sensitive material while the two of you are in person, to prevent anyone online from capturing your data. 
