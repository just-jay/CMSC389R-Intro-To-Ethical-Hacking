<b>I pledge on my honor that I have not given or received any unauthorized assistance on this homework or assignment. -Jacob Elspas</b>

<h2>Homework #11</h2>
  
---
Part 1:

stackexchange: After looking through this file in radware2 and locating the main method, I realized that all it was doing was assigning different hex values to various bytes and XORing them a few times. I tried calculating this out by hand to figure out what was going on, and I got close, but a few things were still off. I asked a TA for help and then took another crack at it. 

Eventually, I was able to calculate what each byte 'section' had in it:

- 1 -> bd xor c0 = 7d -> }
- 2 -> bd xor d8 = 65 -> e
- 3 -> FF xor 86 = 79 -> y
- 4 -> 5f xor 24 = 7b -> {
- 5 -> 87 xor aa = 2d -> -
- 6 -> 6d xor 3f = 52 -> R
- 7 -> dd xor e4 = 39 -> 9
- 8 -> 7d xor 45 = 38 -> 8
- 9 -> e8 xor db = 33 -> 3

reading from bottom to top, we can see the flag: 389R-{ye}

onebyone: For this part I also started by using r2. By this point I'd gotten better at using it, so I quickly found the main function and looked at it in the graph visualizer format (by running  `o main` and then `V`). I read through the visuals, and found the following characters: `0,e,c,3,},-,9,n,8,i,R,{` highlighted in red. I could immediately tell that this was part of the flag, and that it would look something like this: `389R-{?????}`. I played around with the extra letters, and got `nice0 and 0nice`

---
Part 2:

For this part, we were given access to a challenge server (which could be accessed by running `nc 167.99.224.34 9998`) and the sript running. Our job was to crack the password. Luckily, we had the source code. Doubly luckily, I didn't even use it to crack the server (but I looked at it afterwards).

The login prompted me for a password, and when my first guess was (inevitably) incorrect it notified me that passwords must be EXACTLY 20 characters and then gave me 2 more tries. I used my hacker-fu skills and guessed random passwords while focusing on the length (becuase of the 'hint' in the error output), going for short, exactly 20 characters, and longer. When I tried a password that was longer than 20 characters, I was rewarded with this flag -> `Authenticated: CMSC389R-{wat_r_u_doing}`. In retrospect, I got <i> really </i> lucky. So let's see what actually caused this.

What this code does is take an input from the user, and checks if it the first 20 chars match the password. if so, it'sdoes a bitwise of with 1 and sets the flag (so essentially the flag gets set to 1). Then, it checks if the flag was set to 1, and if so it gives the flag. 

The first odd thing here is that that is that READ_SIZE is 1 greater than BUFFER_SIZE. Also, the line where we declare the char buffer array is right below the line where we make the flag (called 'valid' in the code). So, perhaps if we read more than BUFFER_SIZE chars into the buffer it will get run over and set the valid/flag variable? Then later on, when they check if valid is true, if we ran it over with some other numerical input, it will evaluate to true (becuase `if(any number greater than 0) == true)`). Indeed this is what I did.

Consider the input `111111111111111111111` (21 1s). It puts 20 1s into the buffer, and the overflow gets placed into valid. Then when `if(valid)` gets run it evaluates to true, and gives us the flag. 
