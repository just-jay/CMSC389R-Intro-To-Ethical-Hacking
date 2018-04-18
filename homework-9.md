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
3. For this level, I used a similar idea that I used for Part 1 of the homework. I knew I needed to insert soemthing in the searchbar, specifically at the frame number. I saw the the Javascript that was handling parsing the GET request looked like this: `html += "<img src='/static/level3/cloud" + num + ".jpg' />";`. I thought that if I could add an alert attribute to the img tag and cause the img to 'fail' it would make the alert. So I constructed my input (`'onerror=alert("XSS")/>";//`) and inputted it into the search bar like this: `https://xss-game.appspot.com/level3/frame#'onerror=alert("XSS")/>";//` What this did was make the image tag invalid by not providing it a number, add an onerror tag to run upon said error, an end-of-tag marker for the HTML and a comment to get rid of the rest of the Javascript command. This worked (woohoo!) and I moved on to th next level
4. This one took a while for me to figure out, and a bit of googling too. After trying various onerror and other commands from previous questions, I read the hints and realized where the command I was going to inject would go, and how to start it. However, this still took me quite a while to figure out. It was only after _way_ too long and after googling more about XSS and Javascrupt that I realized what I had to do was inject another command into the onload part of the command (I didn't realize you could have more than one command there). This led to me creating the input `');alert('XSS`, which would fail the function call, then do the alert call while still being syntactically valid (the rest of the alert call, `');`, is supplied by the original code). Onto the next one!
5. This one took a while as well. I eventually too the hints and was able to figure out how to run javascript without using onclick(). From there it wasn't that hard to craft a link in order to get the value of the next parameter to be run and make the alert: `next=javascript:alert("XSS")`
6. The last one! Like with the others, I found myself struggling on this too. I was able to discover that I could get something without an `http` or `https` tag to run, so I eventually realized how to use the 4th hint they gave and craft this part of the link `frame#//google.com/jsapi?callback=alert` that exceuted an alert, thereby finishing the challenge

Overall, I found this challening. I did end up learning alot about XSS and how it works though, so thats what counts
