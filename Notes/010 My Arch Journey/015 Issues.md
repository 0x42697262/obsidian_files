> [!INFO]
> Tags: #arch #arch_issues

----
# 015 Issues

## 2022-11-09
Some sort of issue with `paru` that I have no determined the cause yet.
`paru: error while loading shared libraries: libssl.so.1.1: cannot open shared object file: No such file or directory`

Due to [SSL update](https://www.reddit.com/r/archlinux/comments/yn5o8a/comment/iv7qkme/?utm_source=reddit&utm_medium=web2x&context=3), `paru` needs to be rebuilt. I'll reinstall it soon, or later?

Fixed it:
```sh
:: There are 2 providers available for cargo:
:: Repository extra
   1) rust
:: Repository community
   2) rustup

Enter a number (default=1): 2
resolving dependencies...
looking for conflicting packages...

Packages (1) rustup-1.25.1-2

Total Download Size:   2.86 MiB
Total Installed Size:  8.40 MiB
```


## 2022-11-08
Arch did not shutdown yesterday due to XORG issues... forced my laptop to shutoff.