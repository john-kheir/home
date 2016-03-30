#Networking
The core applies the network configuration as follows
- It applies the configuration as configured in the `/etc/g8os/network.toml` file
- It tries to reach at least one of the configured `controllers`
- If it can't reach any, it tries `dhcp` on all interfaces one at a time and try to reach any of the controllers again
- If it still can't reach, it will fall back to random static IP (in range `10.254.254.0/24`) and tries to reach a controller on `10.254.254.254`

The network configuration file is structured as follows
```toml
[network]
auto = true

[interface.<ifname>]
protocol = "<protocol>"

[<protocol>.<ifname>]
#protocol specific configuration
#for that interface
```

The `[network]` section currently only have the `auto` flag, which tells core to auto configure all found interfaces using the dhcp method if there is no specific `interface` section for that interface.
if `auto` is set to false, the `core` will just ignore any interface that is not specificly configured in the network.toml file.

## Network protocols
Currently only the following configurations protocols are supported
### none
The `none` method only brings the interface up it doesn't set an IP on that interface. it also exclude it from the networking fallback plan. Useful if the interface is added to an `openvswitch`.
### dhcp
The `dhcp` method doesn't require any further configurations, specifying `protocl = "dhcp"` is enough.
### static
The `static` method requires a `[static.<if>]` section
Example:
```toml
[interface.eth0]
protocol = "static"

[static.eth0]
ip = "10.20.30.40/24"
gateway = "10.20.30.1"
```

### OVS example
Openvswitch services are started before processing the `network.toml` file. So by the time of processing the `network.tom` file all bridges should be in place.
After that, all tap devices in the `network.toml` file are going to be created.

```bash
ovs-vsctrl add-br br0
ovs-vsctrl add-port br0 eth0
ovs-vsctrl add-port br0 port1
```

```toml
[interface.lo]
protocol = "static"

[static.lo]
ip = "127.0.0.1/8"

[interface.br0]
protocol = "dhcp"

[interface.eth0]
protocol = "none"
```

The final result of this setup should be something like the following
```
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
2: eth0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc pfifo_fast master ovs-system state UP group default qlen 1000
    link/ether 08:00:27:b8:5a:7b brd ff:ff:ff:ff:ff:ff
3: ovs-system: <BROADCAST,MULTICAST> mtu 1500 qdisc noop state DOWN group default
    link/ether ea:ac:67:3f:18:42 brd ff:ff:ff:ff:ff:ff
4: br0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue state UNKNOWN group default
    link/ether 08:00:27:b8:5a:7b brd ff:ff:ff:ff:ff:ff
    inet 10.254.254.79/24 scope global br0
       valid_lft forever preferred_lft forever
5: port1: <NO-CARRIER,BROADCAST,MULTICAST,UP> mtu 1500 qdisc noqueue master ovs-system state DOWN group default qlen 500
    link/ether c2:36:82:75:04:51 brd ff:ff:ff:ff:ff:ff
```

```
Bridge "br0"
    Port "port1"
        Interface "port1"
    Port "br0"
        Interface "br0"
            type: internal
    Port "eth0"
        Interface "eth0"
```