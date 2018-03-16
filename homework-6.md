<b>I pledge on my honor that I have not given or received any unauthorized assistance on this homework or assignment. -Jacob Elspas</b>

<h2>Homework #6</h2>
  
Setup: I started by downloading the requisite fpff file and the python stub to develop.

---

Part 1: I read through the stub, as well as the provided resources on fpff. 
I used the provided stub to write a parser for the fpff file format. It is included in this repository and can be found [here](https://github.com/just-jay/CMSC389R-Intro-To-Ethical-Hacking/blob/master/Homework-6-Parser.py)

Via the code I wrote and used I found the following:

1) foo.fpff has a Unix timestamp of 1056472735, which when converted becomes Tuesday, June 24, 2003 12:38:55 PM (according to my current time zone)
2) The author of the file is mnthomp
3) The file says it has 9 sections. However, after a hint from an instructor, I realized there were actually two more, for a total of 11 sections
4) My code returned the output below
![](/img/Header_And_Sections.PNG)

5) There are 3 hidden flags in this file.
The first flag was in the PNG that I got from section 8. After spending waay to long trying to get it into a png format using Image, Pip and PIL, I took a different route and got it into a file titles resultsfile.png. Opening it up revealed the flag!

![](/img/resultfile.png)

The flag in section 10 looked a lot like the one in a past project, which was encoded in base64. I decided to try and decode it, and I got the following: CMSC389R-{h1dd3n-s3ct10n-1n-f1l3}. Boo Yah!

The second flag was the hardest for me. I tried base64 again, but it didn't work. I eventually made my way to [this](https://en.wikipedia.org/wiki/Binary-to-text_encoding) wiki page and went through every method of encoding trying to decipher the string, until finally base32 worked, giving me the following decryption: "not a UTF-8 string"

I found the online flag by googling the 2 pairs of coordinates found in sections 3 and 7. They brought me to the Florida Keys, and I spent quite a while looking through the online nearby thing, the Alabama Jacks Seafood Restaurant. Eventually I gave up and moved to the other coordinate, which brought me right off UMD campus. BY this point I realized that there was a restaurant theme going on. I looked at the output of the fpff file and noticed it related to restaurant reviews. I looked back at Alabama Jacks and Pupuseria La Familiar (a restaurant in the area), before eventually (after too much time trying lol) finding a review on Yelp about Food Factory by Mark T. It read: "I go here every Friday. Awesome Tandoori chicken, plus their mango lassi is great. Would highly recommend. CMSC389r-{t4nd00r1-ch1ck3n}"

---

An Extra Flag I Found By Accident  
I realized that all the flags had cmsc389 in them in plaintext, so I decided to google that to see what would come up. I ended up finding a flag that was never used for the project, but was just my instructor playing around with some ideas he had. It was a review of Rose Hill Cemetary on TripHobo and it read: "Saw some mountain bikers having fun here. RIP Duane Allman CMSC389R-{wh1pp1ng-p0st}"
