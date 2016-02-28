# Intro

g8os is a grid based Operating System.

principles
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
        - use  