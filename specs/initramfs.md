# initramfs
To start the core0, we currently bundle it in an initramfs.

# Why bundle it ?
We build an initramfs which is bundled with the kernel.
This allow us to sign the kernel one time and make sur that it cannot be altered or replaced on our SecureBoot environment.

# Content
Initramfs contains:
- `busybox`
- `core0`
- `ipfs`
- `fuse` userland tools
- `openssl`
- `redis-server`
- `curl`

# Bootstrap
When the kernel start in the initramfs, the /init script is executed.
This script populate /dev, /proc and /sys and prepare a ramdisk where to boot after.

This is probably not _absolutly_ needed but leaving the initramfs is always a good idea.
In this case, we switch to another ramfs but this can be changed easily.


