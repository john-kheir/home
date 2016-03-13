# Intro

g8os is a grid based Operating System.

process
- bootstrap os booted from USB or VM (template in cloud)
    - bootstrap OS v 0.9:
        - kernel
        - g8os_core
        - ssh daemon
        - networking tools (vxlan, openvswitch, ip)
        - docker / kvm 
        - mc
    - can start from minimal OS distro (arch? or ...)
- core get started and does the following
    - start network
        - configure using net.toml 
            - use  /etc/g8os/net.toml
            - check if we can reach at least 1 of agentcontrollers
        - if cannot get to agentcontroller
            - use dhcp on each interface (do 1 by 1) and check dhcp ok and connection to agentcontroller, stop when connection found
            - keep other interfaces configured as specified in net.toml
        - if still cannot get to agentcontroller after trying dhcp
            -  go over each interface configure as
                - 10.254.254.X  X is random chosen until no conflict (addr conflict, could be because other node was in same failback plan)
                - check agentcontroller connection on 10.254.254.254
                - stop when found
        - if agentcontroller still not found, keep on repeating process above (for ever)
    - mount encrypted filesystem (for config info)
        - connect to agentcontroller over https 
            - post macaddr
            - will retrieve an unlock key from AC
        - use this unlock key to mount
            - /etc/g8os/private/
            - unlock key is encryption key to mount this filesystem (encfs?)
            - mount as /mnt/etc
    - re-establish connection to AC over SSL
        - from now on use SSL keys to connect to AC
        - check AC connection still ok with SSL keys
            - if not ok keep on retrying process 
    - start ssh daemon
        - use ssh keys in /mnt/etc/ssh/...
        - now a root can access using authorization info as specified in /mnt/etc/ssh/...
    - start g8os_fs
        - mount sandbox for
            - os tools
            - jumpscale
            - G8OS binaries
            - ovs
- ays robot will now manage grid
    - ays repo created/checkedout on controller
    - in here nodes are added
    - apps are linked to nodes
    - ays manages install & process management & monitoring
        - in fact full app lifecycle management is done by ays 

## Architecture
![Sequence Diagram](http://www.plantuml.com/plantuml/img/NL9DZnCn3BtdL_W84imFMAb8PSMA5Mn158bBBsxYpaJDs2F7NJJyUfpfTa1xYkAyZxoNMBP2i9D4y574gYbEK-O-X32XMevvGZQu5pQLKaW1AyHNPqfjYY5iDl38sJAM_0Sj2yDc4qAlSfbWH_PRz0p7PkCk0U7z1y0x-2gOWCawax44B0O_TOOep1IRHWCwCjwzceF9WUDwiK2b4ZnWBfJyw0PSRHev3N42Ps8f1yvif7p2IDLd1CUvBJUPKeuOpojxMslk6HGvoGZLF5s4n-_W-uFVO8O1DKMlCVaq42Vti6LTqeUkwvPwFZkX3dYcrimYxhds3VUqlG_nnUqJHvsd9UGNcWEB4SXpApyyoSKxfol0tHxsSAdjmMmWK3BDzEpZCyrriM_SrUW7lRHovK2jvOfS73JtWuLVc0rEebxWEBRRmaazClR45hQBeevOG2RIvOrhzy-enVIKkolasmtImluVOc_-Vy0_HK8QNG7Ur3gy0xBe0czNkRy0)
## Config files

#### [Main config file](docs/config/generic.md)
#### [Network config file](docs/config/network.md)
