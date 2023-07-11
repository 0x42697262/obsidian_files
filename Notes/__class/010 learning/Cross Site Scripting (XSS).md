---
type: note
tags: [xss, cross site scripting]
---

# Cross Site Scripting (XSS)
Check this [video](https://www.youtube.com/watch?v=KHwVjzWei1c) or [blog post](https://liveoverflow.com/do-not-use-alert-1-in-xss/) by LiveOverflow. TL;DR, don't use `alert(1);` but use 
```js
alert(document.domain);
// or use
alert(window.origin);
```
Even if XSS works, it does not imply that a vulnerability exists. It might be sandboxed.

**Types**:
1. Reflected XSS
2. Stored XSS
3. DOM Based XSS

> [!INFO]- Check this next time
> https://owasp.org/www-community/Types_of_Cross-Site_Scripting