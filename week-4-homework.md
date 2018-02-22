<b>I pledge on my honor that I have not given or received any unauthorized assistance on this homework or assignment. -Jacob Elspas</b>

Homework #2

[Question 1] Hi Mark! Thanks for reaching out to me. I’d be happy to help you fix up some of the vulnerabilities of your site. There are three main things that I think would be the most beneficial in fixing, your passwords, putting data on the internet (IP addresses and usernames), and closing your ports.

The main issue was that your password was not very secure. I used a brute-force algorithm to crack it, but it was a) in a database of words which is already a bad sign and b) blink182 is a short and not very secure password, with only 5 letters and three numbers following it. In fact, the online password checker https://howsecureismypassword.net/ shows that it would be cracked instantaneously, that’s how insecure it is. Instead, I would recommend generating a secure password from any site online (for example https://passwordsgenerator.net/) and then committing it to memory or using a secure online password manager like google smart lock or any other service.

The second issue I wanted to address was the fact that you had a git commit that was unintentional, and from there I was able to gather some information about your info, specifically your IP address. Whenever you are pushing data of any kind to the internet where the public can view it, you should make sure that you don’t have anything in your submission that could be sensitive. One thing that you could do is just delete the submission and upload one without with the IP, to prevent further people from discovering your vulnerability. Alternatively, you could keep all your sensitive information in a test file that you keep locally on your machine and have the files that you want to push to GitHub refer to those private test files. Furthermore, you used your username “mnthomp22” almost exclusively for both your personal and business dealings, so if you make a different one for your server that is something else that you can and should keep private.

Lastly, you left port 1337 open, which enabled me to connect to and then break into your server. This is something that you would want to close. You can use a TCP and UDP port scan to detect which ports are open and the daemons (services) running on them, and them stop those services to close down the port or configure it to a different, safer setting. 

If you have any other question, let me know. Hope this helps!

-- Your friendly neighborhood white hat hacker

[Question 2] My understanding is that there is not a very large ethical distinction between HIBP and Shodan/Cersys, however some still does exist. They both use different methods to provide some information about those whose security has bene breached, but not enough to compromise that individual or group. However, Shodan and Cersys seem to be a bit less secure and also a bit less ethical because they tell you what exploits are possible even if they don’t tell you how to do them. As such, this seems to be a bit unsecure, because if you know what vulnerabilities exist in a system it is easier to try and perform those exploits on a system. In contrast, HIBP is able to let people know if they have been the subject of an attack, which from an ethical perspective is great because they are providing a service to notify people of something that they might be unaware about.

