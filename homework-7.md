<b>I pledge on my honor that I have not given or received any unauthorized assistance on this homework or assignment. -Jacob Elspas</b>

<h2>Homework #7</h2>
  
Setup: I read the spec and downloaded all of the requisite files

---

Part 1:

1) According to the wikipedia article on passwd, since they all have $1$ they are all encrypted using MD5
2) The hashes are specified in between $'s right after the id, and are as follows: root: XXv.SXDX, admin:GOpCaSQH, bob:vgy72nH3, joe:eZ5SZG9g, mthomp22:SlJR2aEx
3) Passwords for Bob, Joe, and mnthomp22 were all changed: Bob's was last changed on August 30, 1973, Joe's on January 25, 1971, and mnthomp22's on August 11, 1975
4) There are restrictions on Bob, Joe and mnthomp22's passwords: 
Bob: He must wait 5 days to change the password, the password must be changed every 90 days, he will get a warning 7 days before he has to change his password, and the account will be disabled 7 days after the password expires is no login attempt is made.
Joe: He doesn't haev to wait to change his password, the password must be chnaged once every 120 days, he will get a warning 14 days before he has to change his password, and his account will be disabled 3 days after his password expires if he does not change his password.
mnthomp22: He has to wait 99999 to change his password, and he never has to change his password.  
5) Bob last changed his password on October 4, 2024 (suspicious, thats in the future) and Joe last changed his password on March 28, 2018. This was more than 3 days ago, so it appears his account has expired.
6) I decided to use Hashcat to decrypt my password. After gettign into the server via `nc irc.csec.umiacs.umd.edu 1337` I read through the man pages using `hashcat --help`. After that and doing a bit of research online, i was able to use the command `hashcat -m 500 challenge_shadow rockyou.txt` to attempt to decipher some passwords. Almost right away I decrypted `$1$SlJR2aEx$g6TObcH2OTrlx8MIWDZjs.:blink`. However, the code said it would take about a day to run, an i was like 'nuh uh'. So, after running it for about half an hour and getting nowhere, I realized I can switch and try the other software.
I opened John The Ripper in Kali, and after using different commands I ended up unshadowing my hashes with `unshadow passwd.txt shadow.txt>  unshadowed.txt`, I ran `john unshadowed.txt` and, after waiting, got the following passwords:
- root (root)
- blink (mnthomp22)
- saget (bob)
- etude (admin)
- schmo (Joe)
---
Part 2:
I wrote code [here](https://github.com/just-jay/CMSC389R-Intro-To-Ethical-Hacking/blob/master/Homework-7-Part2.py)
 to decrypt the hashes. I went thorugh each lowercase letter of the alphabet and added it to each word in the password list. Then I hashed the whole thing and checked if it was equal to one of the known hashes I was given. If it was equal then I outputted the salt and the password that made that was related to the respective hash.
 My output was as follows:
- Salt:c Password:888888
- Salt:e Password:manchester
- Salt:b Password:vfhbyf
- Salt:y Password:jason1
- Salt:r Password:motorola
 --- 
Part 3
