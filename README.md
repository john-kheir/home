
see [INTRODUCTION](intro.md)

repo's
- [g8os core](https://github.com/g8os/core0) (Init process and container manager of G8OS)
  - also contains python client for core0. It allows to manage containers, disks and networking of the G8OS
- [g8os fs](https://github.com/g8os/fs) (our virtual filesystem which poweres all our OS'es)
- [g8os stor](https://github.com/g8os/router) (our simple storage system for files served to fs)
- [g8os cmd](https://github.com/g8os/corectl) command line tools
- [hubble](https://github.com/g8os/hubble) (our socket forwarder)
- [builders of G8OS initramfs](https://github.com/g8os/initramfs) (build instructions & scripts)
- [AYS actor templates](https://github.com/g8os/ays_g8os)  (AYS actor templates repository which will contains services related to G8OS.)

Releases:
 - [v0.9.0](https://github.com/g8os/core0/releases/tag/v0.9.0) : First usable beta version of the G8OS.

milestones:
- [0.10.0](https://github.com/g8os/home/milestone/4) :
  - revert usage of IPFS as storage system for flist file.  
    After our tests in 0.9.0 to use IPFS as storage, it turns out that it doesn't fit our need for big Flist. This version revert the usage of IPFS to our own Store.

- [0.11.0](https://github.com/g8os/home/milestone/5) :
  - monitoring / statistics
  - self update
  - container persistance ( maybe using AYS )
  - investigate how to integrate ipfs lib inside core


- [1.0](https://github.com/g8os/home/milestone/2) :
  - First stable version and freezing of the APIs. Backward compatibility contracts start from this version.

see issues
- [https://github.com/g8os/home/issues](https://github.com/g8os/home/issues)
- see issues in each repository listed above

Telegram group to meet the community:
- https://telegram.me/joinchat/BrOCOUGHeT035il_qrwQ2A
