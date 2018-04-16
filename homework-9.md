<b>I pledge on my honor that I have not given or received any unauthorized assistance on this homework or assignment. -Jacob Elspas</b>

<h2>Homework #9</h2>
  
---
Part 1: 
The homework took place at https://bigbenbargains.biz/briongshop. I first attempted some XSS on the site, but had no luck. 

---

Part 2:
For this part we had to complete all 6 levels of https://xss-game.appspot.com/. Here is a breakdown of each level:

1. The first level involved trying to get an alert to pop up on the screen. The was accomplished simply by inputting some javascript into the serach bar on the screen and running this query `<script> alert("XSS!"); <\script>`
2. For the second level I had some trouble fiuring out how to keep the browser to recognize the javascript. Eventually I took the hint and got lead [here](https://www.owasp.org/index.php/XSS_Filter_Evasion_Cheat_Sheet#IMG_onerror_and_javascript_alert_encode), and when I ran that code the alert worked and I got directed to the next level
3.
