---
type: note
tags: [rant, WINE, linux]
---

# Fuck WINE associations
It's annoying to have to open a PDF file or an image expecting you have it opened in your image editor but noooooooo it fucking opens to WINE instead on a fucking Internet Explorer piece of crap. Here's the solution provided by this [website](https://appuals.com/unregister-wine-file-associations-linux/) which basically just remove the fucking wine-extensions as is.

```sh
rm -f ~/.local/share/applications/wine-extension*.desktop
rm -f ~/.local/share/icons/hicolor/*/*/application-x-wine-extension*
```
1st line removes all wine associations when you open a file based on an extension. 2nd line removes any icons associated with it. As for my case, I don't think I need to remove every wine extension since maybe ***osu!*** needs it and as for the icons which *may* be used by Lutris.

Next, remove the cache files
```sh
rm -f ~/.local/share/applications/mimeinfo.cache
rm -f ~/.local/share/mime/packages/x-wine*
rm -f ~/.local/share/mime/application/x-wine-extension*
```
and update the cache
```sh
update-desktop-database ~/.local/share/applications
update-mime-database ~/.local/share/mime/
```
Although, I don't think I need to remove them because.... ***osu!*** of course. Maybe I'd need teh rest, who knows. I just need it to not fucking open images in a fucking internet explorer crap. 

In hindsight, I should've configured my arch to open certain files to certain programs but ehh that's an issue for the next rant.