Tried using Burpsuite on this one and I still cannot figure it out. I will take a look at some walkthroughs... Cheating, I know. 

I used this [writeup](https://github.com/vivian-dai/PicoCTF2021-Writeup/blob/main/Web%20Exploitation/Get%20aHead/Get%20aHead.md) as a guide. I was actually on the right track. However, I only tried `PUT` and `DELETE` methods. [HTTP request methods](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods)

Then, here's the flag:
![[Pasted image 20221027121946.png]]

Okay, so I thought with this hint ![[Pasted image 20221027122043.png]] is that it referred to the colors so I tried using other colors through the POST request.