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
2) This photo was taken in 1984 on January 1st, at exactly 12:12 and 12 seconds. 
This is quite odd, because the first iPhone was released on June 29th, 2007, so someone must have edited the time on the picture. The picture was also taken at these coordinates: 38 deg 55' 1.41" N, 77 deg 1' 42.81" W. This brought me to  street in DC, but I couldn’t find anything of interest at the location. However, since the time the picture was taken had been changed, it is possible that the location had been changed as well.
3)

![](/img/exiftool.PNG)
![](/img/coordmap.PNG)
 --
Part 2
