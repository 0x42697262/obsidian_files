---
title: QEMU
date: 2024-02-06
tags:
  - virtualization
  - virtual-machine
---

# QEMU

---

## Converting from different images

### .ova

Unpack the .ova image format.

```sh
$ tar -xvf <image.ova>
```

That should give extract two files: `.vmdk` and `.ovf.` `.vmdk` needs to be converted into `.qcow2` image format for QEMU to be able to read.

```sh
$ qemu-img convert -f vmdk -O qcow2 <image.vmdk> <converted_image.qcow2>
```

There are more necessary steps involved to make it work inside the QEMU [[Virtual Machine]].

Explanations for the parameters.

`-f`: first image format
`-O`: output image format