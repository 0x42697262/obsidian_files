> [!INFO]
> Tags: #arch 

----
# 012 Package Installs

## 2022-11-26
`paru -S easyeffects`
```sh
Packages (14) graphene-1.10.8-1  gsl-2.7.1-1
              gst-plugins-bad-libs-1.20.4-3
              gst-plugins-base-libs-1.20.4-3  gstreamer-1.20.4-3
              gtk4-1:4.8.2-1  libadwaita-1:1.2.0-1
              libebur128-1.2.6-1  libsigc++-3.0-3.2.0-1
              orc-0.4.33-1  rnnoise-0.4.1-1  tbb-2021.5.0-2
              zita-convolver-4.0.3-2  easyeffects-7.0.0-1

Total Download Size:   16.80 MiB
Total Installed Size:  85.84 MiB
```

`paru -s netcat`
```sh
Packages (1) gnu-netcat-0.7.1-8

Total Download Size:   0.03 MiB
Total Installed Size:  0.06 MiB
```

## 2022-11-10
`paru -S timeshift`
```sh
Repo (10) run-parts-5.5-1  cronie-1.6.1-1  libgee-0.20.6-1  libsoup-2.74.3-1  rsync-3.2.7-2  vte-common-0.70.1-1  vte3-0.70.1-1  libxklavier-5.4-3  libgnomekbd-1:3.28.1-1  xapp-2.2.15-1
Repo Make (25) docbook-xml-4.5-9  docbook-xsl-1.79.2-7  glib2-docs-2.74.1-1  python-lxml-4.9.1-1  python-pygments-2.13.0-1  python-six-1.16.0-6  python-anytree-2.8.0-5  gtk-doc-1.33.2-1  
    libyuv-r2322+3aebf69d-1  libavif-0.11.1-1  libde265-1.0.9-1  libheif-1.13.0-2  gd-2.3.3-5  jbig2dec-0.19-1  libpaper-1.1.28-2  ijs-0.35-4  poppler-data-0.4.11-2  ghostscript-10.0.0-2  netpbm-10.73.37-2  
    gts-0.7.6.121130-2  gsfonts-20200910-2  graphviz-7.0.1-1  vala-0.56.3-1  gcab-1.5-1  appstream-glib-0.8.2-1
Aur (1) timeshift-22.06.5+12+g92ad80c-2


Packages (35) appstream-glib-0.8.2-1  cronie-1.6.1-1  docbook-xml-4.5-9  docbook-xsl-1.79.2-7  gcab-1.5-1  gd-2.3.3-5  ghostscript-10.0.0-2  glib2-docs-2.74.1-1  graphviz-7.0.1-1  gsfonts-20200910-2
              gtk-doc-1.33.2-1  gts-0.7.6.121130-2  ijs-0.35-4  jbig2dec-0.19-1  libavif-0.11.1-1  libde265-1.0.9-1  libgee-0.20.6-1  libgnomekbd-1:3.28.1-1  libheif-1.13.0-2  libpaper-1.1.28-2
              libsoup-2.74.3-1  libxklavier-5.4-3  libyuv-r2322+3aebf69d-1  netpbm-10.73.37-2  poppler-data-0.4.11-2  python-anytree-2.8.0-5  python-lxml-4.9.1-1  python-pygments-2.13.0-1  python-six-1.16.0-6
              rsync-3.2.7-2  run-parts-5.5-1  vala-0.56.3-1  vte-common-0.70.1-1  vte3-0.70.1-1  xapp-2.2.15-1

Total Download Size:    35.91 MiB
Total Installed Size:  172.65 MiB
```

TimeShift scheduled backups require the cronie.service to be running.
Try:
  `systemctl enable --now cronie.service`
Optional dependencies for timeshift
    btrfs-progs: BTRFS support [installed]
    grub-btrfs: BTRFS snapshots in grub

## 2022-11-09
`pacman -S p7zip`
```sh
Packages (1) p7zip-1:17.04-3

Total Download Size:    2.58 MiB
Total Installed Size:  11.21 MiB
```

## 2022-11-04
`paru -S code`
```sh
Packages (3) electron19-19.1.4-3  ripgrep-13.0.0-2  code-1.73.0-1

Total Download Size:    69.10 MiB
Total Installed Size:  280.16 MiB
```
