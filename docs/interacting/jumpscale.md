# JumpScale Client

The [Python client](python.md) (`g8core`) is available under `j.clients.g8os`.

The below script expects that you know the IP address of the Core0 and that you can access it from the machine running the script. A custom [ZeroTier](https://www.zerotier.com/) network is used for that.

See the [Getting Started](../gettingstarted/gettingstarted.md) section for the G8OS installation options.

```
import sys
import time
from JumpScale import j

SSHKEY = j.clients.ssh.SSHKeyGetFromAgentPub("ovh_install")
CORE0IP = "{core0-ip-address}"
ZEROTIER = "{zerotier-network-id}"


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
            'https://hub.gig.tech/maxux/flist-ubuntu1604.flist', zerotier=ZEROTIER, storage='ardb://hub.gig.tech:16379')
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

    raise TimeoutError("[-] couldn't get an ip on ZeroTier network")

if __name__ == '__main__':
    main()
```
