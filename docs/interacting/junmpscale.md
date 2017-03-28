# JumpScale Client

This below script expects you know the IP address of the core0 and you can access it from the machine running this script.

An easy way to do it is to build the initramfs with a custom ZeroTier network ID.


 (https://github.com/g8os/initramfs/tree/0.10.0#customize-build)
At boot core0 will connect to the zerotier network and you can assing an IP to it.


```
import sys
import time
from JumpScale import j

SSHKEY = j.clients.ssh.SSHKeyGetFromAgentPub("ovh_install")
CORE0IP = "{core0-ip-address}"
ZEROTIER = "565799d8f62c272e"


def main():
    print("[+] connect to core0")
    cl = j.clients.g8core.get(CORE0IP)

    try:
        cl.ping()
    except Exception as e:
        print("cannot connect to the core0: %s" % e)
        return 1

    try:
        print("[+] create container")
        from IPython import embed
        print("DEBUG NOW 987")
        embed()
        raise RuntimeError("stop debug here")
        container_id = cl.container.create(
            'https://stor.jumpscale.org/public/flists/flist-ubuntu1604.db.tar.gz', zerotier=ZEROTIER)
        print("[+] container created, ID: %s" % container_id)
    except Exception as e:
        print("[-] error during container creation: %s" % e)
        return 1

    container = cl.container.client(container_id)

    print("[+] authorize ssh key")
    container.system('bash -c "echo \'%s\' > /root/.ssh/authorized_keys"' % SSHKEY)

    container.system("apt install ssh -y").get()

    print("[+] start ssh daemon")
    container.system('/etc/init.d/ssh start').get()

    print("[+] get zerotier ip")
    from IPython import embed
    print("DEBUG NOW iu")
    embed()
    raise RuntimeError("stop debug here")
    container_ip = get_zerotier_ip(container)

    print("[+] you can ssh into your container at root@%s" % container_ip)


def get_zerotier_ip(container):
    i = 0

    while i < 10:
        addrs = container.info.nic()
        ifaces = {a['name']: a for a in addrs}

        for iface, info in ifaces.items():
            if iface.startswith('zt'):
                cidr = info['addrs'][0]['addr']
                return cidr.split('/')[0]
        time.sleep(2)
        i += 1

    raise TimeoutError("[-] couldn't get an ip on zerotier network")

if __name__ == '__main__':
    main()
```
