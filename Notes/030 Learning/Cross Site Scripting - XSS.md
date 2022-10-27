> [!INFO]
> Status:
> Tags: #CTF #Cross_Site_Scripting

----
# Cross Site Scripting - XSS
Check this [video](https://www.youtube.com/watch?v=KHwVjzWei1c) or [blog post](https://liveoverflow.com/do-not-use-alert-1-in-xss/) by LiveOverflow. TL;DR, don't use `alert(1);` but use 
```js
alert(document.domain);
// or use
alert(window.origin);
```
Even if XSS works, it does not imply that a vulnerability exists. It might be sandboxed.