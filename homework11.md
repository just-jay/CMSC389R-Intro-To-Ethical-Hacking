<b>I pledge on my honor that I have not given or received any unauthorized assistance on this homework or assignment. -Jacob Elspas</b>

<h2>Homework #11</h2>
  
---
Part 1:

---
Part 2:

For this part, we were given access to a challenge server (which could be accessed by running `nc 167.99.224.34 9998`) and the sript running. Our job was to crack the password. Luckily, we had the source code. Doubly luckily, I didn't even use it to crack the server (but I looked at it afterwards).

The login prompted me for a password, and when my first guess was (inevitably) incorrect it notified me that passwords must be EXACTLY 20 characters and then gave me 2 more tries. I used my hacker-fu skills and guessed random passwords while focusing on the length (becuase of the 'hint' in the error output), going for short, exactly 20 characters, and longer. When I tried a password that was longer than 20 characters, I was rewarded with this flag -> `Authenticated: CMSC389R-{wat_r_u_doing}`. In retrospect, I got <i> really </i> lucky. So let's see what actually caused this.

What this code does is take an input from the user, and checks if it the first 20 chars match the password. if so, it'sdoes a bitwise of with 1 and sets the flag (so essentially the flag gets set to 1). Then, it checks if the flag was set to 1, and if so it gives the flag. 

The first odd thing here is that that is that READ_SIZE is 1 greater than BUFFER_SIZE. Also, the line where we declare the char buffer array is right below the line where we make the flag (called 'valid' in the code). So, perhaps if we read more than BUFFER_SIZE chars into the buffer it will get run over and set the valid/flag variable? Then later on, when they check if valid is true, if we ran it over with some other numerical input, it will evaluate to true (becuase `if(any number greater than 0) == true)`). Indeed this is what I did.

Consider the input 111111111111111111111 (21 1s). It puts 20 1s into the buffer, and the overflow gets placed into valid. Then when `if(valid)` gets run it evaluates to true, and gives us the flag. 
