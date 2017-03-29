# PXE

We assume you already have a working PXE Boot Environment (dhcp and tftp server).

In order to boot the G8OS kernel via PXE, you can use the popular `PXELINUX` tools.

# Configuration
- On your root tftp directory, create a new directory called `g8os` and put the `vmlinuz.efi` on it.
- Configure the bootfile as well:
```
DEFAULT 1
TIMEOUT 100
PROMPT  1

LABEL 1
    kernel g8os/vmlinuz.efi
```
- Save that config under `pxelinux.cfg` as `default` file or a special name that you can symlink for specific devices.

# Symlink exemples
If you want to boot only some devices, you can symlink a special config for that MAC Address:
```
ln -s g8os 01-2c-88-88-cd-2a-01
```
