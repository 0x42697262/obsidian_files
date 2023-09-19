
### 1. Create the subvolumes
`btrfs su sn / /@` - for the /root partition
`btrfs su sn /home /home/@home` - for the /home partition

### 2. Mount the partitions
`mount /dev/nvme0n1pROOT /mnt -o subvol=@` - mount root to /mnt
`mount /dev/nvmen1HOME /mnt/home -o subvol=@home` - mount home to /home

### 3. Arch-chroot
`arch-chroot /mnt` - might need to install arch-install-scripts

### 4. Edit /etc/fstab
`nvim /etc/fstab`
Remove all `subvolid`s that exists.
Change `subvol=/` to `subvol=/@` for root, and `subvol=/home` to `subvol=/@home`.

### 5. Mount /boot/efi
`mount /dev/nvme0n1pBOOT /boot/efi` - mount /boot/efi

### 6. Reinstall Grub
`grub-mkconfig -o /boot/grub/grub.cfg` then
`grub-install --target=x86_64-efi --efi-directory=/boot/efi --bootloader-id=ARCH`

Then do `mkinitcpio -P`.

Exit and then reboot.

### 7. Check if Arch booted to the new subvolume
`cat /etc/mtab | grep btrfs`
*Note that the /etc/mtab must contain the edited /etc/fstab file.*

### 8. Cleanup
`mount /dev/nvme0n1ROOT /mnt` then delete all folders inside `/mnt` except `/mnt/@`.
`umount /mnt; mount /dev/nvme0n1pHOME /mnt` then delete all user folders except `/mnt/@home`.

### 9. Done
I think we are done! Lol this is all thanks to `i0bz` on Arch Linux discord server (unofficial)