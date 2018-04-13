<b>I pledge on my honor that I have not given or received any unauthorized assistance on this homework or assignment. -Jacob Elspas</b>

<h2>Homework #7</h2>
  
---
Part 1:
I started by logging into the servr at `nc 159.89.236.106 5678` and playing around with the different options. 

---

Part 2: 
For part 2, I satrted by looking for a website to encrypt something with a PGP key, and I conveniently found this: https://www.igolder.com/pgp/encryption/. I then generated a public and private key (which can be found [here](public-and-private-pgp-keys)) and decided on a message that I was going to encrypt (I chose the first paragraph from Harry Potter): 

"Mr. and Mrs. Dursley, of number four, Privet Drive, were proud to say that they were perfectly normal, thank you very much. They were the last people you’d expect to be involved in anything strange or mysterious, because they just didn’t hold with such nonsense."

I encrypted my message with the public key ([encrypted message](encrypted-pgp-message)) and sent it to the challenge email address, pgpassignment@gmail.com
. I then received [this](received-encrypted-pgp-message) encrypted message, which once I decrypted with my private key read `CMSC389R-{th3_boy_wh0_PGPd}`. I really liked how the key related to the message I'd sent, what a fun surprise!
