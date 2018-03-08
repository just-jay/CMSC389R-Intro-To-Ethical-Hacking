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

The second part of this project involved running command injection on the Briong server. This took a long time, because I thought that you had to use metasploit and was having lots of trouble finding a command injection exploit and then running it. However, after too much time spent on that fruitless endeavor, eventually I went to the Wikipedia page that was linked about command injection and realized that I was going about this all wrong. I found that you can add a semicolon and another command to an input, and the second command will run. This got me thinking that I could try to pass a command as my login info to try and see what was on the server.

So, I tried this. I ran `nc briong.com 45` to get into the server, and was greeted with this login screen: 
![](/img/homework4-ping.PNG)

I then tried a semicolon with an `ls` command to see what was in the current directory, which resulted in this output: 
![](/img/homework4-ls.PNG)

I decided to check the desktop to see if anything was there. I logged in again, this time putting `; ls home/` in the login to see what was located in the home directory

![](/img/homework4-home.PNG)

There's the flag! I made one more command injection call with `cat home/flag.txt` to print out the flag and retrieved this flag -> Good! Here's your flag: CMSC389R-{p1ng_c0mmand_inj3ction}

![](/img/homework4-flag.PNG)

This is a pretty big flaw! Anybody could write any kind of code on this server, deleting files or running their own scripts. One common way to fix this is to use a method called 'sanitizing', where inputted strings with questionable characters (like ;, /, etc.) are either rejected or remove those characters before running them. A second common thing to do is use prepared statements, which cleverly runs input in such a way that it keeps the input from directly affecting the data, keeping it secure. 

I went through alot of the folders in the server and eventualy found the code that Mark uses to tell if a server is up and found that it does indeed run the command that is inputted (specified by $domain) without preparing it or checking if it could contain anything malicious.

![](/img/homework4-startup.PNG)

Let's hope Briong starts stepping up their security!
