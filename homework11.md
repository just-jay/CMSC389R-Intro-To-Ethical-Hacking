<b>I pledge on my honor that I have not given or received any unauthorized assistance on this homework or assignment. -Jacob Elspas</b>

<h2>Homework #11</h2>
  
---
Part 1:

---
Part 2:

For this part, we were given access to a challenge server (which could be accessed by running `nc 167.99.224.34 9998`) and the sript running. Our job was to crack the password. Luckily, we had the source code. Doubly luckily, I didn't even use it to crack the server (but I looked at it afterwards).

The login prompted me for a password, and when my first guess was (inevitably) incorrect it notified me that passwords must be EXACTLY 20 characters and then gave me 2 more tries. I used my hacker-fu skills and guessed random passwords while focusing on the length (becuase of the 'hint' in the error output), going for short, exactly 20 characters, and longer. When I tried a password that was longer than 20 characters, I was rewarded with this flag -> `Authenticated: CMSC389R-{wat_r_u_doing}`. But let's see what actually caused this.
