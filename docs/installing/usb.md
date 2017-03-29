# Booting from USB

On a EFI enabled machine, it's really easy to boot the G8OS kernel. No bootloader needed. All you need is to copy the kernel on a `FAT32` partition.

## On Linux

We assume that your USB device is `/dev/sdc`, you can make boot the kernel as following:

- Create a FAT32 partition (this will erase the whole device): `mkfs.vfat /dev/sdc`
- Mount the partition: `mount /dev/sdc /mnt/g8os-usb`
- Create the EFI directories: `mkdir -p /mnt/g8os-usb/EFI/BOOT`
- Copy the kernel: `cp v /mnt/g8os-usb/EFI/BOOT/BOOTX64.EFI`
- Unmount the USB Device: `umount /mnt/g8os-usb`

You can now boot on the USB Device with your EFI Enabled system.
