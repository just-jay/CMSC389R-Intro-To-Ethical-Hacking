<b>I pledge on my honor that I have not given or received any unauthorized assistance on this homework or assignment. -Jacob Elspas</b>

<h2>Homework #9</h2>
  
---
Part 1: 
The homework took place at https://bigbenbargains.biz/briongshop. I first attempted some XSS on the site, but had no luck. The I realized the the ID variable was changing in the serach bar depending on which item I looked at. I tried various fauly input (ex. -1) as an id but nothing worked. Eventually, with the help of the slides, I realized that I would need to use some sort of SQL Injection. Based off of the slides I was able to assume that the SQL that read the IDs loked something like this: `SELECT * FROM table where id = '". $id . "'
`. From this I was able to realize that I could use the input `id=2'OR'1`, which would evaluate to id=TRUE, thereby accomplishing SQL injection and dumping the whole table. I did this and was reqarded with the flag: FLAG CMSC389R-{u_ar3_th3_SQL_ninja} $1337.37. A pretty expensive price for a flag, so it's a good thing I found it for free!

---

Part 2:
For this part we had to complete all 6 levels of https://xss-game.appspot.com/. Here is a breakdown of each level:

1. The first level involved trying to get an alert to pop up on the screen. The was accomplished simply by inputting some javascript into the serach bar on the screen and running this query `<script> alert("XSS!"); <\script>`
2. For the second level I had some trouble fiuring out how to keep the browser to recognize the javascript. Eventually I took the hint and got lead [here](https://www.owasp.org/index.php/XSS_Filter_Evasion_Cheat_Sheet#IMG_onerror_and_javascript_alert_encode), and when I ran that code the alert worked and I got directed to the next level. After looking at the hints, I realized that this command is more what they were looking for: `<img src="image.gif" onerror=alert("XSS")>`
3.
