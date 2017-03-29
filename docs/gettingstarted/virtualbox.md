# Installing Core0 on VirtualBox

Steps:

- [Build an initramsfs](#build-initramsfs)
- [Create a bootable disk image](#create-bootable)
- [Create a new virtual machine on VirtualBox](#create-vm)
- [Create a port forward from the VM to your host to expose the Redis of the core0](#create-portforward)
- [Start the virtual machine](#start-vm)
- [Ping the core0](#ping-core0)


<a id="build-initramsfs"></a>
## Build an initramsfs

See the [initramfs README.md](https://github.com/g8os/initramfs/blob/master/README.md) to know how to proceed.


<a id="create-bootable"></a>
## Create a bootable disk image with the initramfs created in previous step

```shell
dd if=/dev/zero of=g8os.img bs=1M count=64
mkfs.vfat g8os.iso
mount g8os.iso /mnt
mkdir -p /mnt/EFI/BOOT
cp staging/vmlinuz.efi /mnt/EFI/BOOT/BOOTX64.EFI
umount /mnt
```

<a id="create-vm"></a>
## Create a new virtual machine on VirtualBox  

Select a Linux 64bit:  

![create vm](images/create_vm.png)  

Before starting the virtual machine make sure you enabled the EFI support in the settings of the virtual machine:  

![create vm](images/enable_efi.png)  


<a id="create-portforward"></a>
## Create a port forward from the VM to your host to expose the Redis of the core0

![port forward](images/portforward.png)

<a id="start-vm"></a>
## Start the VM

Use the disk created a step 2 as boot disk

<a id="ping-core0></a>
## Ping the core0

Using the Python client:

```python
from g8os.client import Client
cl = Client(self, host, port=6379, password='')
cl.ping() # this should return 'pong'
```
