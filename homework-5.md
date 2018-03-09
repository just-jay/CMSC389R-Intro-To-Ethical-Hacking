<b>I pledge on my honor that I have not given or received any unauthorized assistance on this homework or assignment. -Jacob Elspas</b>

<h2>Homework #4</h2>

<b>Setup</b>:
The first thing I did was run 
` $ sudo apt install exiftool steghide ` 
in bash in order to get the required packages for this assignment. I also downloaded the three files provided to us that we would be analyzing: `imagefun.jpg`, `fubar.core`, and ```traffic.pcap```. 

<b>Part 1</b>:
The first part of this assignment was to investigate the meatdata of a file called `imagefun.jpg`. The first thing I tried was to run `exiftool imagefun.jpg` to see what I could find in the metadata. Using this, I found a lot of information about the photo:
1) The device that took the photo was an Apple iPhone 6. 
Furthermore, it is running a version of iCamera 1.2.3 which was last updated in 2014. Seeing as that was almost 4 years ago, there may have been security flaws discovered in the software that got fixed in a later update, but because this version is not the most current it is susceptible to some attacks. It’s also an iPhone and not an Android, so whoever took this should probably look into getting into getting a better phone. 

![](/img/exiftool.PNG)

2) This photo was taken in 1984 on January 1st, at exactly 12:12 and 12 seconds. 
This is quite odd, because the first iPhone was released on June 29th, 2007, so someone must have edited the time on the picture. The picture was also taken at these coordinates: 38 deg 55' 1.41" N, 77 deg 1' 42.81" W. This brought me to  street in DC, but I couldn’t find anything of interest at the location. However, since the time the picture was taken had been changed, it is possible that the location had been changed as well.

![](/img/coordmap.PNG)

3) I was going through the commands in the slides and trying different ones when I came upon binwalk. I noticed the description mentioned images, so I thought I’d try it out. So I tried `binwalk -a imagefun.jpg`. The output of this showed that there was a second jpg hidden inside the first!  I spent a while reading about binwalk online and through the `man binwalk` command. Eventaully, I found a command on stack overflow to extract all files, ran it `binwalk –dd=’.*’ imagefun.jpg`, and that extracted the below file to my desktop. First flag found!

Based on the info of the first flag, I assumed that the password was mnthomp22 from previous projects. So I ran `steghide extract -sf imagefun.jpg -xf out.txt` which prompted me for a login. I had run this command previously, but now that I had a password I was set. I typed in mnthomp22, and it wrote the extracted data to out.txt.  I ran `cat out.txt` and was greeted with congrats, you made it here! your flag: CMSC389R-{m4rk's b4d s3cur1ty}. Two flags down! Guess Mark really hasn’t learnt his lesson!

![](/img/binwalk-jpeg.PNG)
![](/img/jpegflag1.PNG)

 --
Part 2
First I opened the core file in notepad just cause and found a bunch of stuff:
-	CORE
-	MNTHOMP_PASSWORD true
-	LINUX
-	IGISCORE
-	/tmp/fubar
-	/lib/x86_64-linux-gnu/libc-2.23.so
-	/lib64/ld-linux-x86-64.so.2
-	libc.so.6 getpid printf chdir sleep
-	__libc_start_main setenv
-	__gmon_start__ GLIBC_2.2.5
-	Ilovenickelback
-	PGP_HIDDEN
-	/usr/local/sbin
-	you should run: sudo gcore -o fubar %d (students ignore this)

It all looked useful, but I knew I needed to do more to figure out what meant what
Next I tried running `strings fubar.core`, which outputted a bunch of the data I had seen in the raw text file. However, a few things stood out that helped me see what was actually happening. Combining that data with what I had found previously, I concluded the following:
1) The OS is (Ubuntu 5.4.0-6ubuntu1~16.04.9) 5.4.0 20160609. The libc is /lib/x86_64-linux-gnu/libc-2.23.so (64 bit linux). 
2) by running `strings fubar.core | grep -P "fubar"`, I found `./fubar`, which implies that the program wasn’t run with any commands, and just executed by itself
3) By running `strings fubar.core | grep -P "\S+=\S+"` I found that MNTHOMP_PASSWORD=ilovenickelback, PGP_HIDDEN=true, EN=true, and PGP_HIDDEN=true
4) I used binwalk again to look through all of the files of fubar.core, and inside I found an image file. So I extracted the files again using the method I described part 1 section 3, and was given this image:

 ![](/img/dudeguy.png)

I also found this: dMark Thompson (You're on the right track if you find this - keep digging class!) <mnthomp22@tuta.io>

--
Part 3

I followed along with the recorded lecture for this part of the assignment. The first thing that I did was open wireshark with the pcap file (`wireshark traffic.pcap`). I filtered the requests with HTTP and from there was able to conclude the following

1) We can see that the ip address of the GET requests came from http://129.2.94.135/, which as we have found in other classes is irc.csec.umiacs.umd.edu.
2) Under the info column of wireshark we see /mnthomp_beedogs.html, so we can assume that the relative url of the page is http://irc.csec.umiacs.umd.edu/mnthomp_beedogs.html
3) I followed the directions and exported all the files. Then I opened the html, and in the browser (using inspect element) I changed the image tags so that the linked to the correct file names:

 ![](/img/beedogs.PNG)

4) While in the html and changing the img tags, i also found the flag as a comment: <!--CMSC389R-{pc4p-4n4lys1s}--> 
5) There is a TCP protocol that got highlighted in crimson red by wireshark. I'm not sure what this means but that sounds liek it's important. I assume wireshark knew what it was doing. Also, since it's TCP that means it must have been involved in some type of packet transfer, which means data was getting sent and its logged via this pcap. Perhaps with some hacking one could trace what was being sent? The file doesn't say but it might be possible.
